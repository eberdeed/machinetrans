# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/sqldata.ui'
#
# Created: Thu Jan 25 11:35:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLData(object):
    def setupUi(self, SQLData):
        SQLData.setObjectName("SQLData")
        SQLData.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        SQLData.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SQLData.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(SQLData)
        self.titleLbl.setGeometry(QtCore.QRect(10, 20, 780, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.quitBttn = QtWidgets.QPushButton(SQLData)
        self.quitBttn.setGeometry(QtCore.QRect(640, 520, 150, 50))
        self.quitBttn.setObjectName("quitBttn")
        self.findBttn = QtWidgets.QPushButton(SQLData)
        self.findBttn.setGeometry(QtCore.QRect(490, 520, 150, 50))
        self.findBttn.setObjectName("findBttn")
        self.listDisplay = QtWidgets.QListWidget(SQLData)
        self.listDisplay.setGeometry(QtCore.QRect(10, 70, 780, 440))
        self.listDisplay.setObjectName("listDisplay")
        self.delBttn = QtWidgets.QPushButton(SQLData)
        self.delBttn.setGeometry(QtCore.QRect(160, 520, 150, 50))
        self.delBttn.setObjectName("delBttn")
        self.editBttn = QtWidgets.QPushButton(SQLData)
        self.editBttn.setGeometry(QtCore.QRect(10, 520, 150, 50))
        self.editBttn.setObjectName("editBttn")
        self.helpBttn = QtWidgets.QPushButton(SQLData)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")
        self.sortBttn = QtWidgets.QPushButton(SQLData)
        self.sortBttn.setGeometry(QtCore.QRect(330, 520, 150, 50))
        self.sortBttn.setObjectName("sortBttn")

        self.retranslateUi(SQLData)
        QtCore.QMetaObject.connectSlotsByName(SQLData)
        SQLData.setTabOrder(self.helpBttn, self.listDisplay)
        SQLData.setTabOrder(self.listDisplay, self.editBttn)
        SQLData.setTabOrder(self.editBttn, self.delBttn)
        SQLData.setTabOrder(self.delBttn, self.findBttn)
        SQLData.setTabOrder(self.findBttn, self.quitBttn)

    def retranslateUi(self, SQLData):
        _translate = QtCore.QCoreApplication.translate
        SQLData.setWindowTitle(_translate("SQLData", "Data Display"))
        self.titleLbl.setText(_translate("SQLData", "Machine Translation Data Display"))
        self.quitBttn.setText(_translate("SQLData", "Back"))
        self.findBttn.setText(_translate("SQLData", "Find"))
        self.delBttn.setText(_translate("SQLData", "Delete"))
        self.editBttn.setText(_translate("SQLData", "Edit"))
        self.helpBttn.setText(_translate("SQLData", "Help"))
        self.sortBttn.setText(_translate("SQLData", "Sort"))

