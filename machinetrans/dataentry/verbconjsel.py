#!/usr/bin/python3
"""
    VerbConjSel:  Machine Translation Data Entry -- Russian Verb Conjugation Selector.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 22, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_verbconjsel import Ui_VerbConjSel
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView

class VerbConjSel(QDialog, Ui_VerbConjSel):
    """ Russian Verb Conjugation Selector.  Provides a list
        of verb conjugations to select from.  This GUI is
        supplementary to the verb conjugation page.
    """

    helpfile = "/usr/share/machinetrans/resources/verbconjsel.html"
    parent = None
    columns = list()
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    morphs = None
    comma = ", "
    
    def __init__(self, parent=None):
        """ Initialize the GUI and use the data from the WordMorphs class
            to fill the list of conjugations.
        """
        super(VerbConjSel, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.conjList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.conjList.itemClicked.connect(self.verbconj)
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.showdata()
        
    def resizeEvent(self, event):
        """ Resize the form and save the GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 30, tmpwidth, 40)
        tmpx = 10
        tmpy = 70
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 150
        self.conjList.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 500) / 2
        self.cancelBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx = self.width1 - (((self.width1 - 500) / 2) + 150)
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def showdata(self):
        """ Draw the data on the QListWidget.
        """
        self.conjList.clear()
        for x in self.morphs.conjugations:
            tmpstr = self.comma.join(x)
            item = QListWidgetItem(tmpstr)
            self.conjList.addItem(item)            
        
    def verbconj(self):
        """ Collect the selected conjugation as an index.
            This value is passed along to the VerbConjugation class.
        """
        self.parent.index = self.conjList.currentRow()
        self.close()
        
    def cancel(self):
        """ Cancel the event.
        """
        self.parent.cancel = True
        self.close()

    def accept(self):
        """ Collect the selected conjugation and pass it to the
            VerbConjugation class.  Offer an error message if
            nothing is selected.
        """
        tmpint = self.conjList.currentRow()
        if tmpint < 0:
            QMessageBox.warning(self, "No Item Selected", "There must be an item selected.")
        else:
            self.parent.index = tmpint
            self.close()
            
    def displayhelp(self):
        """ Display help for this GUI as an HTML page.
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