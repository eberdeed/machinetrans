#!/usr/bin/python3
"""
    HelpView:  Machine Translation Data Entry -- Help Viewer.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    October 26, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_helpview import Ui_HelpView

class HelpView(QDialog, Ui_HelpView):
    """ A GUI to display help information.
    """
    failure = False
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    parent = None
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the Help file.
        """
        super(HelpView, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        try:
            textfile = open(parent.helpfile, "r", newline="\n", encoding="utf-8")
            helppage = textfile.read()
        except Exception as e:
            QMessageBox.warning(self, "Unable to Open Help File", "The system was unable to open the help file, error:  " + str(e))
            self.failure = True
        if not self.failure:
            self.helpDisplay.setHtml(helppage)
        self.quitBttn.clicked.connect(self.close)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.quitBttn.setFocus()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 100
        self.helpDisplay.setGeometry(10, 10, tmpwidth, tmpheight)
        tmpy = self.height1 - 70
        tmpx = (self.width1 - 150) / 2
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def closeEvent(self, event):
        """ Close the GUI and pass along GUI sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        