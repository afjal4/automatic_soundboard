import os
import threading
from multiprocessing import Queue
from abc import ABC, abstractmethod
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer
from random import shuffle
from time import sleep
from sound_databases import convert_sound_name_array_to_files
from sound_databases import get_file_from_location, get_file_from_soundID
from sound_databases import locations_list


class AbstractAspect(ABC):
    __volume = 0.5
    __muted = False
    __damper = 1
    # damper = masterVolume * maxVolume

    def initialiseMixer(self):
        if not mixer.get_init(): mixer.init()

    def setDamper(self, pDamper):
        self.__damper = pDamper
    def getDamper(self):
        return self.__damper

    def setVolume(self, pVol : float):
        if 0 <= pVol <= 1:
            self.__volume = pVol
        elif pVol > 1: self.__volume = 1
        elif pVol < 0: self.__volume = 0
    def getVolume(self):
        return self.getRawVolume() if not self.getMuted() else 0
    def getRawVolume(self):
        return self.__volume

    def setMuted(self, mute: bool):
        self.__muted = mute
    def getMuted(self):
        return self.__muted
    
class MasterVolumeAspect(AbstractAspect):
    def __init__(self):
        super().__init__()
        self.setVolume(1)

class SoundAspect(AbstractAspect):
    __abs_volume = 0.5
    #abs_volume = volume * master_volume * max_volume, or self.volume * damper

    def __init__(self):
        super().__init__()
        self.__setAbsVolume(self.getVolume())

    def __setAbsVolume(self, pVol : float):
        #depends on volume so cannot be set directly
        if 0 <= pVol <= 1: self.__abs_volume = pVol
        elif pVol > 1: self.__abs_volume = 1
        elif pVol < 0: self.__abs_volume = 0
    def getAbsVolume(self):
        return self.__abs_volume if not self.getMuted() else 0
    
    def updateVol(self, volume : float = None, damper : float = None):
        # Stores damper if one is given, where damper = masterVol * maxVol
        if damper != None: self.setDamper(damper)

        # Sets volume if volume is given
        if volume != None:
            self.setVolume(volume)

        new_abs_vol = self.getVolume() * self.getDamper()  
        self.__setAbsVolume(new_abs_vol)
        self.updateMixerVolume(self.getAbsVolume())
    
    @abstractmethod
    def updateMixerVolume(): ...

class ChanneledAspect(SoundAspect):
    __channel_ID = 0

    def __init__(self, pChannelID : int):
        self.setChannelID(pChannelID)

    def setChannelID(self, pChannelID : int):
        self.__channel_ID = pChannelID
    def getChannelID(self):
        return self.__channel_ID

    def updateMixerVolume(self, volume : float):
        if mixer.get_init(): mixer.Channel(self.getChannelID()).set_volume(volume)

class SoundEffectAspect(ChanneledAspect):
    def playSoundID(self, ID : str):
        if not ID: return

        file = get_file_from_soundID(ID)
        if not file:
            print(f"SoundManager: Couldn't find file associated with ID {ID}")
            return
        
        self.playSoundEffectFile(file)

    def playSoundEffectFile(self, file : str):
        if not os.path.isfile(file): 
            print(f"SoundManager: {file} is no longer a file")
            return
        sound = mixer.Sound(file)
        channel = mixer.Channel(self.getChannelID())
        channel.play(sound)
        while channel.get_busy():
            sleep(0.1)

class BackingTrackAspect(SoundAspect):
    __location = None
    swap_fade = 500
    end_fade = 2000
    offload_optimisation = False

    def __setLocation(self, pLocation : str):
        if not pLocation: self.__location = None; return
        if pLocation not in locations_list():
            print(f"SoundManager: {pLocation} has no associated file")
        self.__location = pLocation

    def updateLocation(self, pLocation : str):
        if not pLocation: 
            self.terminateCurrentTrack(fade_ms=self.end_fade)
            self.__setLocation(None)
            return
        if pLocation not in locations_list():
            print(f"SoundManager: {pLocation} has no associated file")
            return
        
        different = self.getLocation() != pLocation
        self.__setLocation(pLocation)
        if different: self.updateTrack(pLocation)  

    def getLocation(self):
        return self.__location
    
    def terminateCurrentTrack(self, fade_ms : int = 2000):
        if not mixer.get_init(): return
        if not mixer.music.get_busy(): return
        mixer.music.fadeout(fade_ms)
        if self.offload_optimisation: mixer.music.unload()

    def swapTrack(self, file : str):
        if not mixer.get_init(): return

        self.terminateCurrentTrack(fade_ms=self.swap_fade)
        mixer.music.load(file)
        mixer.music.play(-1)

    def updateTrack(self, location : str):
        file = get_file_from_location(location)
        if not file:
            print(f"SoundManager: Couldn't find file associated with location {location}")
            return
        if not os.path.isfile(file):
            print(f"SoundManager: File {file} no longer exists")
            return
        
        self.swapTrack(file)

    def updateMixerVolume(self, volume : float):
        if not mixer.get_init(): return
        mixer.music.set_volume(volume)

