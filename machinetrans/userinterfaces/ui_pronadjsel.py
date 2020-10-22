# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/pronadjsel.ui'
#
# Created: Thu Jan 25 11:35:28 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PronAdjSel(object):
    def setupUi(self, PronAdjSel):
        PronAdjSel.setObjectName("PronAdjSel")
        PronAdjSel.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        PronAdjSel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PronAdjSel.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(PronAdjSel)
        self.titleLbl.setGeometry(QtCore.QRect(10, 30, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(PronAdjSel)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(PronAdjSel)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(PronAdjSel)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")
        self.declType = QtWidgets.QComboBox(PronAdjSel)
        self.declType.setGeometry(QtCore.QRect(240, 90, 330, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.declType.setFont(font)
        self.declType.setObjectName("declType")
        self.declList = QtWidgets.QTextBrowser(PronAdjSel)
        self.declList.setGeometry(QtCore.QRect(90, 160, 600, 300))
        self.declList.setObjectName("declList")

        self.retranslateUi(PronAdjSel)
        QtCore.QMetaObject.connectSlotsByName(PronAdjSel)
        PronAdjSel.setTabOrder(self.helpBttn, self.declType)
        PronAdjSel.setTabOrder(self.declType, self.cancelBttn)
        PronAdjSel.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, PronAdjSel):
        _translate = QtCore.QCoreApplication.translate
        PronAdjSel.setWindowTitle(_translate("PronAdjSel", "Pronoun Endings Selector"))
        self.titleLbl.setText(_translate("PronAdjSel", "Russian Pronoun Endings Selector"))
        self.cancelBttn.setText(_translate("PronAdjSel", "Cancel"))
        self.acceptBttn.setText(_translate("PronAdjSel", "Accept"))
        self.helpBttn.setText(_translate("PronAdjSel", "Help"))

