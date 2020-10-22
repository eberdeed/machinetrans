#!/usr/bin/python3
"""
    PronList:  Machine Translation Data Entry -- Russian Pronoun Declension List.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 22, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_pronlist import Ui_PronList
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView
from machinetrans.dataentry.decltable import DeclTable

class PronList(QDialog, Ui_PronList):
    """ Russian pronoun declension selector:  Allows for viewing, 
        and selection of pronouns. Also allows for one single 
        insertion of ALL pronouns.
    """
    
    helpfile = "/usr/share/machinetrans/resources/pronlist.html"
    parent = None
    columns = list()
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    morphs = None
    group = False
    comma = ", "
    groupindex = 0
    singleindex = 0
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the pronouns and their declensions.
        """
        super(PronList, self).__init__(parent)
        self.setupUi(self)
        self.groupView = QTextBrowser(self)
        self.groupView.setVisible(False)
        self.groupView.setEnabled(False)
        self.upBttn = QPushButton("^\n^\n^", self)
        self.upBttn.setVisible(False)
        self.upBttn.setEnabled(False)
        self.downBttn = QPushButton("V\nV\nV", self)
        self.downBttn.setVisible(False)
        self.downBttn.setEnabled(False)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.pronList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pronList.itemDoubleClicked.connect(self.pdecl)
        self.cancelBttn.clicked.connect(self.cancel)
        self.singleBttn.clicked.connect(self.singleconj)
        self.groupBttn.clicked.connect(self.groupconj)
        self.addallBttn.clicked.connect(self.addall)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.upBttn.clicked.connect(self.plusgroup)
        self.downBttn.clicked.connect(self.minusgroup)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.singleconj()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 20, tmpwidth, 40)
        tmpx = 10
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 140
        if self.group:
            tmpwidth = self.width1 - 130
            self.groupView.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
            tmpx = self.width1 - 120
            tmpy = (self.height1 / 2) - 150
            self.upBttn.setGeometry(tmpx, tmpy, 50, 120)
            tmpy += 140
            self.downBttn.setGeometry(tmpx, tmpy, 50, 120)
        else:
            self.pronList.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 780) / 2
        tmpint = 780 / 5
        self.cancelBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.singleBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.groupBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.addallBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def singleconj(self):
        """ Display the pronouns and their declensions.
            Utilizes a dictionary in the WordMorphs class
            for the data.
        """
        self.pronList.setVisible(True)
        self.pronList.setEnabled(True)
        self.group = False
        self.groupView.setVisible(False)
        self.groupView.setEnabled(False)
        self.upBttn.setVisible(False)
        self.upBttn.setEnabled(False)
        self.downBttn.setVisible(False)
        self.downBttn.setEnabled(False)
        self.pronList.clear()
        for x in self.morphs.singlekeys:
            tmplist = self.morphs.pronouns[x][:]
            tmplist = tmplist[:-1]
            tmpstr = self.comma.join(tmplist)
            item = QListWidgetItem(tmpstr)
            self.pronList.addItem(item)            
    
    def groupconj(self):
        """ Display a group value and allow for the 
            display of other group values.
        """
        self.pronList.setVisible(False)
        self.pronList.setEnabled(False)
        self.group = True
        self.groupView.setVisible(True)
        self.groupView.setEnabled(True)
        self.upBttn.setVisible(True)
        self.upBttn.setEnabled(True)
        self.downBttn.setVisible(True)
        self.downBttn.setEnabled(True)
        tmpstr = self.morphs.groupkeys[self.groupindex]
        tmpstr1 = self.morphs.pronouns[tmpstr][0][1]
        htmltable = DeclTable(tmpstr1)
        for y in range(6):
            x = self.morphs.pronouns[tmpstr][y]
            htmltable.addrow(x)
        tmpstr = htmltable.table()
        self.groupView.setHtml(tmpstr)
        currsize = QSize(self.width1, self.height1)
        resevent = QResizeEvent(currsize, currsize)
        self.resizeEvent(resevent)
        return
    
    def plusgroup(self):
        """ Increment the index of the group value allowing
            for the display of the next group in the sequence.
        """
        self.groupindex += 1
        if self.groupindex >= len(self.morphs.groupkeys):
            self.groupindex = 0
        tmpstr = self.morphs.groupkeys[self.groupindex]
        tmpstr1 = self.morphs.pronouns[tmpstr][0][1]
        htmltable = DeclTable(tmpstr1)
        for y in range(6):
            x = self.morphs.pronouns[tmpstr][y]
            htmltable.addrow(x)
        tmpstr = htmltable.table()
        self.groupView.setHtml(tmpstr)
            
    def minusgroup(self):
        """ Decrement the index of the group value allowing
            for the display of the preceding group in the sequence.
        """
        self.groupindex -= 1
        if self.groupindex < 0:
            self.groupindex = len(self.morphs.groupkeys) - 1
        tmpstr = self.morphs.groupkeys[self.groupindex]
        tmpstr1 = self.morphs.pronouns[tmpstr][0][1]
        htmltable = DeclTable(tmpstr1)
        for y in range(6):
            x = self.morphs.pronouns[tmpstr][y]
            htmltable.addrow(x)
        tmpstr = htmltable.table()
        self.groupView.setHtml(tmpstr)

    def pdecl(self):
        """ Collect the selected row of a single pronoun and pass along
            the name of the pronoun entry.
            Close the form.
        """
        index = self.pronList.currentRow()
        self.parent.pronname = self.morphs.singlekeys[index]
        self.close()
        
    def cancel(self):
        """ Cancel the event.
        """
        self.close()

    def addall(self):
        """ Signal the calling GUI to add all the 
            pronouns at once and close the form.
            The pronouns are added to the database
            in the calling GUI.
        """
        self.parent.addall = True
        self.close()
        
    def displayhelp(self):
        """ Display an HTML help file for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def accept(self):
        """ Collect the selected row or group index. 
            Show an error message if no single pronoun 
            is selected. Close the form.
        """
        self.parent.group = self.group
        if self.group:
            self.parent.groupindex = self.groupindex
        else:
            self.singleindex = -1
            self.singleindex = self.pronList.currentRow()
            if self.singleindex < 0:
                QMessageBox.warning(self, "No Item Selected", "There must be an item selected.")
                return
            else:
                self.parent.singleindex = self.singleindex
        self.close()
            
    def closeEvent(self, event):
        """ Close the form and pass along sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        