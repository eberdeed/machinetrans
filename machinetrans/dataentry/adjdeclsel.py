#!/usr/bin/python3
"""
    AdjDeclSel:  Machine Translation Data Entry -- Russian Adjective Declension Selector.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 28, 2017, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_adjdeclsel import Ui_AdjDeclSel
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView
from machinetrans.dataentry.decltable import DeclTable

class AdjDeclSel(QDialog, Ui_AdjDeclSel):
    """ Russian Adjective Declension Selector.  Provides a list
        of adjective declension types to select from.
    """

    helpfile = "/usr/share/machinetrans/resources/adjdeclsel.html"
    parent = None
    currtype = 0
    columns = list()
    titles = list()
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    # Word Morphology class.
    morphs = None
    
    def __init__(self, parent=None):
        """ Initialize the GUI and use the data from the WordMorphs class
            to fill the list of conjugations.
        """
        super(AdjDeclSel, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.upList.clicked.connect(self.decdecl)
        self.downList.clicked.connect(self.incdecl)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        comma = ", "
        self.currtype = self.parent.adjtype
        # Set up the endings.
        self.titles = list(["Hard Endings", "ГКХ Soft Endings", "Soft Endings", "ОЙ Ending", "ЬЕ nueter Ending"])
        self.createobj()

    def resizeEvent(self, event):
        """ Resize the form and save the GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 / 600
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 30, tmpwidth, 40)
        tmpx = 10
        tmpy = 70
        tmpwidth = self.width1 - 80
        tmpheight = self.height1 - 150
        self.declView.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpx = self.width1 - 60
        tmpy = 140 * hscale
        self.upList.setGeometry(tmpx, tmpy, 50, 100)
        tmpy =  260 * hscale
        self.downList.setGeometry(tmpx, tmpy, 50, 100)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 500) / 2
        self.cancelBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx = self.width1 - (((self.width1 - 500) / 2) + 150)
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def incdecl(self):
        """ Increment the selected declension.  This value is passed onto the parent class.
        """
        self.parent.adjtype += 1
        if self.parent.adjtype > 4:
            self.parent.adjtype = 0
        self.createobj()

    def decdecl(self):
        """ Decrement the selected declension.  This value is passed to the parent class.
        """
        self.parent.adjtype -= 1
        if self.parent.adjtype < 0:
            self.parent.adjtype = 4
        self.createobj()
        
    def createobj(self):
        ''' Create an HTML table of adjectival declensions.
        '''
        self.declView.clear()
        # A class to draw the HTML table.
        tmptable = DeclTable(self.titles[self.parent.adjtype])
        for x in self.morphs.declension[self.parent.adjtype]:
            tmptable.addrow(x)
        tmpstr = tmptable.table()
        # Put the table in the GUI.
        self.declView.clear()
        self.declView.setHtml(tmpstr)

    def cancel(self):
        """ Cancel the event.
        """
        self.parent.adjtype = self.currtype
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