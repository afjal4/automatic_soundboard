from pydub import AudioSegment
import numpy as np
import pyaudio
from time import time
from numpy import array
from multiprocessing import Queue


def CalculateOverlap(sound : AudioSegment, time_s = int) -> AudioSegment:
    # Return the entire sound if the overlap time is larger than the actual duration
    if sound.duration_seconds <= time_s: 
        return sound
    else: 
        return sound[-1000 * time_s:]

def RecordSpeech(audio_queue : Queue, transcription_interval : int = 10):
    #(i) process records audio continuously to a given wave file
    RATE = 16000
    CHANNELS = 1
    WIDTH = 2
    CHUNK = 1024

    overlap_s = 2
    frames_per_interval = int((16000 / 1024) * transcription_interval)

    # Params required for Whisper
    sound = AudioSegment(b'', sample_width = WIDTH, frame_rate = RATE, channels = CHANNELS)

    # Iitialises PyAydio
    pa = pyaudio.PyAudio()
    Stream = pa.open(rate=RATE,
                    channels=CHANNELS,
                    frames_per_buffer=CHUNK,
                    input=True,
                    format= pyaudio.paInt16)

    while True:
        # Empties buffer
        frames = []
        # Records for transcription_interval s
        for _ in range(0, frames_per_interval):
            frame = Stream.read(CHUNK)
            frames.append(frame)

        # Concatenates frames into bytes
        audio = b''.join(frames)

        # Adds overlap from previous to audio
        overlap = CalculateOverlap(sound, overlap_s)
        sound = AudioSegment(audio, sample_width = WIDTH, frame_rate = RATE, channels = CHANNELS)
        final_sound = sound + overlap

        # Conversion to Whisper format using AudioSegment methods
        if final_sound.frame_rate != 16000: # 16 kHz
            final_sound = final_sound.set_frame_rate(16000)
        if final_sound.sample_width != 2:   # int16
            final_sound = final_sound.set_sample_width(2)
        if final_sound.channels != 1:       # mono
            final_sound = final_sound.set_channels(1)
        # Converts AudioSegment back to bytes array
        bytes_array = np.array(final_sound.get_array_of_samples())
        normalised_array = bytes_array.astype(np.float32) / -32768.0 #normalisation
        
        # Adds timestamp to implement time to live of timeslice
        audio_queue.put((normalised_array, time()))


#for testing:
if __name__ == "__main__":
    RecordSpeech(10)
    #RecordSpeech(2.5,"SessionRecordings/book.wav"))
    #GenerateContinuousFileSlices("SessionRecordings/book.wav", 10000,(1,2,16000,1024))
    ...
