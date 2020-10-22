# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/errordisplay.ui'
#
# Created: Thu Jan 25 11:35:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorDisplay(object):
    def setupUi(self, ErrorDisplay):
        ErrorDisplay.setObjectName("ErrorDisplay")
        ErrorDisplay.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        ErrorDisplay.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ErrorDisplay.setWindowIcon(icon)
        self.errorEdit = QtWidgets.QTextEdit(ErrorDisplay)
        self.errorEdit.setGeometry(QtCore.QRect(10, 60, 780, 460))
        self.errorEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.errorEdit.setObjectName("errorEdit")
        self.titleLbl = QtWidgets.QLabel(ErrorDisplay)
        self.titleLbl.setGeometry(QtCore.QRect(70, 20, 571, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.acceptBttn = QtWidgets.QPushButton(ErrorDisplay)
        self.acceptBttn.setGeometry(QtCore.QRect(300, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(ErrorDisplay)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(ErrorDisplay)
        QtCore.QMetaObject.connectSlotsByName(ErrorDisplay)
        ErrorDisplay.setTabOrder(self.helpBttn, self.errorEdit)
        ErrorDisplay.setTabOrder(self.errorEdit, self.acceptBttn)

    def retranslateUi(self, ErrorDisplay):
        _translate = QtCore.QCoreApplication.translate
        ErrorDisplay.setWindowTitle(_translate("ErrorDisplay", "Error Display"))
        self.titleLbl.setText(_translate("ErrorDisplay", "Machine Translation Error"))
        self.acceptBttn.setText(_translate("ErrorDisplay", "Continue"))
        self.helpBttn.setText(_translate("ErrorDisplay", "Help"))