class SoundManager:
    master = MasterVolumeAspect()

    #when adding an aspect:
    #update self.updateVols method to add main_slider support
    backing_track = BackingTrackAspect()
    soundboard = SoundEffectAspect(pChannelID=0)
    sound_effects = SoundEffectAspect(pChannelID=1)
    previews = SoundEffectAspect(pChannelID=0)

    __max_volume = 1

    def __init__(self):
        self.updateVols()

    def setMaxVolume(self, pVol : float):
        self.__max_volume = pVol
    def getMaxVolume(self):
        return self.__max_volume

    def setMasterVolume(self, pVol : float):
        self.master.setVolume(pVol)
        self.updateVols()
    def getMasterVolume(self):
        return self.master.getVolume()
    def getRawMasterVolume(self):
        return self.master.getRawVolume()

    def updateVols(self):
        damper = self.getMaxVolume() * self.getMasterVolume()
        damper_ignore_mute = self.getMaxVolume() * self.getRawMasterVolume()

        self.backing_track.updateVol(damper = damper)
        self.soundboard.updateVol(damper = damper)
        self.sound_effects.updateVol(damper = damper)
        self.previews.updateVol(damper = damper_ignore_mute)

    def __setMasterMute(self, mute : bool):
        self.master.setMuted(mute)
        self.updateVols()
    def getMasterMute(self):
        return self.master.getMuted()
    
    def mute(self):
        self.__setMasterMute(True)
    def unmute(self):
        self.__setMasterMute(False)
    def toggleMute(self):
        self.__setMasterMute(not self.master.getMuted())
    def setMute(self, muted : bool):
        self.__setMasterMute(muted)

    def getVols(self):
        return (self.getMasterVolume(), self.backing_track.getVolume(), self.backing_track.getAbsVolume())

def __ProcessNER(sound_tokens : list, sound_manager : SoundManager):
    files = convert_sound_name_array_to_files(sound_tokens)
    shuffle(files)
    for f in files:
        sound_manager.sound_effects.playSoundEffectFile(f)

def __ProcessLDA(data, sound_manager : SoundManager):
    ...

def __ProcessCS(data, sound_manager : SoundManager):
    ...

def __ProcessSignalQueue(q : Queue, sound_manager : SoundManager):
    #Takes in tokens of format (Signal, Data)
    while True:
        while not q.empty():
            current = q.get()
            try: signal, value = current
            except ValueError:
                print(f"SignalQueue: {current} is an Invalid Signal Token")
                continue
            
            #Mute Button
            if signal == 'mute_button': sound_manager.setMute(value); continue

            #Adjusters - tags depend on adjuster.ObjectName, do not edit
            if signal == 'music_dial': sound_manager.backing_track.updateVol(value); continue
            if signal == 'auto_sound_dial': sound_manager.sound_effects.updateVol(value); continue
            if signal == 'soundboard_dial': sound_manager.soundboard.updateVol(value); continue
            if signal == 'vol_slider': sound_manager.setMasterVolume(value); continue

def __ProcessSoundQueue(q : Queue, sound_manager : SoundManager):
    #Takes in tokens of format (Type, Data)
    while True:
        while not q.empty():
            current = q.get()
            try: tag, data = current
            except ValueError:
                print(f"SoundQueue: {current} is an Invalid Sound Token")
                continue
            
            ##UI Tags
            if tag == 'Soundboard': sound_manager.soundboard.playSoundID(data); continue
            if tag == 'Location': sound_manager.backing_track.updateLocation(data); continue
            if tag == 'Preview': sound_manager.previews.playSoundID(data); continue
            ##NLP Tags
            if tag == 'NER': __ProcessNER(data, sound_manager); continue
            #not yet supported vvv
            if tag == 'LDA': __ProcessLDA(data, sound_manager); continue
            if tag == 'CosSim': __ProcessCS(data, sound_manager); continue

            print(f"SoundQueue: {current} is an invalid token")

def Player(sound_queue : Queue, signal_queue: Queue):
    mixer.init()
    sound_manager = SoundManager()

    SoundPlayer = threading.Thread(target=__ProcessSoundQueue, args=(sound_queue,sound_manager,))
    SignalReciever = threading.Thread(target=__ProcessSignalQueue, args=(signal_queue,sound_manager,))
    SoundPlayer.start()
    SignalReciever.start()
