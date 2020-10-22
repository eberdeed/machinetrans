# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/worddatagen.ui'
#
# Created: Thu Jan 25 11:35:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WordDataGen(object):
    def setupUi(self, WordDataGen):
        WordDataGen.setObjectName("WordDataGen")
        WordDataGen.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(17)
        WordDataGen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WordDataGen.setWindowIcon(icon)
        self.acceptBttn = QtWidgets.QPushButton(WordDataGen)
        self.acceptBttn.setGeometry(QtCore.QRect(520, 520, 130, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.titleLbl = QtWidgets.QLabel(WordDataGen)
        self.titleLbl.setGeometry(QtCore.QRect(20, 10, 761, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.quitBttn = QtWidgets.QPushButton(WordDataGen)
        self.quitBttn.setGeometry(QtCore.QRect(150, 520, 130, 50))
        self.quitBttn.setObjectName("quitBttn")
        self.listDisplay = QtWidgets.QListWidget(WordDataGen)
        self.listDisplay.setGeometry(QtCore.QRect(10, 60, 780, 441))
        self.listDisplay.setObjectName("listDisplay")
        self.backBttn = QtWidgets.QPushButton(WordDataGen)
        self.backBttn.setGeometry(QtCore.QRect(340, 520, 130, 50))
        self.backBttn.setObjectName("backBttn")
        self.helpBttn = QtWidgets.QPushButton(WordDataGen)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(WordDataGen)
        QtCore.QMetaObject.connectSlotsByName(WordDataGen)
        WordDataGen.setTabOrder(self.helpBttn, self.listDisplay)
        WordDataGen.setTabOrder(self.listDisplay, self.quitBttn)
        WordDataGen.setTabOrder(self.quitBttn, self.backBttn)
        WordDataGen.setTabOrder(self.backBttn, self.acceptBttn)

    def retranslateUi(self, WordDataGen):
        _translate = QtCore.QCoreApplication.translate
        WordDataGen.setWindowTitle(_translate("WordDataGen", "Sentence Generation"))
        self.acceptBttn.setText(_translate("WordDataGen", "Accept"))
        self.titleLbl.setText(_translate("WordDataGen", "Random Sentence Generation"))
        self.quitBttn.setText(_translate("WordDataGen", "Quit"))
        self.backBttn.setText(_translate("WordDataGen", "Back"))
        self.helpBttn.setText(_translate("WordDataGen", "Help"))

