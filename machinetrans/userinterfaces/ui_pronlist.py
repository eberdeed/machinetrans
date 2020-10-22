# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/pronlist.ui'
#
# Created: Thu Jan 25 11:35:27 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PronList(object):
    def setupUi(self, PronList):
        PronList.setObjectName("PronList")
        PronList.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        PronList.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PronList.setWindowIcon(icon)
        self.titleLbl = QtWidgets.QLabel(PronList)
        self.titleLbl.setGeometry(QtCore.QRect(10, 20, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.cancelBttn = QtWidgets.QPushButton(PronList)
        self.cancelBttn.setGeometry(QtCore.QRect(10, 530, 150, 50))
        self.cancelBttn.setObjectName("cancelBttn")
        self.acceptBttn = QtWidgets.QPushButton(PronList)
        self.acceptBttn.setGeometry(QtCore.QRect(640, 530, 150, 50))
        self.acceptBttn.setObjectName("acceptBttn")
        self.pronList = QtWidgets.QListWidget(PronList)
        self.pronList.setGeometry(QtCore.QRect(10, 60, 780, 460))
        self.pronList.setObjectName("pronList")
        self.addallBttn = QtWidgets.QPushButton(PronList)
        self.addallBttn.setGeometry(QtCore.QRect(490, 530, 150, 50))
        self.addallBttn.setObjectName("addallBttn")
        self.helpBttn = QtWidgets.QPushButton(PronList)
        self.helpBttn.setGeometry(QtCore.QRect(640, 10, 150, 50))
        self.helpBttn.setObjectName("helpBttn")
        self.singleBttn = QtWidgets.QPushButton(PronList)
        self.singleBttn.setGeometry(QtCore.QRect(160, 530, 150, 50))
        self.singleBttn.setObjectName("singleBttn")
        self.groupBttn = QtWidgets.QPushButton(PronList)
        self.groupBttn.setGeometry(QtCore.QRect(320, 530, 150, 50))
        self.groupBttn.setObjectName("groupBttn")

        self.retranslateUi(PronList)
        QtCore.QMetaObject.connectSlotsByName(PronList)
        PronList.setTabOrder(self.helpBttn, self.pronList)
        PronList.setTabOrder(self.pronList, self.cancelBttn)
        PronList.setTabOrder(self.cancelBttn, self.singleBttn)
        PronList.setTabOrder(self.singleBttn, self.groupBttn)
        PronList.setTabOrder(self.groupBttn, self.addallBttn)
        PronList.setTabOrder(self.addallBttn, self.acceptBttn)

    def retranslateUi(self, PronList):
        _translate = QtCore.QCoreApplication.translate
        PronList.setWindowTitle(_translate("PronList", "Pronoun Conjugation List"))
        self.titleLbl.setText(_translate("PronList", "Russian Pronoun List"))
        self.cancelBttn.setText(_translate("PronList", "Cancel"))
        self.acceptBttn.setText(_translate("PronList", "Accept"))
        self.addallBttn.setText(_translate("PronList", "Add All"))
        self.helpBttn.setText(_translate("PronList", "Help"))
        self.singleBttn.setText(_translate("PronList", "Singles"))
        self.groupBttn.setText(_translate("PronList", "Groups"))

