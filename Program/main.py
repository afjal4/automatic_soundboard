#Utility
from multiprocessing import Process, Queue
import time
import sys
from random import randint, shuffle
import pickle
#UI
from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt, QTimer
from UI.ui import Ui_Application as UI
import darkdetect, qdarktheme
#Dialogs
from widgets import AudioManagerDialog, KeywordManagerDialog
#Processes
from recording import RecordSpeech
from nlp import NLProcesser
from transcription import Transcriber
from output import Player
#Database Access
from sound_databases import create_sound_databases
from sound_databases import locations_list, sounds_list

class Soundboard(qtw.QMainWindow, UI):
    # Queues to interact with Processes outside of GUI
    audio_queue = Queue()
    corpus_queue = Queue()
    sound_queue = Queue()
    signal_queue = Queue()

    # Labels for soundboard, stored in pickle
    soundboard_pickle_file = r"Program\SaveData\saved_soundboard.pkl"
    soundboard_labels = {'soundboard': {},
                         'locations' : {}}

    # Button Disabling
    button_cooldown_time_ms = 300
    __disabled_buttons = set()

    # Editing Mode attributes
    isEditing = False
    SOUNDS = 'soundboard_option'
    LOCATIONS = 'location_option'
    editingOption = SOUNDS #one from above

    # Recording Parameters
    recording_interval = 10 #seconds
    model_size = "small"
    current_location = ''

    # Processes
    SoundPlayer = Process(target=Player, args=(sound_queue,signal_queue,))
    # Auto-Soundboard processes, set by method setAutoSoundProcesses
    Recorder = Process() 
    Transcriber = Process()
    NLProcesser = Process()

    def __init__(self):
        super().__init__()

        ## SetUp UI
        self.ui = UI
        UI.setupUi(self, self)

        ## At Start
        create_sound_databases()
        self.is_dark_theme = darkdetect.isDark()
        self.setAutoSoundProcesses()
        self.SoundPlayer.start()
        self.Utility.setProperty("currentIndex", 0)#set to notes page
        self.__loadSoundboards()
        
        ## GUI Element Connections
        # Toolbar
        self.actionOpen_Manager_S.triggered.connect(self.openSoundManager)
        self.actionOpen_Manager_K.triggered.connect(self.openKeywordManager)
        self.actionDark_Mode.triggered.connect(self.toggleDarkMode)

        # QTabWidget Buttons
        self.DiceButtons.buttonClicked.connect(self.__diceRoll)
        self.Utility.currentChanged.connect(self.tabChanged)
        self.EditChoices.buttonClicked.connect(self.__updateEditOptionChosen)
        self.save_sb_button.clicked.connect(self.__saveSoundboardsClicked)

        # Buttons
        self.aut_soundboard_toggle.toggled.connect(self.updateAutoSound)
        self.LocationButtons.buttonClicked.connect(self.__locationChosen)
        self.SoundboardButtons.buttonClicked.connect(self.__soundboardPressed)
        self.mute_toggle.clicked.connect(self.updateMute)

        # Sliders and Dials
        self.music_dial.valueChanged.connect(lambda: self.__updateAbstractSliderVol(self.music_dial))
        self.soundboard_dial.valueChanged.connect(lambda: self.__updateAbstractSliderVol(self.soundboard_dial))
        self.auto_sounds_dial.valueChanged.connect(lambda: self.__updateAbstractSliderVol(self.auto_sounds_dial))
        self.vol_slider.valueChanged.connect(lambda: self.__updateAbstractSliderVol(self.vol_slider))

        self.show()
    
    ##Button Functionality
    def __soundboardPressed(self, button : qtw.QPushButton):
        # If Soundboard is being edited, click to rename
        if self.isEditing and self.editingOption == self.SOUNDS:
            self.__renameButton(button)
            return
        
        # Gets label on button and enqueues
        sound = button.text()
        if not sound: return 
        self.sound_queue.put(("Soundboard", sound))
        self.__cooldown(button)
            
    def __locationChosen(self, button : qtw.QPushButton):
        
        if button.objectName() == 'empty': #blank button always mutes
            self.sound_queue.put(("Location", None))
            return
        
        # If Locations are being edited, click to rename
        if self.isEditing:
            if self.isEditing and self.editingOption == self.LOCATIONS:
                self.__renameButton(button)
            return

        # Gets label on button and enqueues
        location = button.text()
        # But doesn't send a new sound input if the location hasn't changed
        if location == self.current_location: return
        self.current_location = location   
        self.sound_queue.put(("Location", location))
             
    def __cooldown(self, button : qtw.QAbstractButton, time_ms = None):
        # Sets to default wait time if no parameter is given
        if not time_ms: time_ms = self.button_cooldown_time_ms
        button.setDisabled(True)
        QTimer.singleShot(time_ms, lambda: button.setEnabled(True))

    def __updateAbstractSliderVol(self, adjuster : qtw.QAbstractSlider):
        # Enqueues the slider name along with the the % Dialed
        scaled_value = round(adjuster.value() / adjuster.maximum(), 4)
        self.signal_queue.put((adjuster.objectName(), scaled_value))

    def setAutoSoundProcesses(self):
        # Sets processes so they can be recalled
        self.Recorder = Process(target=RecordSpeech, args=(self.audio_queue,))
        self.NLProcesser = Process(target=NLProcesser, args=(self.corpus_queue,self.sound_queue,))
        self.Transcriber = Process(target=Transcriber, args=(self.audio_queue, self.corpus_queue,))

    def updateAutoSound(self):
        # Checks if the board button is enabled and updates accordingly
        if self.aut_soundboard_toggle.isChecked(): 
            self.enableAutoSound()
        else: self.disableAutoSound()

    def enableAutoSound(self):
        # Starts necessary processes
        for p in [self.Recorder, self.NLProcesser, self.Transcriber]:
            p.start()

    def disableAutoSound(self):
        # Disables processes required to use the Auto Soundboard
        for p in [self.Recorder, self.NLProcesser, self.Transcriber]:
            p.terminate()
            p.join()
        # Resets these processes so they can be played again
        self.setAutoSoundProcesses()

    def updateMute(self):
        # Checks if the mute button is toggled
        isMuted = self.mute_toggle.isChecked()
        # Enqueues muted condition to sound player
        self.signal_queue.put(("mute_button", isMuted))
        # Changes text to prompt what to do next
        if isMuted:
            self.mute_toggle.setText("Unmute")
        elif not isMuted:
            self.mute_toggle.setText("Mute")
    
    ##Button Disabling - for Sound Effect buttons that don't have a valid sound assigned
    def getDisabledButtons(self) -> set[qtw.QPushButton]:
        return self.__disabled_buttons
    
    def addDisabledButton(self, button : qtw.QPushButton):
        self.__disabled_buttons.add(button)

    def removeDisabledButton(self, button : qtw.QPushButton):
        self.__disabled_buttons.discard(button)

    def setDisabledButtons(self, isDisabled : bool = True):
        for button in self.getDisabledButtons():
            button.setDisabled(isDisabled)

    ##QTabWindow
    def tabChanged(self, index : int):
        # Ensures that editing mode is off, but is turned on when it runs editTabOpened()
        self.isEditing = False
        # Disables all buttons that are inactive, but these are again re-enabled when editing
        self.setDisabledButtons(isDisabled=True)
        # Allows all location buttons to be checked as this is disabled when edit is opened
        for button in self.LocationButtons.buttons():
            button.setCheckable(True)
        # Runs page-specific opening protocol
        page = self.Utility.currentWidget().objectName()
        if page == 'Edit': self.__editTabOpened()
        if page == 'Dice': self.__diceOpened()
        if page == 'Notes': self.__notesOpened()
    
    #Edit tab
    def __editTabOpened(self):
        self.isEditing = True
        self.setDisabledButtons(isDisabled=False)
        self.current_location = ''

        # Disables Location buttons from being Checked and stops music
        for button in self.LocationButtons.buttons():
            # Sets the Mute button to be highlighted
            if button.objectName() == 'empty':
                button.setChecked(True)
            else:
                button.setCheckable(False)
        self.sound_queue.put(('Location', None))
        self.__updateEditOptionChosen()

    def __updateEditOptionChosen(self):
        # Detects what option is chosen on Radio buttons
        option = self.EditChoices.checkedButton().objectName()
        self.editingOption = option
        # Updates the Combo Box to show which is selected
        self.updateComboBox()

    def updateComboBox(self):
        # Chooses items to populate combo_box based on editing option chosen
        items = []
        if self.editingOption == self.SOUNDS: 
            items = sounds_list()
        elif self.editingOption == self.LOCATIONS: 
            items = locations_list()
        items.append('CLEAR') # Empty Option
        self.comboBox.clear()
        self.comboBox.addItems(items)

    def __renameButton(self, button : qtw.QPushButton):
        # Sets name to the current contents of the combo-box
        new_name = self.comboBox.currentText()

        # If a soundboard_button is being renamed, adds disabling function
        if self.editingOption == self.SOUNDS:
            if new_name == 'CLEAR': self.addDisabledButton(button)
            else: self.removeDisabledButton(button)

        # Generates default label if it is cleared
        if new_name == 'CLEAR':
            # Generates label in the form Slot X
            if self.editingOption == self.SOUNDS:
                new_name = self.__formatObjectLabel(button)
            # Label is blank
            if self.editingOption == self.LOCATIONS:
                new_name = ''

        button.setText(new_name)

    def __saveSoundboardsClicked(self):
        if self.saveSoundboards():
            # Plays if saveSoundboards() emits true signal
            self.saveSuccess()
    
    #Notes tab
    def __notesOpened(self):
        ...
    
    #Dice tab
    def __diceOpened(self):
        ...

    def __diceRoll(self, button : qtw.QPushButton):
        dice_type = button.text()
        # Validation for if the button name isn't an int
        try: dice_type = int(dice_type)
        except: 
            print(f"{dice_type} is invalid")
            return
        
        # Adjusts the LCD number value with random integer
        self.lcdNumber.setProperty("value",randint(1, dice_type))
        self.__cooldown(button)

    ##Menu Bar Functionality
    def toggleDarkMode(self):
        self.is_dark_theme = not self.is_dark_theme
        # Updates theme based on new toggled value
        if self.is_dark_theme: qdarktheme.setup_theme("dark")
        else: qdarktheme.setup_theme("light")
        
    def openSoundManager(self):
        dlg =AudioManagerDialog(self)
        self.__openDialog(dlg, exec = False, is_modal=False)

    def openKeywordManager(self):
        dlg = KeywordManagerDialog(self)
        self.__openDialog(dlg, exec = True, is_modal=True)
    
    def __openDialog(self, dialog : qtw.QDialog, exec : bool = True, is_modal : bool = False):
        #! Behaves unpredictably so upon error, change the modality / exec params
        # Modality - whether it disables the QMainWindow when active
        modality = Qt.WindowModality.WindowModal if is_modal else Qt.WindowModality.NonModal
        dialog.setWindowModality(modality)

        # Keeps dialog on top of QMainWindow
        dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)

        # .exec runs file differently from .show
        if exec: dialog.exec()
        else: dialog.show()

    def playSoundPreviewFromDialog(self, sound : str):
        self.sound_queue.put(("Preview", sound))

    ##Pickle - implementation of soundboard layout saving
    def saveSoundboards(self):
        # Records current labels
        self.__updateSoundboardLabels()
        # Saves to .pkl file
        with open(self.soundboard_pickle_file, 'wb') as f:
            pickle.dump(self.soundboard_labels, f)
        f.close
        # Sends signal if successful
        return True

    def __loadSoundboards(self):
        # Opens and updates saved soundboard layout upon start
        with open(self.soundboard_pickle_file, 'rb') as f:
            self.soundboard_labels = pickle.load(f)
        f.close
        self.__loadSoundboardLabels()
    '''
    soundboard_labels = {'soundboard' : {buttonID : label,
                                        ...},
                        'locations' : {buttonID : label,
                                        ...}}
    '''
    def __updateSoundboardLabels(self):
        for button in self.SoundboardButtons.buttons():
            ID = self.SoundboardButtons.id(button)
            self.soundboard_labels['soundboard'][ID] = button.text()
        for button in self.LocationButtons.buttons():
            ID = self.LocationButtons.id(button)
            self.soundboard_labels['locations'][ID] = button.text()

    def __loadSoundboardLabels(self):
        valid_sounds = sounds_list()
        valid_locations = locations_list()

        # Generates Soundboard Labels
        for ID, label in self.soundboard_labels['soundboard'].items():
            # Sets label to placeholder if it is an invalid sound
            if label not in valid_sounds: 
                button = self.SoundboardButtons.button(ID)
                self.addDisabledButton(button)
                # Sets the name to be in form 'Slot X'
                label = self.__formatObjectLabel(button)

            self.SoundboardButtons.button(ID).setText(label)
        self.setDisabledButtons(isDisabled=True)

        # Generates Locations Labels
        for ID, label in self.soundboard_labels['locations'].items():
            if label not in valid_locations: label = ''
            self.LocationButtons.button(ID).setText(label)

    def __formatObjectLabel(self, button : qtw.QPushButton):
        label = button.objectName()
        # Label in form TYPE_ID, converts to "TYPE ID"
        return "".join([part+' ' for part in label.split('_')]).strip()

    def saveSuccess(self):
        # Changes the text of all of the buttons one by one, then reverts changes
        # Collate buttons
        buttons = self.SoundboardButtons.buttons() + self.LocationButtons.buttons()
        
        # Saves the formatting of the buttons
        original_stylesheet = [button.styleSheet() for button in buttons]
        
        # Chooses color based on darkmode
        if self.is_dark_theme: color = '#FFFF00' #yellow
        else: color = '#660099' #purple

        # Randomises order of buttons
        shuffled_buttons = buttons.copy()
        shuffle(shuffled_buttons)

        # Sets colour of each button
        time_per_button = 20#ms
        for (i, button) in enumerate(shuffled_buttons):
            self.__setButtonColorDelayed(button, color = color, delay = ((i+1) * time_per_button))
        
        # Wait until every button changes then set to original
        delay = (len(buttons) + 1) * time_per_button
        QTimer.singleShot(delay, lambda: self.__setButtonAppearances(buttons, original_stylesheet))

    def __setButtonColorDelayed(self, button : qtw.QPushButton, color : str, delay : int):
        # Performs function after delay ms
        QTimer.singleShot(delay, lambda : button.setStyleSheet(f"color: {color}"))

    def __setButtonAppearances(self, buttons, stylesheets):
        for button, stylesheet in zip(buttons, stylesheets):
            button.setStyleSheet(stylesheet)

def main():
    # Create the application
    qdarktheme.enable_hi_dpi()
    app = qtw.QApplication(sys.argv)
    qdarktheme.setup_theme("auto")
    # Create the soundboard object, shows itsself in __init__
    soundboard = Soundboard()
    # Runs the main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
