# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/datadisplay.ui'
#
# Created: Thu Jan 25 11:35:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataDisplay(object):
    def setupUi(self, DataDisplay):
        DataDisplay.setObjectName("DataDisplay")
        DataDisplay.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        DataDisplay.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataDisplay.setWindowIcon(icon)
        self.dataEdit = QtWidgets.QTextEdit(DataDisplay)
        self.dataEdit.setGeometry(QtCore.QRect(10, 60, 780, 470))
        self.dataEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dataEdit.setObjectName("dataEdit")
        self.titleLbl = QtWidgets.QLabel(DataDisplay)
        self.titleLbl.setGeometry(QtCore.QRect(10, 20, 780, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.acceptBttn = QtWidgets.QPushButton(DataDisplay)
        self.acceptBttn.setGeometry(QtCore.QRect(300, 540, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(DataDisplay)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(DataDisplay)
        QtCore.QMetaObject.connectSlotsByName(DataDisplay)
        DataDisplay.setTabOrder(self.helpBttn, self.dataEdit)
        DataDisplay.setTabOrder(self.dataEdit, self.acceptBttn)

    def retranslateUi(self, DataDisplay):
        _translate = QtCore.QCoreApplication.translate
        DataDisplay.setWindowTitle(_translate("DataDisplay", "Data Display"))
        self.titleLbl.setText(_translate("DataDisplay", "Machine Translation Data Display"))
        self.acceptBttn.setText(_translate("DataDisplay", "Continue"))
        self.helpBttn.setText(_translate("DataDisplay", "Help"))

