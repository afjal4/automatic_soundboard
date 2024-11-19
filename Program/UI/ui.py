# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIaqfIVv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDial,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Application(object):
    def setupUi(self, Application):
        if not Application.objectName():
            Application.setObjectName(u"Application")
        Application.resize(832, 531)
        icon = QIcon()
        icon.addFile(u":/icons/playing_lm.png", QSize(), QIcon.Normal, QIcon.Off)
        Application.setWindowIcon(icon)
        self.actionAdd_Sound = QAction(Application)
        self.actionAdd_Sound.setObjectName(u"actionAdd_Sound")
        font = QFont()
        self.actionAdd_Sound.setFont(font)
        self.actionRemove_Sound = QAction(Application)
        self.actionRemove_Sound.setObjectName(u"actionRemove_Sound")
        self.actionAdd_Keywords = QAction(Application)
        self.actionAdd_Keywords.setObjectName(u"actionAdd_Keywords")
        self.actionRemove_Keywords = QAction(Application)
        self.actionRemove_Keywords.setObjectName(u"actionRemove_Keywords")
        self.actionView_Keywords = QAction(Application)
        self.actionView_Keywords.setObjectName(u"actionView_Keywords")
        self.actionView_Sounds = QAction(Application)
        self.actionView_Sounds.setObjectName(u"actionView_Sounds")
        self.actionDark_Mode = QAction(Application)
        self.actionDark_Mode.setObjectName(u"actionDark_Mode")
        self.actionOpen_Manager_S = QAction(Application)
        self.actionOpen_Manager_S.setObjectName(u"actionOpen_Manager_S")
        self.actionOpen_Manager_K = QAction(Application)
        self.actionOpen_Manager_K.setObjectName(u"actionOpen_Manager_K")
        self.centralwidget = QWidget(Application)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Structure = QVBoxLayout()
        self.Structure.setObjectName(u"Structure")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Notes_Toggle = QVBoxLayout()
        self.Notes_Toggle.setObjectName(u"Notes_Toggle")
        self.Utility = QTabWidget(self.centralwidget)
        self.Utility.setObjectName(u"Utility")
        self.Utility.setMovable(True)
        self.Notes = QWidget()
        self.Notes.setObjectName(u"Notes")
        self.horizontalLayout_4 = QHBoxLayout(self.Notes)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.note = QTextEdit(self.Notes)
        self.note.setObjectName(u"note")

        self.horizontalLayout_4.addWidget(self.note)

        self.Utility.addTab(self.Notes, "")
        self.Dice = QWidget()
        self.Dice.setObjectName(u"Dice")
        self.horizontalLayout_5 = QHBoxLayout(self.Dice)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.d6 = QPushButton(self.Dice)
        self.DiceButtons = QButtonGroup(Application)
        self.DiceButtons.setObjectName(u"DiceButtons")
        self.DiceButtons.addButton(self.d6)
        self.d6.setObjectName(u"d6")
        self.d6.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d6, 0, 1, 1, 1)

        self.d20 = QPushButton(self.Dice)
        self.DiceButtons.addButton(self.d20)
        self.d20.setObjectName(u"d20")
        self.d20.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d20, 2, 1, 1, 1)

        self.d12 = QPushButton(self.Dice)
        self.DiceButtons.addButton(self.d12)
        self.d12.setObjectName(u"d12")
        self.d12.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d12, 2, 0, 1, 1)

        self.d4 = QPushButton(self.Dice)
        self.DiceButtons.addButton(self.d4)
        self.d4.setObjectName(u"d4")
        self.d4.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d4, 0, 0, 1, 1)

        self.d8 = QPushButton(self.Dice)
        self.DiceButtons.addButton(self.d8)
        self.d8.setObjectName(u"d8")
        self.d8.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d8, 1, 0, 1, 1)

        self.d10 = QPushButton(self.Dice)
        self.DiceButtons.addButton(self.d10)
        self.d10.setObjectName(u"d10")
        self.d10.setMinimumSize(QSize(0, 35))

        self.gridLayout_4.addWidget(self.d10, 1, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_4)

        self.lcdNumber = QLCDNumber(self.Dice)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_5.addWidget(self.lcdNumber)

        self.Utility.addTab(self.Dice, "")
        self.Edit = QWidget()
        self.Edit.setObjectName(u"Edit")
        self.verticalLayout_3 = QVBoxLayout(self.Edit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.soundboard_option = QRadioButton(self.Edit)
        self.EditChoices = QButtonGroup(Application)
        self.EditChoices.setObjectName(u"EditChoices")
        self.EditChoices.setExclusive(True)
        self.EditChoices.addButton(self.soundboard_option)
        self.soundboard_option.setObjectName(u"soundboard_option")
        self.soundboard_option.setChecked(True)

        self.horizontalLayout_6.addWidget(self.soundboard_option)

        self.location_option = QRadioButton(self.Edit)
        self.EditChoices.addButton(self.location_option)
        self.location_option.setObjectName(u"location_option")

        self.horizontalLayout_6.addWidget(self.location_option)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.comboBox = QComboBox(self.Edit)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.label_5 = QLabel(self.Edit)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.save_sb_button = QPushButton(self.Edit)
        self.save_sb_button.setObjectName(u"save_sb_button")

        self.verticalLayout_2.addWidget(self.save_sb_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.Utility.addTab(self.Edit, "")

        self.Notes_Toggle.addWidget(self.Utility)

        self.aut_soundboard_toggle = QRadioButton(self.centralwidget)
        self.aut_soundboard_toggle.setObjectName(u"aut_soundboard_toggle")
        self.aut_soundboard_toggle.setAutoFillBackground(False)
        self.aut_soundboard_toggle.setIconSize(QSize(20, 20))
        self.aut_soundboard_toggle.setChecked(False)

        self.Notes_Toggle.addWidget(self.aut_soundboard_toggle)


        self.horizontalLayout_7.addLayout(self.Notes_Toggle)

        self.Sliders = QGroupBox(self.centralwidget)
        self.Sliders.setObjectName(u"Sliders")
        self.gridLayout = QGridLayout(self.Sliders)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MasterVol = QHBoxLayout()
        self.MasterVol.setObjectName(u"MasterVol")
        self.mute_toggle = QToolButton(self.Sliders)
        self.mute_toggle.setObjectName(u"mute_toggle")
        self.mute_toggle.setIcon(icon)
        self.mute_toggle.setCheckable(True)

        self.MasterVol.addWidget(self.mute_toggle)

        self.vol_slider = QSlider(self.Sliders)
        self.vol_slider.setObjectName(u"vol_slider")
        self.vol_slider.setValue(99)
        self.vol_slider.setOrientation(Qt.Horizontal)

        self.MasterVol.addWidget(self.vol_slider)


        self.gridLayout.addLayout(self.MasterVol, 0, 0, 1, 1)

        self.Dials = QGridLayout()
        self.Dials.setObjectName(u"Dials")
        self.soundboard_dial = QDial(self.Sliders)
        self.soundboard_dial.setObjectName(u"soundboard_dial")
        self.soundboard_dial.setEnabled(True)
        self.soundboard_dial.setMinimumSize(QSize(70, 70))
        self.soundboard_dial.setAutoFillBackground(True)
        self.soundboard_dial.setMaximum(99)
        self.soundboard_dial.setValue(50)
        self.soundboard_dial.setInvertedAppearance(False)
        self.soundboard_dial.setInvertedControls(False)
        self.soundboard_dial.setWrapping(False)
        self.soundboard_dial.setNotchesVisible(True)
        self.soundboard_dial.setNotchTarget(2)

        self.Dials.addWidget(self.soundboard_dial, 0, 1, 1, 1)

        self.label_2 = QLabel(self.Sliders)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.Dials.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.Sliders)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.Dials.addWidget(self.label_3, 1, 2, 1, 1)

        self.label = QLabel(self.Sliders)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.Dials.addWidget(self.label, 1, 0, 1, 1)

        self.auto_sounds_dial = QDial(self.Sliders)
        self.auto_sounds_dial.setObjectName(u"auto_sounds_dial")
        self.auto_sounds_dial.setEnabled(True)
        self.auto_sounds_dial.setMinimumSize(QSize(70, 70))
        self.auto_sounds_dial.setAutoFillBackground(True)
        self.auto_sounds_dial.setMaximum(99)
        self.auto_sounds_dial.setValue(50)
        self.auto_sounds_dial.setNotchesVisible(True)
        self.auto_sounds_dial.setNotchTarget(2)

        self.Dials.addWidget(self.auto_sounds_dial, 0, 2, 1, 1)

        self.music_dial = QDial(self.Sliders)
        self.music_dial.setObjectName(u"music_dial")
        self.music_dial.setMinimumSize(QSize(70, 70))
        self.music_dial.setAutoFillBackground(True)
        self.music_dial.setMaximum(99)
        self.music_dial.setValue(50)
        self.music_dial.setOrientation(Qt.Horizontal)
        self.music_dial.setNotchesVisible(True)
        self.music_dial.setNotchTarget(2)

        self.Dials.addWidget(self.music_dial, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.Dials, 1, 0, 1, 1)

        self.auto_sound_outp = QLabel(self.Sliders)
        self.auto_sound_outp.setObjectName(u"auto_sound_outp")

        self.gridLayout.addWidget(self.auto_sound_outp, 2, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.Sliders)


        self.Structure.addLayout(self.horizontalLayout_7)

        self.SoundboardStruct = QGroupBox(self.centralwidget)
        self.SoundboardStruct.setObjectName(u"SoundboardStruct")
        self.horizontalLayout_3 = QHBoxLayout(self.SoundboardStruct)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Soundboard = QGridLayout()
        self.Soundboard.setObjectName(u"Soundboard")
        self.lower_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Soundboard.addItem(self.lower_spacer, 3, 0, 1, 1)

        self.Slot_2 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons = QButtonGroup(Application)
        self.SoundboardButtons.setObjectName(u"SoundboardButtons")
        self.SoundboardButtons.addButton(self.Slot_2)
        self.Slot_2.setObjectName(u"Slot_2")
        self.Slot_2.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_2, 1, 1, 1, 1)

        self.Slot_5 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_5)
        self.Slot_5.setObjectName(u"Slot_5")
        self.Slot_5.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        iconThemeName = u"accessories-dictionary"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.Slot_5.setIcon(icon1)

        self.Soundboard.addWidget(self.Slot_5, 1, 4, 1, 1)

        self.Slot_4 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_4)
        self.Slot_4.setObjectName(u"Slot_4")
        self.Slot_4.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_4, 1, 3, 1, 1)

        self.Slot_3 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_3)
        self.Slot_3.setObjectName(u"Slot_3")
        self.Slot_3.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_3, 1, 2, 1, 1)

        self.upper_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Soundboard.addItem(self.upper_spacer, 0, 0, 1, 1)

        self.Slot_1 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_1)
        self.Slot_1.setObjectName(u"Slot_1")
        self.Slot_1.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_1, 1, 0, 1, 1)

        self.Slot_6 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_6)
        self.Slot_6.setObjectName(u"Slot_6")
        self.Slot_6.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_6, 1, 5, 1, 1)

        self.Slot_7 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_7)
        self.Slot_7.setObjectName(u"Slot_7")
        self.Slot_7.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_7, 2, 0, 1, 1)

        self.Slot_8 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_8)
        self.Slot_8.setObjectName(u"Slot_8")
        self.Slot_8.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_8, 2, 1, 1, 1)

        self.Slot_9 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_9)
        self.Slot_9.setObjectName(u"Slot_9")
        self.Slot_9.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_9, 2, 2, 1, 1)

        self.Slot_10 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_10)
        self.Slot_10.setObjectName(u"Slot_10")
        self.Slot_10.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_10, 2, 3, 1, 1)

        self.Slot_11 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_11)
        self.Slot_11.setObjectName(u"Slot_11")
        self.Slot_11.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_11, 2, 4, 1, 1)

        self.Slot_12 = QPushButton(self.SoundboardStruct)
        self.SoundboardButtons.addButton(self.Slot_12)
        self.Slot_12.setObjectName(u"Slot_12")
        self.Slot_12.setMinimumSize(QSize(0, 50))

        self.Soundboard.addWidget(self.Slot_12, 2, 5, 1, 1)


        self.verticalLayout.addLayout(self.Soundboard)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.Structure.addWidget(self.SoundboardStruct)

        self.LocationsStruct = QGroupBox(self.centralwidget)
        self.LocationsStruct.setObjectName(u"LocationsStruct")
        self.LocationsStruct.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.LocationsStruct)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Locations = QHBoxLayout()
        self.Locations.setObjectName(u"Locations")
        self.empty = QToolButton(self.LocationsStruct)
        self.LocationButtons = QButtonGroup(Application)
        self.LocationButtons.setObjectName(u"LocationButtons")
        self.LocationButtons.addButton(self.empty)
        self.empty.setObjectName(u"empty")
        self.empty.setCheckable(True)
        self.empty.setChecked(True)

        self.Locations.addWidget(self.empty)

        self.Location_A = QPushButton(self.LocationsStruct)
        self.LocationButtons.addButton(self.Location_A)
        self.Location_A.setObjectName(u"Location_A")
        self.Location_A.setMinimumSize(QSize(0, 30))
        self.Location_A.setCheckable(True)
        self.Location_A.setAutoExclusive(True)

        self.Locations.addWidget(self.Location_A)

        self.Location_B = QPushButton(self.LocationsStruct)
        self.LocationButtons.addButton(self.Location_B)
        self.Location_B.setObjectName(u"Location_B")
        self.Location_B.setMinimumSize(QSize(0, 30))
        self.Location_B.setCheckable(True)
        self.Location_B.setAutoExclusive(True)

        self.Locations.addWidget(self.Location_B)

        self.Location_C = QPushButton(self.LocationsStruct)
        self.LocationButtons.addButton(self.Location_C)
        self.Location_C.setObjectName(u"Location_C")
        self.Location_C.setMinimumSize(QSize(0, 30))
        self.Location_C.setCheckable(True)

        self.Locations.addWidget(self.Location_C)

        self.Location_D = QPushButton(self.LocationsStruct)
        self.LocationButtons.addButton(self.Location_D)
        self.Location_D.setObjectName(u"Location_D")
        self.Location_D.setMinimumSize(QSize(0, 30))
        self.Location_D.setCheckable(True)

        self.Locations.addWidget(self.Location_D)

        self.Location_E = QPushButton(self.LocationsStruct)
        self.LocationButtons.addButton(self.Location_E)
        self.Location_E.setObjectName(u"Location_E")
        self.Location_E.setMinimumSize(QSize(0, 30))
        self.Location_E.setCheckable(True)
        self.Location_E.setChecked(False)

        self.Locations.addWidget(self.Location_E)


        self.horizontalLayout_2.addLayout(self.Locations)


        self.Structure.addWidget(self.LocationsStruct)

        self.Structure.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.Structure)

        Application.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Application)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 832, 26))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.menuBar.setFont(font1)
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuAdd_Sound = QMenu(self.menuBar)
        self.menuAdd_Sound.setObjectName(u"menuAdd_Sound")
        self.menuAdd_Keyword = QMenu(self.menuBar)
        self.menuAdd_Keyword.setObjectName(u"menuAdd_Keyword")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.menuAdd_Keyword.setFont(font2)
        self.menuAdd_Keyword.setCursor(QCursor(Qt.ArrowCursor))
        Application.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAdd_Sound.menuAction())
        self.menuBar.addAction(self.menuAdd_Keyword.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionDark_Mode)
        self.menuAdd_Sound.addAction(self.actionOpen_Manager_S)
        self.menuAdd_Keyword.addAction(self.actionOpen_Manager_K)

        self.retranslateUi(Application)

        self.Utility.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"Automatic Soundboard", None))
        self.actionAdd_Sound.setText(QCoreApplication.translate("Application", u"Add Sound", None))
        self.actionRemove_Sound.setText(QCoreApplication.translate("Application", u"Remove Sound", None))
        self.actionAdd_Keywords.setText(QCoreApplication.translate("Application", u"Add Keywords", None))
        self.actionRemove_Keywords.setText(QCoreApplication.translate("Application", u"Remove Keywords", None))
        self.actionView_Keywords.setText(QCoreApplication.translate("Application", u"View Keywords", None))
        self.actionView_Sounds.setText(QCoreApplication.translate("Application", u"View Sounds", None))
        self.actionDark_Mode.setText(QCoreApplication.translate("Application", u"Toggle Dark Mode", None))
        self.actionOpen_Manager_S.setText(QCoreApplication.translate("Application", u"Open Manager", None))
        self.actionOpen_Manager_K.setText(QCoreApplication.translate("Application", u"Open Manager", None))
        self.Utility.setTabText(self.Utility.indexOf(self.Notes), QCoreApplication.translate("Application", u"Notes", None))
