#!/usr/bin/python3
"""
    SortedKeys:  Machine Translation Data Entry -- Sort Keys for SQL Data Display.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    October 30, 2017, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_sortedkeys import Ui_SortedKeys
from machinetrans.helpview import HelpView

class SortedKeys(QDialog, Ui_SortedKeys):
    """ A GUI to provide sorting keys for the SQLData class.
    """
    
    helpfile = "/usr/share/machinetrans/resources/sortedkeys.html"
    parent = None
    winx = 0
    winy = 0
    geometry = list()    
    width1 = 800
    height1 = 300
    types = None
    dictval = ""
    keylist = list()
    sortlist = list()
    
    def __init__(self, parent=None):
        """ Intialize the GUI and display the proper number of slots for the number
            of available keys.
        """
        super(SortedKeys, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.dictval = self.parent.wclass
        self.types = self.parent.types
        self.quitBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.accept)
        self.resetBttn.clicked.connect(self.reset)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.key1.currentIndexChanged.connect(self.handlekey1)
        self.key2.currentIndexChanged.connect(self.handlekey2)
        self.key3.currentIndexChanged.connect(self.handlekey3)
        self.key4.currentIndexChanged.connect(self.handlekey4)
        self.key5.currentIndexChanged.connect(self.handlekey5)
        self.key6.currentIndexChanged.connect(self.handlekey6)
        self.key7.currentIndexChanged.connect(self.handlekey7)
        self.key8.currentIndexChanged.connect(self.handlekey8)
        self.key9.currentIndexChanged.connect(self.handlekey9)
        self.reset()
        self.key1.setFocus()
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        
    def resizeEvent(self, event):
        """ Resize the GUI and record sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 / 300
        wscale = self.width1 / 800
        tmpx = self.width1 - 160
        tmpy = 0
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpint = (self.width1 - 120) / 3
        if (wscale > 1.5):
            tmpstart = ((self.width1 - (680 * wscale)) / 2) + (70 * wscale)
        else:
            tmpstart = 60 * wscale
        tmpx = tmpstart
        tmpy = 80 * hscale
        self.key1.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key2.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key3.setGeometry(tmpx, tmpy, 200, 35)
        tmpx = tmpstart
        tmpy = 150 * hscale
        self.key4.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key5.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key6.setGeometry(tmpx, tmpy, 200, 35)
        tmpx = tmpstart
        tmpy = 220 * hscale
        self.key7.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key8.setGeometry(tmpx, tmpy, 200, 35)
        tmpx += tmpint
        self.key9.setGeometry(tmpx, tmpy, 200, 35)
        tmpint = (self.width1 - 100) / 3
        if wscale > 1.5:
            tmpstart = ((self.width1 - (580 * wscale)) / 2) + (40 * wscale)
        else:
            tmpstart = 110 * wscale
        tmpx = tmpstart
        tmpy = 50 * hscale
        self.key1Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key2Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key3Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx = tmpstart
        tmpy = 120 * hscale
        self.key4Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key5Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key6Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx = tmpstart
        tmpy = 190 * hscale
        self.key7Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key8Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpx += tmpint
        self.key9Lbl.setGeometry(tmpx, tmpy, 100, 25)
        tmpint = (self.width1 - 180) / 3
        if wscale > 1.5:
            tmpx = 150 * wscale
        else:
            tmpx = 50 * wscale
        tmpy = 260 * hscale
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.resetBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def handlekey1(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        self.sortlist = list()
        item = self.key1.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key2.clear()
                self.key2.addItems(self.keylist)
                self.key2.setCurrentIndex(0)
                self.key2.setEnabled(True)

    def handlekey2(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key2.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key3.clear()
                self.key3.addItems(self.keylist)
                self.key3.setCurrentIndex(0)
                self.key3.setEnabled(True)

    def handlekey3(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key3.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key4.clear()
                self.key4.addItems(self.keylist)
                self.key4.setCurrentIndex(0)
                self.key4.setEnabled(True)

    def handlekey4(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key4.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key5.clear()
                self.key5.addItems(self.keylist)
                self.key5.setCurrentIndex(0)
                self.key5.setEnabled(True)

    def handlekey5(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key5.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key6.clear()
                self.key6.addItems(self.keylist)
                self.key6.setCurrentIndex(0)
                self.key6.setEnabled(True)

    def handlekey6(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key6.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key7.clear()
                self.key7.addItems(self.keylist)
                self.key7.setCurrentIndex(0)
                self.key7.setEnabled(True)

    def handlekey7(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key7.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key8.clear()
                self.key8.addItems(self.keylist)
                self.key8.setCurrentIndex(0)
                self.key8.setEnabled(True)

    def handlekey8(self):
        """ Get the selected item and append it to the sorting list.
            Set up the next drop down in the sequence for selection if necessary.
        """
        item = self.key8.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])
            del self.keylist[item] 
            if (len(self.keylist) > 1):
                self.key9.clear()
                self.key9.addItems(self.keylist)
                self.key9.setCurrentIndex(0)
                self.key9.setEnabled(True)

    def handlekey9(self):
        """ Get the selected item abad append it to the sorting list.
        """
        item = self.key9.currentIndex()
        if item > 0:
            self.sortlist.append(self.keylist[item])

    def reset(self):
        """ Prepare the GUI for data selection.  Set the necessary labels visible
            and initialize the first drop down.
        """
        self.keylist = list(self.types.wordkeys[self.dictval])
        numkeys = len(self.keylist)
        numkeys -= 1
        if numkeys > 0:
            numkeys -= 1
            if self.key2Lbl.isHidden():
                self.key2Lbl.setHidden(False)
        elif numkeys == 0 and not self.key2Lbl.isHidden():
            self.key2Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key3Lbl.isHidden():
                self.key3Lbl.setHidden(False)
        elif numkeys == 0 and not self.key3Lbl.isHidden():
            self.key3Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key4Lbl.isHidden():
                self.key4Lbl.setHidden(False)
        elif numkeys == 0 and not self.key4Lbl.isHidden():
            self.key4Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key5Lbl.isHidden():
                self.key5Lbl.setHidden(False)
        elif numkeys == 0 and not self.key5Lbl.isHidden():
            self.key5Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key6Lbl.isHidden():
                self.key6Lbl.setHidden(False)
        elif numkeys == 0 and not self.key6Lbl.isHidden():
            self.key6Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key7Lbl.isHidden():
                self.key7Lbl.setHidden(False)
        elif numkeys == 0 and not self.key7Lbl.isHidden():
            self.key7Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key8Lbl.isHidden():
                self.key8Lbl.setHidden(False)
        elif numkeys == 0 and not self.key8Lbl.isHidden():
            self.key8Lbl.setHidden(True)
        if numkeys > 0:
            numkeys -= 1
            if self.key9Lbl.isHidden():
                self.key9Lbl.setHidden(False)
        elif numkeys == 0 and not self.key9Lbl.isHidden():
            self.key9Lbl.setHidden(True)
        self.keylist.insert(0,"None")
        self.key1.clear()
        self.key1.addItems(self.keylist)
        self.key1.setCurrentIndex(0)
        self.key1.setEnabled(True)
        
    def accept(self):
        """ Accept the presented SQL commands.
        """
        self.parent.sortlist = self.sortlist
        self.close()
        
    def displayhelp(self):
        """ Display an HTML help page for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def cancel(self):
        """ Cancel and drop the presented SQL commands.
        """
        self.close()
        
    def closeEvent(self, event):
        """ Close the GUI and pass along GUI sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()
        