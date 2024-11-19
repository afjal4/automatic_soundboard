from tinydb import Query, TinyDB
from pydub import AudioSegment
import os

keyword_table = "Program\\SaveData\\Tables\\NER_Keywords.json"
KEYWORD = 'word'
SOUND_ID = 'sound_name'
sound_table = "Program\\SaveData\\Tables\\Sounds_Files.json"
SOUND_NAME = 'name'
SOUND_FILE = 'sound_file'
location_table = "Program\\SaveData\\Tables\\Location_Tracks.json"
LOCATION = 'location'
TRACK_FILE = 'sound_file'
track_minimum_threshold = 8000#ms

#Tables
def create_sound_databases():
    if not os.path.isfile(keyword_table):
        open(keyword_table, 'a').close()
    if not os.path.isfile(sound_table):
        open(sound_table, 'a').close()
    if not os.path.isfile(location_table):
        open(location_table, 'a').close()

def reset_tables():
    #(!!!) irreversible
    TinyDB(sound_table).drop_tables()
    TinyDB(keyword_table).drop_tables()
    create_sound_databases()

#Validation
def file_exists(file : str) -> bool:
    exists = os.path.isfile(file)
    if not exists:
        print(f"File: {file}, doesn't exist")
    return exists

def presence(word) -> bool:
    if not word:
        print(f"Please enter a valid string, \"{word}\" is invalid.")
    return bool(word)

def length_check(str : str, max_length : int = 15) -> bool:
    isValid = len(str) < max_length
    if not isValid:
        print(f'{str} is too long, {max_length} char max')
    return isValid

def format_check(str : str) -> bool:
    isValid = True
    # Check for if alphabetical (or has '_')
    string_without_underscores = str.replace('_', '')
    if not string_without_underscores.isalpha():
        print(f'{str}: word should be entirely alphabetical')
        isValid = False
    # Check if has ' '
    if len(str.split(' ')) != 1:
        print(f'{str}: spaces in the phrases should be denoted by an _')
        isValid = False
    return isValid
    
def sound_exists(sound_name : str) -> bool:
    sound_db = TinyDB(sound_table)
    exists = sound_db.contains(Query().name == sound_name.lower())
    if not exists:
        print(f"Sound under name: {sound_name}, doesn't exist")
    return exists


#Inserting and Deleting
def add_sound(name : str, soundfile : str):
    if not file_exists(sound_table): return
    if not file_exists(soundfile): return

    # Validation
    if not presence(name): return
    if not length_check(name, 20): return
    
    db = TinyDB(sound_table)
    sound = db.search(Query().name == name.lower())
    if sound:#exists
        sound = sound[0]
        print(f"A sound under the name: {sound[SOUND_NAME]} already exists.")
        return
    
    db.insert({SOUND_NAME: name.lower(),
                SOUND_FILE: soundfile
                })
    return True #signal that it was successful
    
def add_location_track(location : str, sound_file : str):
    if not file_exists(location_table): return
    if not file_exists(sound_file): return
    if not presence(location): return

    db = TinyDB(location_table)
    record = db.search(Query().location == location.lower())
    if record:
        record = record[0]
        print(f"{record[LOCATION]} already has registered sound: {record[TRACK_FILE]}")
        return
    
    track = AudioSegment.from_file(sound_file)
    if len(track) < track_minimum_threshold:
        print(f"{sound_file} is too short, must exceed {track_minimum_threshold}ms")
        return
    
    db.insert({LOCATION: location.lower(),
               TRACK_FILE: sound_file})
    return True #signal that it was successful

def add_keyword(word : str, sound_name : str):
    # Checks if tables exist
    if not (file_exists(sound_table) and file_exists(keyword_table)): return
    
    # Validation
    if not presence(word): return
    if not sound_exists(sound_name): return
    if not format_check(word): return
    if not length_check(word, 15): return

    keyword_db = TinyDB(keyword_table)
    word_row = keyword_db.search(Query().word == word.lower())
    if word_row:#exists 
        word_row = word_row[0]
        print(f"The keyword {word_row[KEYWORD]} already exists under the sound {word_row[SOUND_ID]}")
        return

    keyword_db.insert({KEYWORD: word.lower(),
                       SOUND_ID: sound_name.lower()
                       })

def add_keywords(words : list, sound_name : str):
    if not (file_exists(sound_table) and file_exists(keyword_table)): return
    sound_db = TinyDB(sound_table)
    if not sound_db.contains(Query().name == sound_name.lower()):
        print(f"Sound under name: {sound_name}, doesn't exist")
        return
    
    for word in words:
        add_keyword(word, sound_name)
    return True #signal that it was successful

def delete_sound(name : str):
    if not (file_exists(sound_table) and file_exists(keyword_table)): return

    TinyDB(keyword_table).remove(Query().sound_name == name.lower())
    TinyDB(sound_table).remove(Query().name == name.lower())
    return True #signal that it was successful

def delete_keyword(word : str):
    if not file_exists(keyword_table): return

    TinyDB(keyword_table).remove(Query().word == word.lower())
    return True #signal that it was successful

def delete_location(location : str):
    if not file_exists(location_table): return

    TinyDB(location_table).remove(Query().location == location.lower())
    return True #signal that it was successful

#Querying
def get_file_from_location(location : str):
    if not file_exists(location_table): return

    db = TinyDB(location_table)
    result = db.search(Query().location == location.lower())
    
    return result[0][TRACK_FILE] if result else None

def get_file_from_soundID(ID : str):
    if not file_exists(sound_table): return

    db = TinyDB(sound_table)
    result = db.search(Query().name == ID.lower())
    
    return result[0][SOUND_FILE] if result else None

#Generating Data Structures
def convert_sound_name_array_to_files(sound_names : list) -> list:
    if not file_exists(sound_table): return

    db = TinyDB(sound_table)
    items = db.search(Query().name.one_of(sound_names))
    return [i[SOUND_FILE] for i in items]

def keywords_to_ID_dict() -> dict:
    if not file_exists(keyword_table): return
    return {k[KEYWORD] : k[SOUND_ID] for k in TinyDB(keyword_table).all()}

def sounds_to_keywords_dict() -> dict:
    if not file_exists(keyword_table): return
    
    db = TinyDB(keyword_table)
    sounds = sounds_list()
    dict = {sound : [] for sound in sounds}
    for s in sounds:
        keywords_under_s = db.search(Query().sound_name == s)
        dict[s] = [record[KEYWORD] for record in keywords_under_s]
    return dict

def locations_list() -> list[str]:
    if not file_exists(location_table): return
    records = TinyDB(location_table).all()
    return [r[LOCATION] for r in records]

def sounds_list() -> list[str]:
    if not file_exists(sound_table): return
    records = TinyDB(sound_table).all()
    return [r[SOUND_NAME] for r in records]


if __name__ == "__main__":
    print(bool('hello'))

    

    

    