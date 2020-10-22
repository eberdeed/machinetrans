# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles/helpview.ui'
#
# Created: Thu Jan 25 11:35:28 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpView(object):
    def setupUi(self, HelpView):
        HelpView.setObjectName("HelpView")
        HelpView.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../usr/share/machinetrans/resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpView.setWindowIcon(icon)
        self.helpDisplay = QtWidgets.QTextBrowser(HelpView)
        self.helpDisplay.setGeometry(QtCore.QRect(10, 10, 780, 500))
        self.helpDisplay.setObjectName("helpDisplay")
        self.quitBttn = QtWidgets.QPushButton(HelpView)
        self.quitBttn.setGeometry(QtCore.QRect(325, 530, 150, 50))
        self.quitBttn.setObjectName("quitBttn")

        self.retranslateUi(HelpView)
        QtCore.QMetaObject.connectSlotsByName(HelpView)

    def retranslateUi(self, HelpView):
        _translate = QtCore.QCoreApplication.translate
        HelpView.setWindowTitle(_translate("HelpView", "MachineTrans Help"))
        self.quitBttn.setText(_translate("HelpView", "Quit"))

