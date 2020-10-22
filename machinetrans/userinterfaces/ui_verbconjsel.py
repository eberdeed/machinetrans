# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/verbconjsel.ui'
#
# Created: Thu Jan 25 11:35:26 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VerbConjSel(object):
    def setupUi(self, VerbConjSel):
        VerbConjSel.setObjectName("VerbConjSel")
        VerbConjSel.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        VerbConjSel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VerbConjSel.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(VerbConjSel)
        self.titleLbl.setGeometry(QtCore.QRect(10, 30, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(VerbConjSel)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(VerbConjSel)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.conjList = QtWidgets.QListWidget(VerbConjSel)
        self.conjList.setGeometry(QtCore.QRect(10, 70, 780, 450))
        self.conjList.setObjectName("conjList")
        self.helpBttn = QtWidgets.QPushButton(VerbConjSel)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(VerbConjSel)
        QtCore.QMetaObject.connectSlotsByName(VerbConjSel)
        VerbConjSel.setTabOrder(self.helpBttn, self.conjList)
        VerbConjSel.setTabOrder(self.conjList, self.cancelBttn)
        VerbConjSel.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, VerbConjSel):
        _translate = QtCore.QCoreApplication.translate
        VerbConjSel.setWindowTitle(_translate("VerbConjSel", "Verb Conjugation Selector"))
        self.titleLbl.setText(_translate("VerbConjSel", "Russian Verb Conjugation List"))
        self.cancelBttn.setText(_translate("VerbConjSel", "Cancel"))
        self.acceptBttn.setText(_translate("VerbConjSel", "Accept"))
        self.helpBttn.setText(_translate("VerbConjSel", "Help"))

