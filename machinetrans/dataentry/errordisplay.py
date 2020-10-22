#!/usr/bin/python3
"""
    ErrorDisplay:  Machine Translation Data Entry -- SQL Error Display.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    July 1, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_errordisplay import Ui_ErrorDisplay
from machinetrans.helpview import HelpView

class ErrorDisplay(QDialog, Ui_ErrorDisplay):
    """ A GUI to display PostgreSQL errors.  It needs a seperate GUI
        because the error data is so large.
    """

    helpfile = "/usr/share/machinetrans/resources/errordisplay.html"
    parent = None
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    
    def __init__(self, parent=None):
        """ Initialize a QDialog and connect the signals
            to their various methods.
        """
        super(ErrorDisplay, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.errorEdit.setPlainText(self.parent.errormessage)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.acceptBttn.setFocus()

    def resizeEvent(self, event):
        """ Resize the GUI.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 10, tmpwidth, 25)
        tmpx = 20
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 140
        self.errorEdit.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 70
        tmpx = (self.width1 - 150) / 2
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def displayhelp(self):
        """ Display help for this GUI as an HTML page.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()
        
    def accept(self):
        """ Accept the error and close the GUI.
        """
        self.parent.setVisible(True)
        self.close()
        
    def closeEvent(self, event):
        """ Close the GUI passing along GUI sizing information.
        """ 
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()