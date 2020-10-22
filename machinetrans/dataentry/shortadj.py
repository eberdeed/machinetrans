"""
    ShortAdj:  Machine Translation Data Entry -- Russian Short Form Adjectives.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 16, 2016, San Diego California United States of America
"""
import os, sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_shortadj import Ui_ShortAdj
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView

class ShortAdj(QDialog, Ui_ShortAdj):
    """ A GUI to enter Russian short form adjectives.
    """
    
    helpfile = "/usr/share/machinetrans/resources/shortadj.html"
    parent = None
    labeltext = ""
    rustr = ""
    enstr = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    sqlcommand = ""
    geometry = list()
    morphs = None
    stem = ""
    adjdict = dict()
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the data.
        """
        super(ShortAdj, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        self.stem = self.rustr[:-2]
        self.labeltext = self.titleLbl.text()
        self.labeltext += " " + self.rustr.capitalize()
        self.titleLbl.setText(self.labeltext)
        self.shortCheck.clicked.connect(self.enableform)
        self.quitBttn.clicked.connect(self.cancel)
        self.backBttn.clicked.connect(self.backpage)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.stemEdit.firereturn.triggered.connect(self.updatestem)
        self.stemEdit.firefocus.triggered.connect(self.updatestem)
        self.enEdit.firereturn.triggered.connect(self.updateeng)
        self.enEdit.firefocus.triggered.connect(self.updateeng)
        self.rumascEdit.setText(self.rustr)
        self.stemEdit.setText(self.stem)
        self.enEdit.setText(self.enstr)
        if self.parent.adjpages[1]:
            self.adjdict.clear()
            self.adjdict = self.parent.adjdict.copy()
            if self.adjdict["disabled"]:
                self.shortCheck.setChecked(False)
                self.stemEdit.setText("")
                self.stemEdit.setEnabled(False)
                self.rumascEdit.setText("")
                self.rumascEdit.setEnabled(False)
                self.rufemEdit.setText("")
                self.rufemEdit.setEnabled(False)
                self.runuetEdit.setText("")
                self.runuetEdit.setEnabled(False)
                self.ruplurEdit.setText("")
                self.ruplurEdit.setEnabled(False)
                self.enEdit.setText("")
                self.enEdit.setEnabled(False)
            else:
                self.shortCheck.setChecked(True)
                self.stemEdit.setText(self.adjdict["stem"])
                self.rumascEdit.setText(self.adjdict["masc"])
                self.rufemEdit.setText(self.adjdict["fem"])
                self.runuetEdit.setText(self.adjdict["nuet"])
                self.ruplurEdit.setText(self.adjdict["plur"])
                self.enEdit.setText(self.adjdict["eng"])
            return
        self.setdata()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record sizing information.
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
        self.titleLbl.setGeometry(10, 20, tmpwidth, 60)
        tmpy = 70 * hscale
        tmpx = (self.width1 / 2) - 80
        self.shortCheck.setGeometry(tmpx, tmpy, 160, 25)
        tmpy = 110 * hscale
        tmpx = (self.width1 - 700) / 2
        self.rumascLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20) 
        self.rufemLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 140 * hscale
        tmpx = (self.width1 - 700) / 2
        self.rumascEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20) 
        self.rufemEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 210 * hscale
        tmpx = (self.width1 - 700) / 2
        self.runuetLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20)
        self.ruplurLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 240 * hscale
        tmpx = (self.width1 - 700) / 2
        self.runuetEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20)
        self.ruplurEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 330) / 2
        tmpy = 300 * hscale
        self.stemLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 330 * hscale
        self.stemEdit.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 390 * hscale
        self.engLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 420 * hscale
        self.enEdit.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 - 540) / 2)
        tmpy = self.height1 - 80
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) - 75
        self.backBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + 120
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
        
    def updatestem(self):
        """ When the user changes the Russian stem for the adjective
            this method propogates it to all the instances of the adjective.
        """
        self.stem = self.stemEdit.text()
        self.setdata()
        
    def updateeng(self):
        """ Update the English translation value.
        """
        self.enstr = self.enEdit.text()


    def setdata(self):
        """ Decline and display one Russian short form adjective.
            Declension of short form adjectives is very simple.
        """
        self.shortCheck.setChecked(True)
        if self.rustr[-2] == "и" or self.rustr[-2] == "о": 
            self.rumascEdit.setText(self.stem)
            self.rufemEdit.setText(self.stem + self.morphs.adjshortsoft[2])
            self.runuetEdit.setText(self.stem + self.morphs.adjshortsoft[3])
            self.ruplurEdit.setText(self.stem + self.morphs.adjshortsoft[4])
        else:
            self.rumascEdit.setText(self.stem)
            self.rufemEdit.setText(self.stem + self.morphs.adjshorthard[2])
            self.runuetEdit.setText(self.stem + self.morphs.adjshorthard[3])
            self.ruplurEdit.setText(self.stem + self.morphs.adjshorthard[4])
            
    def accept(self):
        """ Accept the declension, gather the data,
            and create a series of SQL commands to insert
            the data into the database. Close the GUI.
        """
        if not self.shortCheck.isChecked():
            self.parent.shortadj = False
            self.parent.contpage = False
            self.close()
            return
        basecommand = self.parent.sqlcommand
        self.parent.sqldict["name"] = "\'" + self.enstr + "\'"
        self.parent.sqldict["runame"] = "\'" + self.rustr + "\'"
        self.parent.sqldict["gender"] = "\'masculine\'"
        self.parent.sqldict["declension"] = "\'" + self.rumascEdit.text() + "\'"
        self.parent.sqldict["wordcase"] = "\'nominative\'"
        self.parent.sqldict["animate"] = "\'inanimate\'"
        cols = "("
        data = "("
        for y in self.parent.sqldict:
            cols += y + ", "
            data += self.parent.sqldict[y] + ", "
        cols = cols[:-2] + ") VALUES"
        data = data[:-2] + ");\n"
        self.sqlcommand += basecommand + cols + data
        self.parent.sqldict["gender"] = "\'feminine\'"
        self.parent.sqldict["declension"] = "\'" + self.rufemEdit.text() + "\'"
        cols = "("
        data = "("
        for y in self.parent.sqldict:
            cols += y + ", "
            data += self.parent.sqldict[y] + ", "
        cols = cols[:-2] + ") VALUES"
        data = data[:-2] + ");\n"
        self.sqlcommand += basecommand + cols + data
        self.parent.sqldict["gender"] = "\'nueter\'"
        self.parent.sqldict["declension"] = "\'" + self.runuetEdit.text() + "\'"
        cols = "("
        data = "("
        for y in self.parent.sqldict:
            cols += y + ", "
            data += self.parent.sqldict[y] + ", "
        cols = cols[:-2] + ") VALUES"
        data = data[:-2] + ");\n"
        self.sqlcommand += basecommand + cols + data
        self.parent.sqldict["gender"] = "\'plural\'"
        self.parent.sqldict["declension"] = "\'" + self.ruplurEdit.text() + "\'"
        cols = "("
        data = "("
        for y in self.parent.sqldict:
            cols += y + ", "
            data += self.parent.sqldict[y] + ", "
        cols = cols[:-2] + ") VALUES"
        data = data[:-2] + ");\n"
        self.sqlcommand += basecommand + cols + data
        self.parent.shortadjcommand = self.sqlcommand
        self.parent.contpage = False
        self.close()
    
    def enableform(self):
        if self.shortCheck.isChecked():
            self.stemEdit.setEnabled(True)
            self.rumascEdit.setEnabled(True)
            self.rufemEdit.setEnabled(True)
            self.runuetEdit.setEnabled(True)
            self.ruplurEdit.setEnabled(True)
            self.enEdit.setEnabled(True)
            if self.parent.adjpages[1] and not self.adjdict["disabled"]:
                self.stemEdit.setText(self.adjdict["stem"])
                self.rumascEdit.setText(self.adjdict["masc"])
                self.rufemEdit.setText(self.adjdict["fem"])
                self.runuetEdit.setText(self.adjdict["nuet"])
                self.ruplurEdit.setText(self.adjdict["plur"])
                self.enEdit.setText(self.adjdict["eng"])
                return
            self.setdata()
        else:
            self.stemEdit.setText("")
            self.stemEdit.setEnabled(False)
            self.rumascEdit.setText("")
            self.rumascEdit.setEnabled(False)
            self.rufemEdit.setText("")
            self.rufemEdit.setEnabled(False)
            self.runuetEdit.setText("")
            self.runuetEdit.setEnabled(False)
            self.ruplurEdit.setText("")
            self.ruplurEdit.setEnabled(False)
            self.enEdit.setText("")
            self.enEdit.setEnabled(False)

        
    def displayhelp(self):
        """ Display an HTML help page for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def cancel(self):
        """ Cancel the event.
        """
        self.parent.cancel = True
        self.close()
        
    def backpage(self):
        """ Go back to the main adjective page.
        """
        self.parent.contpage = True
        self.parent.adjpages[1] = True
        if self.shortCheck.isChecked():
            self.adjdict["disabled"] = False
            self.adjdict["stem"] = self.stemEdit.text()
            self.adjdict["masc"] = self.rumascEdit.text()
            self.adjdict["fem"] = self.rufemEdit.text()
            self.adjdict["nuet"] = self.runuetEdit.text()
            self.adjdict["plur"] = self.ruplurEdit.text()
            self.adjdict["eng"] = self.enEdit.text()
        else:
            self.adjdict["disabled"] = True
        self.parent.adjdict = self.adjdict.copy()
        self.close()
           
    def closeEvent(self, event):
        """ Close the GUI and pass along GUI sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept() 