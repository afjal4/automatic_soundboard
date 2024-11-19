# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AudioManagerDialoglhyXYX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 409)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_box = QGroupBox(Dialog)
        self.top_box.setObjectName(u"top_box")
        self.horizontalLayout_4 = QHBoxLayout(self.top_box)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sound_title_inp = QLineEdit(self.top_box)
        self.sound_title_inp.setObjectName(u"sound_title_inp")

        self.horizontalLayout_4.addWidget(self.sound_title_inp)

        self.mode_change = QPushButton(self.top_box)
        self.mode_change.setObjectName(u"mode_change")
        self.mode_change.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.mode_change)


        self.verticalLayout_2.addWidget(self.top_box)

        self.active_sounds_box = QGroupBox(Dialog)
        self.active_sounds_box.setObjectName(u"active_sounds_box")
        self.verticalLayout_4 = QVBoxLayout(self.active_sounds_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.active_sounds = QListView(self.active_sounds_box)
        self.active_sounds.setObjectName(u"active_sounds")
        self.active_sounds.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.active_sounds.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.active_sounds.setAlternatingRowColors(True)
        self.active_sounds.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_4.addWidget(self.active_sounds)

        self.delete_sound = QPushButton(self.active_sounds_box)
        self.delete_sound.setObjectName(u"delete_sound")
        self.delete_sound.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.delete_sound)


        self.verticalLayout_2.addWidget(self.active_sounds_box)

        self.choose_file_box = QGroupBox(Dialog)
        self.choose_file_box.setObjectName(u"choose_file_box")
        self.horizontalLayout = QHBoxLayout(self.choose_file_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_inp = QLineEdit(self.choose_file_box)
        self.file_inp.setObjectName(u"file_inp")

        self.horizontalLayout.addWidget(self.file_inp)

        self.browse_button = QPushButton(self.choose_file_box)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.browse_button)


        self.verticalLayout_2.addWidget(self.choose_file_box)

        self.bottom = QGroupBox(Dialog)
        self.bottom.setObjectName(u"bottom")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.submit_button = QPushButton(self.bottom)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.submit_button)

        self.error_label = QLabel(self.bottom)
        self.error_label.setObjectName(u"error_label")

        self.horizontalLayout_2.addWidget(self.error_label)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.bottom)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Manage Sounds", None))
        self.top_box.setTitle(QCoreApplication.translate("Dialog", u"Enter Sound Title", None))
        self.mode_change.setText(QCoreApplication.translate("Dialog", u"Change to Location Manager", None))
        self.active_sounds_box.setTitle(QCoreApplication.translate("Dialog", u"Active Sounds", None))
        self.delete_sound.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.choose_file_box.setTitle(QCoreApplication.translate("Dialog", u"Choose Audio File", None))
        self.browse_button.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.bottom.setTitle("")
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.error_label.setText(QCoreApplication.translate("Dialog", u"Errors:", None))
    # retranslateUi

