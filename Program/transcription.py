import whisper
from multiprocessing import Queue
from vad import EnergyVAD
from torchaudio import load
import os
import time

def VAD(audio : str) -> float:
    #(i) returns % of audio file that is speech

    # Time "speech" segment needs to last for it to be accepted as speech
    segment_time_threshold = 100#ms
    rate = 16000#Hz
    
    try:
        eVAD = EnergyVAD(sample_rate=rate,
                         energy_threshold= 0.002)
        vad_file = eVAD(audio)
    except:
        print("VAD: error with Energy VAD")
        # If there is an error in VAD, accept file regardless
        return 1
    
    vad_file = [int(n) for n in vad_file]
    vad_str = ''.join([str(n) for n in vad_file]) #concatenate all numbers
    speech_segments = vad_str.split('0') #separating segments of speech
    speech_segments = [int(len(seg)) for seg in speech_segments] #finding lengths of intervals of 1s
    speech_segments = [seg for seg in speech_segments if seg > segment_time_threshold / eVAD.frame_length] #filtering out short segments
    # sum is number of active frames, len is total frames
    speech_percentage = sum(speech_segments) / len(vad_file) if len(vad_file) != 0 else 0 #rejects if length zero
     
    return speech_percentage  

def WhisperSpeechProbability(result : dict) -> float:
    try: #catches times when whisper format glitches  
        return 1 - result['segments'][0]['no_speech_prob']
    except: return 1

def Transcriber(audio_queue : Queue, corpus_queue : Queue, model : str = "small.en"):
    # Parameters for corpus rejection
    speech_prob_threshold = 0.5
    time_to_live = 15
    vad_threshold = 0.01

    # Tokens that are instantly rejected
    invalid_text = [' Thank you.', '']

    # Loading transcription model
    Whisper = whisper.load_model(model)

    while True:
        while not audio_queue.empty():
                
 
            audio_bytes, timestamp = audio_queue.get()
            result = {}

            # Validation
            activity = VAD(audio_bytes)
            if activity < vad_threshold: 
                print(f"VAD: File Rejected, {activity} below threshold")
                continue
            if time.time() - timestamp > time_to_live: 
                print(f"Time Out: File Rejected as age exceeded time to live")
                continue

            try:
                result = Whisper.transcribe(
                    audio = audio_bytes,
                    # Disables punctuation
                    prepend_punctuations='', append_punctuations='',
                    # Temperature - How deterministic/absolute Transcript is
                    temperature= 0.1,
                    # Additional Params
                    fp16 = False, language = "English")
            except: 
                print('Whisper: Error Transcribing')

            if not result: continue
            text = result['text']

            # Final Validation
            if text in invalid_text: continue
            if WhisperSpeechProbability(result) < speech_prob_threshold: continue
            
            print(text)
            corpus_queue.put(text)

#Testing
if __name__ == "__main__":
    from random import choice
    tot=0
    for _ in range(5):
        print('Playing')
        print(tot)
        tot += choice([3.675845,5.782450,1.043249])