#if QT_CONFIG(tooltip)
        self.Utility.setTabToolTip(self.Utility.indexOf(self.Notes), QCoreApplication.translate("Application", u"Notepad", None))
#endif // QT_CONFIG(tooltip)
        self.d6.setText(QCoreApplication.translate("Application", u"6", None))
        self.d20.setText(QCoreApplication.translate("Application", u"20", None))
        self.d12.setText(QCoreApplication.translate("Application", u"12", None))
        self.d4.setText(QCoreApplication.translate("Application", u"4", None))
        self.d8.setText(QCoreApplication.translate("Application", u"8", None))
        self.d10.setText(QCoreApplication.translate("Application", u"10", None))
        self.Utility.setTabText(self.Utility.indexOf(self.Dice), QCoreApplication.translate("Application", u"Dice", None))
#if QT_CONFIG(tooltip)
        self.Utility.setTabToolTip(self.Utility.indexOf(self.Dice), QCoreApplication.translate("Application", u"Roll n-sided Dice", None))
#endif // QT_CONFIG(tooltip)
        self.soundboard_option.setText(QCoreApplication.translate("Application", u"Sound Effects", None))
        self.location_option.setText(QCoreApplication.translate("Application", u"Locations", None))
        self.comboBox.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Application", u"Soundboards are currently Disabled\n"
