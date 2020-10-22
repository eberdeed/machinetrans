# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/editdata.ui'
#
# Created: Thu Jan 25 11:35:28 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditData(object):
    def setupUi(self, EditData):
        EditData.setObjectName("EditData")
        EditData.resize(800, 250)
        font = QtGui.QFont()
        font.setPointSize(16)
        EditData.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditData.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(EditData)
        self.titleLbl.setGeometry(QtCore.QRect(10, 10, 780, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.acceptBttn = QtWidgets.QPushButton(EditData)
        self.acceptBttn.setGeometry(QtCore.QRect(490, 190, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.quitBttn = QtWidgets.QPushButton(EditData)
        self.quitBttn.setGeometry(QtCore.QRect(160, 190, 150, 50))
        self.quitBttn.setObjectName("quitBttn")
        self.textEdit = QtWidgets.QTextEdit(EditData)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 780, 110))
        self.textEdit.setObjectName("textEdit")
        self.helpBttn = QtWidgets.QPushButton(EditData)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(EditData)
        QtCore.QMetaObject.connectSlotsByName(EditData)
        EditData.setTabOrder(self.helpBttn, self.textEdit)
        EditData.setTabOrder(self.textEdit, self.quitBttn)
        EditData.setTabOrder(self.quitBttn, self.acceptBttn)

    def retranslateUi(self, EditData):
        _translate = QtCore.QCoreApplication.translate
        EditData.setWindowTitle(_translate("EditData", "Data Edit"))
        self.titleLbl.setText(_translate("EditData", "Machine Translation Data Editor"))
        self.acceptBttn.setText(_translate("EditData", "Accept"))
        self.quitBttn.setText(_translate("EditData", "Quit"))
        self.helpBttn.setText(_translate("EditData", "Help"))

