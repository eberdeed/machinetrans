# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/adjdeclsel.ui'
#
# Created: Thu Jan 25 11:35:26 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdjDeclSel(object):
    def setupUi(self, AdjDeclSel):
        AdjDeclSel.setObjectName("AdjDeclSel")
        AdjDeclSel.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        AdjDeclSel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdjDeclSel.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(AdjDeclSel)
        self.titleLbl.setGeometry(QtCore.QRect(10, 30, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(AdjDeclSel)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(AdjDeclSel)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(AdjDeclSel)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")
        self.declView = QtWidgets.QTextBrowser(AdjDeclSel)
        self.declView.setGeometry(QtCore.QRect(10, 70, 720, 450))
        self.declView.setObjectName("declView")
        self.upList = QtWidgets.QPushButton(AdjDeclSel)
        self.upList.setGeometry(QtCore.QRect(740, 140, 50, 100))
        self.upList.setObjectName("upList")
        self.downList = QtWidgets.QPushButton(AdjDeclSel)
        self.downList.setGeometry(QtCore.QRect(740, 260, 50, 100))
        self.downList.setObjectName("downList")

        self.retranslateUi(AdjDeclSel)
        QtCore.QMetaObject.connectSlotsByName(AdjDeclSel)
        AdjDeclSel.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, AdjDeclSel):
        _translate = QtCore.QCoreApplication.translate
        AdjDeclSel.setWindowTitle(_translate("AdjDeclSel", "Adjective Declension Selector"))
        self.titleLbl.setText(_translate("AdjDeclSel", "Russian Adjective Declension List"))
        self.cancelBttn.setText(_translate("AdjDeclSel", "Cancel"))
        self.acceptBttn.setText(_translate("AdjDeclSel", "Accept"))
        self.helpBttn.setText(_translate("AdjDeclSel", "Help"))
        self.upList.setText(_translate("AdjDeclSel", "^\n"
"^\n"
"^\n"
"^\n"
""))
        self.downList.setText(_translate("AdjDeclSel", "v\n"
"v\n"
"v\n"
"v"))

