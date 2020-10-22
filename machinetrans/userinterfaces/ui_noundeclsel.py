# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/noundeclsel.ui'
#
# Created: Thu Jan 25 11:35:26 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NounDeclSel(object):
    def setupUi(self, NounDeclSel):
        NounDeclSel.setObjectName("NounDeclSel")
        NounDeclSel.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        NounDeclSel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NounDeclSel.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(NounDeclSel)
        self.titleLbl.setGeometry(QtCore.QRect(10, 30, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(NounDeclSel)
        self.cancelBttn.setGeometry(QtCore.QRect(10, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(NounDeclSel)
        self.acceptBttn.setGeometry(QtCore.QRect(630, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(NounDeclSel)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")
        self.genderBox = QtWidgets.QComboBox(NounDeclSel)
        self.genderBox.setGeometry(QtCore.QRect(170, 80, 470, 34))
        self.genderBox.setObjectName("genderBox")
        self.declList = QtWidgets.QListWidget(NounDeclSel)
        self.declList.setGeometry(QtCore.QRect(110, 160, 600, 300))
        self.declList.setObjectName("declList")

        self.retranslateUi(NounDeclSel)
        QtCore.QMetaObject.connectSlotsByName(NounDeclSel)
        NounDeclSel.setTabOrder(self.helpBttn, self.genderBox)
        NounDeclSel.setTabOrder(self.genderBox, self.declList)
        NounDeclSel.setTabOrder(self.declList, self.cancelBttn)
        NounDeclSel.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, NounDeclSel):
        _translate = QtCore.QCoreApplication.translate
        NounDeclSel.setWindowTitle(_translate("NounDeclSel", "Noun Declension Selector"))
        self.titleLbl.setText(_translate("NounDeclSel", "Russian Noun Declension List"))
        self.cancelBttn.setText(_translate("NounDeclSel", "Cancel"))
        self.acceptBttn.setText(_translate("NounDeclSel", "Accept"))
        self.helpBttn.setText(_translate("NounDeclSel", "Help"))

