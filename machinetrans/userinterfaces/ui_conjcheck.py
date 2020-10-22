# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/conjcheck.ui'
#
# Created: Fri Aug 25 14:00:03 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConjCheck(object):
    def setupUi(self, ConjCheck):
        ConjCheck.setObjectName("ConjCheck")
        ConjCheck.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        ConjCheck.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConjCheck.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(ConjCheck)
        self.titleLbl.setGeometry(QtCore.QRect(10, 30, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(ConjCheck)
        self.cancelBttn.setGeometry(QtCore.QRect(150, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(ConjCheck)
        self.acceptBttn.setGeometry(QtCore.QRect(500, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.conjList = QtWidgets.QListWidget(ConjCheck)
        self.conjList.setGeometry(QtCore.QRect(10, 70, 780, 450))
        self.conjList.setObjectName("conjList")
        self.helpBttn = QtWidgets.QPushButton(ConjCheck)
        self.helpBttn.setGeometry(QtCore.QRect(630, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")

        self.retranslateUi(ConjCheck)
        QtCore.QMetaObject.connectSlotsByName(ConjCheck)
        ConjCheck.setTabOrder(self.conjList, self.cancelBttn)
        ConjCheck.setTabOrder(self.cancelBttn, self.acceptBttn)

    def retranslateUi(self, ConjCheck):
        _translate = QtCore.QCoreApplication.translate
        ConjCheck.setWindowTitle(_translate("ConjCheck", "Verb Conjugation List"))
        self.titleLbl.setText(_translate("ConjCheck", "Russian Verb Conjugation List"))
        self.cancelBttn.setText(_translate("ConjCheck", "Cancel"))
        self.acceptBttn.setText(_translate("ConjCheck", "Accept"))
        self.helpBttn.setText(_translate("ConjCheck", "Help"))

