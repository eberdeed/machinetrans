# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/sqltest.ui'
#
# Created: Thu Jan 25 11:35:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLTest(object):
    def setupUi(self, SQLTest):
        SQLTest.setObjectName("SQLTest")
        SQLTest.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        SQLTest.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SQLTest.setWindowIcon(icon)
        self.sqlEdit = QtWidgets.QTextEdit(SQLTest)
        self.sqlEdit.setGeometry(QtCore.QRect(10, 60, 780, 460))
        self.sqlEdit.setObjectName("sqlEdit")
        self.titleLbl = QtWidgets.QLabel(SQLTest)
        self.titleLbl.setGeometry(QtCore.QRect(210, 20, 341, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(SQLTest)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(SQLTest)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.helpBttn = QtWidgets.QPushButton(SQLTest)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(SQLTest)
        QtCore.QMetaObject.connectSlotsByName(SQLTest)
        SQLTest.setTabOrder(self.helpBttn, self.sqlEdit)
        SQLTest.setTabOrder(self.sqlEdit, self.cancelBttn)
        SQLTest.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, SQLTest):
        _translate = QtCore.QCoreApplication.translate
        SQLTest.setWindowTitle(_translate("SQLTest", "SQL Check"))
        self.titleLbl.setText(_translate("SQLTest", "SQL Command Editor"))
        self.cancelBttn.setText(_translate("SQLTest", "Cancel"))
        self.acceptBttn.setText(_translate("SQLTest", "Continue"))
        self.helpBttn.setText(_translate("SQLTest", "Help"))

