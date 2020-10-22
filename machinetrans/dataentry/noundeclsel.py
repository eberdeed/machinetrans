#!/usr/bin/python3
"""
    NounDeclSel:  Machine Translation Data Entry -- Russian Noun Declension Selector.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 28, 2017, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_noundeclsel import Ui_NounDeclSel
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView
from machinetrans.dataentry.decltable import DeclTable

class NounDeclSel(QDialog, Ui_NounDeclSel):
    """ Russian Noun Declension Selector.  Select a noun declenion
        and pass the selection back to the noun declension class.
    """

    helpfile = "/usr/share/machinetrans/resources/noundeclsel.html"
    parent = None
    columns = list()
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    comma = ", "
    geometry = list()    
    titles = list()
    morphs = None
    tmpint = -1
    def __init__(self, parent=None):
        """ Initialize the GUI and use the data from the WordMorphs class
            to fill the list of declensions from the gender and number
            value determined by the noun declension class.
        """
        super(NounDeclSel, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.declList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.close)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.declList.itemClicked.connect(self.noundecl)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        comma = ", "
        self.titles = list(["Masculine Singular", "Nueter Singular", "Feminine Singular",
            "Masculine Plural", "Nueter Plural", "Feminine Plural", "Plural Only"])
        for x in self.titles:
            self.genderBox.addItem(x)
        self.createobj()
        self.genderBox.currentIndexChanged.connect(self.changedecltype)
        self.genderBox.setCurrentIndex(self.parent.decltype)
        
    def resizeEvent(self, event):
        """ Resize the form and save the GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        wscale = self.width1 / 800
        hscale = self.height1 / 600
        tmpy = 80 * hscale
        tmpx = 170 * wscale
        self.genderBox.setGeometry(tmpx, tmpy, 470, 35)
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpy = 20
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 30, tmpwidth, 40)
        tmpx = 110 * wscale
        tmpy = 160 * hscale
        tmpwidth = 600 * wscale
        tmpheight = 300 * hscale
        self.declList.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 70
        tmpx = 10
        self.cancelBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = self.width1 - 170
        self.height1 - 70
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def createobj(self):
        ''' Create an HTML table of the noun declensions.
        '''
        tmplist = list()
        tmptable = None
        self.declList.clear()
        # A class to draw the HTML table.
        tmplist = self.parent.morphs.datalist[self.parent.decltype][:]
        for x in tmplist:
            tmpstr = self.comma.join(x)
            item = QListWidgetItem(tmpstr)
            self.declList.addItem(item)
        
    def changedecltype(self):
        """ Change the type of declension, i.e. Masculine Plural,
            Feminine Singular, etc.
        """
        self.parent.decltype = self.genderBox.currentIndex()
        self.createobj()
        
    def noundecl(self):
        """ Collect the selected declension as an index.
            This value is passed along to the noun declension class.
            Ensure that the declension number is within range for
            the given declension type.
        """
        self.tmpint = self.declList.currentRow()
        
    def cancel(self):
        """ Cancel the event.
        """
        self.tmpint = self.parent.declnum
        self.close()

    def displayhelp(self):
        """ Display an HTML page with help for the current GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()
            
    def closeEvent(self, event):
        """ Close the GUI and pass along window sizing information.
            Determine animate/inanimate status.
        """
        if self.tmpint < 0 and self.parent.decltype != 6:
            QMessageBox.warning(self, "Unselected Declension Type", "The declension type was not selected.")
            event.ignore()
            return
        elif self.parent.decltype == 6:
            self.parent.declnum = 0
        else:
            self.parent.declnum = self.tmpint
        self.parent.animated = False
        if self.parent.decltype == 0:
            if self.parent.declnum == 0:
                self.parent.animated = True
            elif self.parent.declnum == 1:
                self.parent.animated = False
            elif self.parent.declnum == 2:
                self.parent.animated = True
            elif self.parent.declnum == 3:
                self.parent.animated = False
            elif self.parent.declnum == 4:
                self.parent.animated = True
            elif self.parent.declnum == 5:
                self.parent.animated = False
            elif self.parent.declnum == 6:
                self.parent.animated = True
            elif self.parent.declnum == 7:
                self.parent.animated = False
            elif self.parent.declnum == 8:
                self.parent.animated = True
            elif self.parent.declnum == 9:
                self.parent.animated = False
        elif self.parent.decltype == 3:
            if self.parent.declnum == 0:
                self.parent.animated = True
            elif self.parent.declnum == 1:
                self.parent.animated = False
            elif self.parent.declnum == 2:
                self.parent.animated = True
            elif self.parent.declnum == 3:
                self.parent.animated = False
            elif self.parent.declnum == 4:
                self.parent.animated = True
            elif self.parent.declnum == 5:
                self.parent.animated = False
            elif self.parent.declnum == 6:
                self.parent.animated = True
            elif self.parent.declnum == 7:
                self.parent.animated = False
            elif self.parent.declnum == 8:
                self.parent.animated = True
            elif self.parent.declnum == 9:
                self.parent.animated = False
            elif self.parent.declnum == 10:
                self.parent.animated = True
            elif self.parent.declnum == 11:
                self.parent.animated = False
        elif self.parent.decltype == 5:
            if self.parent.declnum == 0:
                self.parent.animated = True
            elif self.parent.declnum == 1:
                self.parent.animated = False
            elif self.parent.declnum == 2:
                self.parent.animated = True
            elif self.parent.declnum == 3:
                self.parent.animated = False
            elif self.parent.declnum == 4:
                self.parent.animated = True
            elif self.parent.declnum == 5:
                self.parent.animated = False
            elif self.parent.declnum == 6:
                self.parent.animated = True
            elif self.parent.declnum == 7:
                self.parent.animated = False
            elif self.parent.declnum == 8:
                self.parent.animated = True
            elif self.parent.declnum == 9:
                self.parent.animated = False
            elif self.parent.declnum == 10:
                self.parent.animated = True
            elif self.parent.declnum == 11:
                self.parent.animated = False
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        