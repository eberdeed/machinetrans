# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/dataentry.ui'
#
# Created: Thu Jan 25 11:35:23 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataEntry(object):
    def setupUi(self, DataEntry):
        DataEntry.setObjectName("DataEntry")
        DataEntry.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(17)
        DataEntry.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataEntry.setWindowIcon(icon)
        self.acceptBttn = QtWidgets.QPushButton(DataEntry)
        self.acceptBttn.setGeometry(QtCore.QRect(660, 520, 130, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.titleLbl = QtWidgets.QLabel(DataEntry)
        self.titleLbl.setGeometry(QtCore.QRect(10, 10, 780, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.quitBttn = QtWidgets.QPushButton(DataEntry)
        self.quitBttn.setGeometry(QtCore.QRect(10, 520, 130, 50))
        self.quitBttn.setObjectName("quitBttn")
        self.sqlBttn = QtWidgets.QPushButton(DataEntry)
        self.sqlBttn.setGeometry(QtCore.QRect(500, 520, 130, 50))
        self.sqlBttn.setObjectName("sqlBttn")
        self.listDisplay = QtWidgets.QListWidget(DataEntry)
        self.listDisplay.setGeometry(QtCore.QRect(100, 120, 600, 300))
        self.listDisplay.setObjectName("listDisplay")
        self.cancelBttn = QtWidgets.QPushButton(DataEntry)
        self.cancelBttn.setGeometry(QtCore.QRect(340, 520, 130, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.dataBttn = QtWidgets.QPushButton(DataEntry)
        self.dataBttn.setGeometry(QtCore.QRect(180, 520, 130, 50))
        self.dataBttn.setObjectName("dataBttn")
        self.helpBttn = QtWidgets.QPushButton(DataEntry)
        self.helpBttn.setGeometry(QtCore.QRect(650, 10, 130, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(DataEntry)
        QtCore.QMetaObject.connectSlotsByName(DataEntry)
        DataEntry.setTabOrder(self.helpBttn, self.listDisplay)
        DataEntry.setTabOrder(self.listDisplay, self.quitBttn)
        DataEntry.setTabOrder(self.quitBttn, self.dataBttn)
        DataEntry.setTabOrder(self.dataBttn, self.cancelBttn)
        DataEntry.setTabOrder(self.cancelBttn, self.sqlBttn)
        DataEntry.setTabOrder(self.sqlBttn, self.acceptBttn)

    def retranslateUi(self, DataEntry):
        _translate = QtCore.QCoreApplication.translate
        DataEntry.setWindowTitle(_translate("DataEntry", "Machine Translation Data Entry Module"))
        self.acceptBttn.setText(_translate("DataEntry", "Accept"))
        self.titleLbl.setText(_translate("DataEntry", "Data Entry for "))
        self.quitBttn.setText(_translate("DataEntry", "Quit"))
        self.sqlBttn.setText(_translate("DataEntry", "SQL"))
        self.cancelBttn.setText(_translate("DataEntry", "Cancel"))
        self.dataBttn.setText(_translate("DataEntry", "Data"))
        self.helpBttn.setText(_translate("DataEntry", "Help"))

