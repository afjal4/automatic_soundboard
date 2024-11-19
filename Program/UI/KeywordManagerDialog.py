# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KeywordInputDialogWfKGTB.ui'
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
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(652, 293)
        Dialog.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keywords_input = QLineEdit(self.groupBox)
        self.keywords_input.setObjectName(u"keywords_input")
        self.keywords_input.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.keywords_input)

        self.clear_button = QToolButton(self.groupBox)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout_2.addWidget(self.clear_button)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.SoundSelectionBox = QGroupBox(Dialog)
        self.SoundSelectionBox.setObjectName(u"SoundSelectionBox")
        self.horizontalLayout = QHBoxLayout(self.SoundSelectionBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SoundsList = QListView(self.SoundSelectionBox)
        self.SoundsList.setObjectName(u"SoundsList")
        self.SoundsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.SoundsList.setAlternatingRowColors(True)

        self.horizontalLayout.addWidget(self.SoundsList)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.KwListLabel = QLabel(self.SoundSelectionBox)
        self.KwListLabel.setObjectName(u"KwListLabel")

        self.horizontalLayout_4.addWidget(self.KwListLabel)

        self.preview_button = QToolButton(self.SoundSelectionBox)
        self.preview_button.setObjectName(u"preview_button")

        self.horizontalLayout_4.addWidget(self.preview_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.CorrespondingKeywordsList = QListView(self.SoundSelectionBox)
        self.CorrespondingKeywordsList.setObjectName(u"CorrespondingKeywordsList")
        self.CorrespondingKeywordsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CorrespondingKeywordsList.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.CorrespondingKeywordsList)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.SoundSelectionBox)

        self.Selection_Errors_Bar = QGroupBox(Dialog)
        self.Selection_Errors_Bar.setObjectName(u"Selection_Errors_Bar")
        self.horizontalLayout_3 = QHBoxLayout(self.Selection_Errors_Bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.submit_button = QPushButton(self.Selection_Errors_Bar)
        self.submit_button.setObjectName(u"submit_button")

        self.horizontalLayout_3.addWidget(self.submit_button)

        self.errors = QLabel(self.Selection_Errors_Bar)
        self.errors.setObjectName(u"errors")

        self.horizontalLayout_3.addWidget(self.errors)

        self.delete_kw_button = QPushButton(self.Selection_Errors_Bar)
        self.delete_kw_button.setObjectName(u"delete_kw_button")

        self.horizontalLayout_3.addWidget(self.delete_kw_button)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.Selection_Errors_Bar)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Keyword Input", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Enter Keyword/s", None))
        self.keywords_input.setText("")
        self.keywords_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Separate entries using commas ( , )", None))
        self.clear_button.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.SoundSelectionBox.setTitle(QCoreApplication.translate("Dialog", u"Choose Corresponding Sound", None))
        self.KwListLabel.setText(QCoreApplication.translate("Dialog", u"Keywords Under Sound:", None))
        self.preview_button.setText(QCoreApplication.translate("Dialog", u"Play Preview", None))
        self.Selection_Errors_Bar.setTitle("")
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.errors.setText(QCoreApplication.translate("Dialog", u"Errors: None", None))
        self.delete_kw_button.setText(QCoreApplication.translate("Dialog", u"Delete Keyword", None))
    # retranslateUi

