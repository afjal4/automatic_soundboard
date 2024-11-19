import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
from UI.AudioManagerDialog import Ui_Dialog as AudioManagerUI
from UI.KeywordManagerDialog import Ui_Dialog as KeywordManagerUI
from capture_stdout_decorator import print_capture
import os, sys

import sound_databases as sd

class AudioManagerDialog(qtw.QDialog, AudioManagerUI):
    # Attributes to choose menu mode
    SOUNDS = 0
    LOCATIONS = 1
    __mode = 0 #from above

    # Submission data
    title = ''
    file = ''
    __sound_directory = ''

    # Display data
    sounds = []
    locations = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AudioManagerUI()
        self.ui.setupUi(self)
        self.__setSoundDirectory(self.findSoundsDirectory())

        # List view
        self.model = qtc.QStringListModel(self)
        self.ui.active_sounds.setModel(self.model)
        self.updateActiveSounds()
        
        # Button signals
        self.ui.sound_title_inp.textEdited.connect(self.setTitle)
        self.ui.browse_button.clicked.connect(self.browseSoundFiles)
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.mode_change.clicked.connect(self.toggleMode)
        self.ui.delete_sound.clicked.connect(self.deleteSound)

    def __setToSoundsMode(self):
        self.__setMode(self.SOUNDS)
        self.ui.mode_change.setText(f"Change to Locations Manager")
    def __setToLocationsMode(self):
        self.__setMode(self.LOCATIONS)
        self.ui.mode_change.setText(f"Change to Sounds Manager")

    def __setMode(self, pMode):
        if pMode not in [self.SOUNDS, self.LOCATIONS]: return
        self.__mode = pMode
    def getMode(self):
        return self.__mode

    def __setSoundDirectory(self, pPath):
        self.__sound_directory = pPath
    def getSoundDirectory(self):
        return self.__sound_directory

    def setTitle(self, pTitle):
        self.title = pTitle
    def getTitle(self):
        return self.title

    def setFile(self, pFile):
        self.file = pFile
    def getFile(self):
        return self.file
    
    def browseSoundFiles(self):
        # Instanciating file searcher
        file_dialog = qtw.QFileDialog(self)
        file_dialog.setFileMode(qtw.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Sound files (*.wav *.mp3)")
        file_dialog.setDirectory(self.getSoundDirectory())
        # Executes here, cancels browsing if browser loading fails
        if not file_dialog.exec(): return
        # Output
        selected_files = file_dialog.selectedFiles()
        if not selected_files: return
        # Updates file attribute if a file is found
        self.ui.file_inp.setText(selected_files[0])
        self.setFile(selected_files[0])

    def findSoundsDirectory(self):
        goal = "Sounds"
        sound_path = os.path.join(os.getcwd(), goal)
        if os.path.exists(sound_path): return sound_path
        else: print(f"FileBrowser: Check for folder named 'Sounds' in the top level of {os.getcwd()}, or enter file manually.")

    def updateActiveSounds(self):
        # Uses different list depending on the mode
        if self.getMode() == self.SOUNDS: list = lambda: sd.sounds_list()
        elif self.getMode() == self.LOCATIONS: list = lambda: sd.locations_list()
        self.model.setStringList(list())
    
    def updateElementText(self):
        if self.getMode() == self.SOUNDS: mode_pl = 'Sounds'
        elif self.getMode() == self.LOCATIONS: mode_pl = 'Locations'
        mode_sg = mode_pl[:-1]

        self.ui.top_box.setTitle(f"Enter {mode_sg} Title")
        self.ui.active_sounds_box.setTitle(f"Active {mode_pl}")

    def toggleMode(self):
        if self.getMode() == self.SOUNDS: self.__setToLocationsMode()
        elif self.getMode() == self.LOCATIONS: self.__setToSoundsMode()
        self.updateElementText()
        self.updateActiveSounds()
    
    def deleteSound(self):
        # errors = (None, errors), captured by print_capture decorator
        errors = self.__deleteHoveredSound()[1]
        if errors:
            error_message = f"Errors: {errors[:-2]}"
            # Slicing to remove trailing new line
        else: error_message = "Deletion Successful"
        self.ui.error_label.setText(error_message)

    @print_capture
    def __deleteHoveredSound(self):
        # Accesses UI element to get hovered location
        item = self.ui.active_sounds.currentIndex().data()
        # Uses different deletion function based on mode
        if self.getMode() == self.LOCATIONS: 
            delete = lambda place : sd.delete_location(place)
        elif self.getMode() == self.SOUNDS: 
            delete = lambda sound : sd.delete_sound(sound)
        else: pass
        delete(item)
        self.updateActiveSounds()

    def submit(self):
        # errors = (None, errors), captured by print_capture decorator
        errors = self.__submit_to_DB()[1]
        if errors:
            error_message = f"Errors: {errors[:-2]}"
            # Slicing to remove trailing new line
        else: error_message = "Submission Successful"
        self.ui.error_label.setText(error_message)

    @print_capture
    def __submit_to_DB(self):
        #submits to a different database in different modes
        if self.getMode() == self.SOUNDS: 
            submit = lambda name, file : sd.add_sound(name, file)
        elif self.getMode() == self.LOCATIONS: 
            submit = lambda name, file: sd.add_location_track(name, file)

        if submit(self.getTitle(), self.getFile()):
            self.ui.sound_title_inp.clear()
            self.ui.file_inp.clear()
            self.setFile('')
            self.setTitle('')
        self.updateActiveSounds()

class KeywordManagerDialog(qtw.QDialog, KeywordManagerUI):
    # Words from QLineEdit string separated by commas
    input_words = []

    # Parameters for the ListView
    __sounds = []
    __chosen_sound = ''
    __chosen_keywords = []

    def __init__(self, parent = None):
        super().__init__()
        self.ui = KeywordManagerUI()
        self.ui.setupUi(self)
        self.main_window = parent

        # Update the model attribute to update display
        self.sound_model = qtc.QStringListModel(self)
        self.kw_model = qtc.QStringListModel(self)
        self.ui.SoundsList.setModel(self.sound_model)
        self.ui.CorrespondingKeywordsList.setModel(self.kw_model)
        self.updateSounds()

        self.ui.clear_button.clicked.connect(self.emptyInputText)
        self.ui.SoundsList.pressed.connect(self.updateChosenSound)
        self.ui.preview_button.clicked.connect(self.playPreview)
        self.ui.keywords_input.textEdited.connect(self.updateInputWords)
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.delete_kw_button.clicked.connect(self.deleteCurrentKeyword)
    
    def __setChosenSound(self, pSound):
        self.__chosen_sound = pSound
    def getChosenSound(self):
        return self.__chosen_sound

    def __setInputWords(self, pWords):
        self.input_words = pWords
    def getInputWords(self):
        return self.input_words

    def __setChosenKeywords(self, pWords):
        self.__chosen_keywords = pWords
    def getChosenKeywords(self):
        return self.__chosen_keywords

    def __setSounds(self, pSounds):
        self.__sounds = pSounds
    def getSounds(self):
        return self.__sounds

    def emptyInputText(self):
        self.__setInputWords([])
        self.ui.keywords_input.clear()
        self.ui.errors.setText("Errors: None")

    def updateInputWords(self):
        text = self.ui.keywords_input.text()
        #separates string of comma separated values
        words = [word.strip() for word in text.split(',')]
        self.__setInputWords(words)

    def identifyChosenSound(self):
        chosen_sound = self.ui.SoundsList.currentIndex().data()
        self.__setChosenSound(chosen_sound)
        return chosen_sound

    def updateChosenSound(self, identifyNew = True):
        # Obtaining sound to update
        if identifyNew: chosen_sound = self.identifyChosenSound()
        else: chosen_sound = self.getChosenSound()
        
        if chosen_sound not in self.getSounds(): 
            self.__setChosenKeywords([])
        else:
            sounds_to_keywords = sd.sounds_to_keywords_dict()
            self.__setChosenKeywords(sounds_to_keywords[chosen_sound])
            # Update the label above kw list
            self.ui.KwListLabel.setText(f"Keywords under {self.getChosenSound()}:")
        self.updateListviews()
    
    def updateSounds(self):
        self.__setSounds(sd.sounds_list())
        self.sound_model.setStringList(self.getSounds())

    def updateListviews(self):
        self.sound_model.setStringList(self.getSounds())
        self.kw_model.setStringList(self.getChosenKeywords())

    def deleteCurrentKeyword(self):
        # Identifies the keyword chosen from QListView
        current_keyword = self.ui.CorrespondingKeywordsList.currentIndex().data()
        if current_keyword == None: return
        if sd.delete_keyword(current_keyword):
            self.ui.errors.setText('Deletion Successful')
        self.updateChosenSound(identifyNew=False)

    def playPreview(self):
        sound_to_play = self.getChosenSound()
        self.main_window.playSoundPreviewFromDialog(sound_to_play)

    def submit(self):
        # errors = (None, errors), captured by print_capture decorator
        errors = self.__submit_to_DB()[1]
        if errors:
            error_message = f"Errors: {errors[:-2]}"
            # Slicing to remove trailing new line
        else: error_message = "Submission Successful"
        self.ui.errors.setText(error_message)

    @print_capture
    def __submit_to_DB(self):
        # If no sound is selected, return
        if not self.getChosenSound(): return
        # Validation done at DB
        sd.add_keywords(self.getInputWords(), self.getChosenSound())
        self.updateChosenSound(identifyNew=False)

if __name__ == '__main__':
    # Create the application
    print(sd.sounds_to_keywords_dict())
    app = qtw.QApplication(sys.argv)
    # Create the dialog object
    dialog = KeywordManagerDialog()
    dialog.show()
    # Runs the main loop
    sys.exit(app.exec())