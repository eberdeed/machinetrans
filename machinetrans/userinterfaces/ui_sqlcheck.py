# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/sqlcheck.ui'
#
# Created: Thu Jan 25 11:35:23 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLCheck(object):
    def setupUi(self, SQLCheck):
        SQLCheck.setObjectName("SQLCheck")
        SQLCheck.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        SQLCheck.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SQLCheck.setWindowIcon(icon)
        self.sqlEdit = QtWidgets.QTextEdit(SQLCheck)
        self.sqlEdit.setGeometry(QtCore.QRect(10, 60, 780, 460))
        self.sqlEdit.setObjectName("sqlEdit")
        self.titleLbl = QtWidgets.QLabel(SQLCheck)
        self.titleLbl.setGeometry(QtCore.QRect(200, 10, 341, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(SQLCheck)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(SQLCheck)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(SQLCheck)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(SQLCheck)
        QtCore.QMetaObject.connectSlotsByName(SQLCheck)
        SQLCheck.setTabOrder(self.helpBttn, self.sqlEdit)
        SQLCheck.setTabOrder(self.sqlEdit, self.cancelBttn)
        SQLCheck.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, SQLCheck):
        _translate = QtCore.QCoreApplication.translate
        SQLCheck.setWindowTitle(_translate("SQLCheck", "SQL Check"))
        self.titleLbl.setText(_translate("SQLCheck", "SQL Commit Data Check"))
        self.cancelBttn.setText(_translate("SQLCheck", "Cancel"))
        self.acceptBttn.setText(_translate("SQLCheck", "Accept"))
        self.helpBttn.setText(_translate("SQLCheck", "Help"))

