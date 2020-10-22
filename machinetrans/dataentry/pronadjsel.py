#!/usr/bin/python3
"""
    PronAdjSel:  Machine Translation Data Entry -- Russian Adjective Declension Selector.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 28, 2017, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_pronadjsel import Ui_PronAdjSel
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView
from machinetrans.dataentry.decltable import DeclTable

class PronAdjSel(QDialog, Ui_PronAdjSel):
    """ Russian Adjective Declension Selector.  Provides a list
        of adjective declension types to select from.
    """

    helpfile = "/usr/share/machinetrans/resources/pronadjsel.html"
    parent = None
    currtype = 0
    columns = list()
    titles = list()
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    comma = ", "
    geometry = list()    
    # Word Morphology class.
    morphs = None
    titles = list()
    
    def __init__(self, parent=None):
        """ Initialize the GUI and use the data from the WordMorphs class
            to fill the list of conjugations.
        """
        super(PronAdjSel, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.declType.currentIndexChanged.connect(self.seltype)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        comma = ", "
        self.currtype = self.parent.decltype
        # Set up the endings.
        self.titles = list(["Hard Endings", "ГКХ Soft Endings", "Soft Endings", "ОЙ Ending", "ЬЕ nueter Ending"])
        self.declType.addItems(self.titles)
        self.declType.setCurrentIndex(self.parent.decltype)
        self.createobj()

    def resizeEvent(self, event):
        """ Resize the form and save the GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 / 600
        wscale = self.width1 / 800
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 30, tmpwidth, 40)
        tmpx = (self.width1 - 330) / 2
        tmpy = 90 * hscale
        self.declType.setGeometry(tmpx, tmpy, 330, 40)
        tmpx = 100 * wscale
        tmpy = 150 * hscale
        tmpwidth = 600 * wscale
        tmpheight = 300 * hscale
        self.declList.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 500) / 2
        self.cancelBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + (100 * wscale)
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def seltype(self):
        """ Select the type of adjectival ending for this pronoun.
        """
        self.parent.decltype = self.declType.currentIndex()
        self.createobj()
        
    def selnum(self):
        """ Select the number of the adjectival ending for this pronoun and close the GUI.
        """
        self.parent.declnum = self.declList.currentRow()
        self.close()
        
    def createobj(self):
        ''' Create an HTML table of adjectival declensions.
        '''
        self.declList.clear()
        # A class to draw the HTML table.
        tmptable = DeclTable(self.titles[self.parent.decltype])
        for x in self.morphs.declension[self.parent.decltype]:
            tmptable.addrow(x)
        tmpstr = tmptable.table()
        # Put the table in the GUI.
        self.declList.clear()
        self.declList.setHtml(tmpstr)

    def cancel(self):
        """ Cancel the event.
        """
        self.parent.decltype = self.currtype
        self.close()

    def accept(self):
        """ Close the gui.
        """
        self.close()
            
    def displayhelp(self):
        """ Display an HTML help page.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()
            
    def closeEvent(self, event):
        """ Close the GUI and pass along window sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        