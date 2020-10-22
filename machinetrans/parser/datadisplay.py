#!/usr/bin/python3
"""
    DataDisplay:  Machine Translation Data Entry -- English lanuage sentence display.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    July 4, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_datadisplay import Ui_DataDisplay
from machinetrans.helpview import HelpView

class DataDisplay(QDialog, Ui_DataDisplay):
    """ A GUI to display English sentences generated
        with random data.
    """
    
    helpfile = "/usr/share/machinetrans/resources/datadisplay.html"
    parent = None
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the data.
        """
        super(DataDisplay, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        tmpstr = self.titleLbl.text() + " " + self.parent.datatype
        self.titleLbl.setText(tmpstr)
        self.dataEdit.setText(self.parent.datastr)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.acceptBttn.setFocus()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record GUI sizing data.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 10, tmpwidth, 25)
        tmpx = 10
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 140
        self.dataEdit.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 65
        tmpx = (self.width1 - 150) / 2
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def displayhelp(self):
        """ Display help in HTML format.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def accept(self):
        """ Close the GUI passing along GUI sizing data.
        """
        self.parent.setVisible(True)
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        self.close()
        