"Choose a sound from box above\n"
"You can add new sounds in the Sound Manager\n"
"Click one of the buttons below to link\n"
"Leave this tab to resume", None))
        self.save_sb_button.setText(QCoreApplication.translate("Application", u"Save Soundboards", None))
        self.Utility.setTabText(self.Utility.indexOf(self.Edit), QCoreApplication.translate("Application", u"Edit Soundboards", None))
        self.aut_soundboard_toggle.setText(QCoreApplication.translate("Application", u"Enable Auto Soundboard", None))
        self.Sliders.setTitle(QCoreApplication.translate("Application", u"Volume", None))
        self.mute_toggle.setText(QCoreApplication.translate("Application", u"Mute", None))
        self.label_2.setText(QCoreApplication.translate("Application", u"Soundboard", None))
        self.label_3.setText(QCoreApplication.translate("Application", u"Auto-Sounds", None))
        self.label.setText(QCoreApplication.translate("Application", u"Music", None))
        self.auto_sound_outp.setText("")
        self.SoundboardStruct.setTitle(QCoreApplication.translate("Application", u"Sound Effects", None))
        self.Slot_2.setText(QCoreApplication.translate("Application", u"Slot 2", None))
        self.Slot_5.setText(QCoreApplication.translate("Application", u"Slot 5", None))
        self.Slot_4.setText(QCoreApplication.translate("Application", u"Slot 4", None))
        self.Slot_3.setText(QCoreApplication.translate("Application", u"Slot 3", None))
        self.Slot_1.setText(QCoreApplication.translate("Application", u"Slot 1", None))
        self.Slot_6.setText(QCoreApplication.translate("Application", u"Slot 6", None))
        self.Slot_7.setText(QCoreApplication.translate("Application", u"Slot 7", None))
        self.Slot_8.setText(QCoreApplication.translate("Application", u"Slot 8", None))
        self.Slot_9.setText(QCoreApplication.translate("Application", u"Slot 9", None))
        self.Slot_10.setText(QCoreApplication.translate("Application", u"Slot 10", None))
        self.Slot_11.setText(QCoreApplication.translate("Application", u"Slot 11", None))
        self.Slot_12.setText(QCoreApplication.translate("Application", u"Slot 12", None))
        self.LocationsStruct.setTitle(QCoreApplication.translate("Application", u"Locations", None))
        self.empty.setText(QCoreApplication.translate("Application", u"X", None))
        self.Location_A.setText(QCoreApplication.translate("Application", u"Location A", None))
        self.Location_B.setText(QCoreApplication.translate("Application", u"Location B", None))
        self.Location_C.setText(QCoreApplication.translate("Application", u"Location C", None))
        self.Location_D.setText(QCoreApplication.translate("Application", u"Location D", None))
        self.Location_E.setText(QCoreApplication.translate("Application", u"Location E", None))
        self.menuSettings.setTitle(QCoreApplication.translate("Application", u"Settings", None))
        self.menuAdd_Sound.setTitle(QCoreApplication.translate("Application", u"Manage Sounds  ", None))
        self.menuAdd_Keyword.setTitle(QCoreApplication.translate("Application", u"Manage Keywords  ", None))
    # retranslateUi

