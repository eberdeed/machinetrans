#!/usr/bin/python3
"""
    DeclEntry:  Machine Translation Data Entry -- Russian Noun Declension.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 1, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from machinetrans.userinterfaces.ui_declentry import Ui_DeclEntry
from machinetrans.data.wordmorph import WordMorph
from machinetrans.dataentry.decltable import DeclTable
from machinetrans.dataentry.wordparsesmall import WordParseSmall
from machinetrans.helpview import HelpView
from machinetrans.dataentry.noundeclsel import NounDeclSel

class DeclEntry(QDialog, Ui_DeclEntry):
    """ A GUI to enter Russian noun declensions.
        Uses data from the WordMorph class and uses 
        the WordParse class to determine noun gender
        from the given noun.
    """
    
    helpfile = "/usr/share/machinetrans/resources/declentry.html"
    parent = None
    labeltext = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()
    
    morphs = None
    tableobj = list()
    decllist = list()
    gencheck = False
    singgender = None
    numeric = False
    instrumental = ""
    oblique = ""
    rustr = ""
    stem = ""
    ending = ""
    penul = ""
    enstr = ""
    decltype = 0
    declnum = 0
    otherdecl = -1
    parser = None
    buttonstart = 5
    animated = False
    plural = False
    numbers = ("один", "два", "три", "четыре")
    def __init__(self, parent=None):
        """ Initialize the GUI and determine the gender of the noun
            using the WordParse class.  The drawtable method uses
            the gender found to determine what to display and also
            uses the DeclTable class to create the HTML code for
            the table displayed.
        """
        super(DeclEntry, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.parser = WordParseSmall(self)
        self.rustr = self.parent.rustr
        self.animated = self.parent.sqldict["animate"] == "animate"
        self.singgender = self.parser.parse(self.rustr)
        if self.singgender == "masculine":
            self.decltype = 0
        elif self.singgender == "nueter":
            self.decltype = 1
        elif self.singgender == "feminine":
            self.decltype = 2
        elif self.singgender == "plural":
            self.decltype = 3
            self.singgender = "masculine"
        else:
            self.decltype = 0
            self.singgender = "masculine"
        self.ending = self.rustr[-1]
        self.penul = self.rustr[-2]
        if self.ending in self.morphs.vowels:
            self.stem = self.rustr[:-1]
        elif self.ending == 'ь':
            self.stem = self.rustr[:-1]
        else:
            self.stem = self.rustr
        self.enstr = self.parent.sqldict["name"].strip("\'")
        del(self.parent.sqldict["name"])
        self.enEdit.setText(self.enstr)
        # Initialize the outgoing data list.
        self.parent.declension = list()
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        # This adjusts the postions of the buttons,
        # so you cannot double click and select
        # the wrong button when the GUI changes.
        self.buttonstart = 5
        cursize = self.size()
        sizeevent = QResizeEvent(cursize, cursize)
        self.resizeEvent(sizeevent)
        # Connect the signals to the methods.
        self.acceptBttn.clicked.connect(self.accept)
        self.declBttn.clicked.connect(self.finddecl)
        self.rejectBttn.clicked.connect(self.cancel)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.stemEdit.firereturn.triggered.connect(self.updatestem)
        self.stemEdit.firefocus.triggered.connect(self.updatestem)
        self.wordlogic()
        self.createobj()
        
    def singulartitle(self):
        """ Display a title for a singular noun.
        """
        tmpstr = self.singgender.capitalize() + " Russian Noun Declension"
        self.titleLbl.setText(tmpstr)

    def pluraltitle(self):
        """ Display a title for a plural noun.
        """
        tmpstr = "Russian Plural Noun Declension"
        self.titleLbl.setText(tmpstr)
                
    def resizeEvent(self, event):
        """ Resize the GUI and store sizing information.
        """ 
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 /600
        wscale = self.width1 / 800
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 20, tmpwidth, 30)
        tmpheight = hscale * 180
        self.tableView.setGeometry(10, 60, tmpwidth, tmpheight)
        tmpint = tmpwidth / 6
        tmpy = 250 * hscale
        tmpint = 30 * hscale
        tmpx = (self.width1 - 740) / 2
        self.engLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30        
        self.stemLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.enEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.stemEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 - 740) / 2
        tmpy += 40
        self.nomLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30        
        self.accLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.nomEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.accEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy += 40
        tmpx = (self.width1 - 740) / 2
        self.genLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30        
        self.datLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.genEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.datEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy += 40
        tmpx = (self.width1 - 740) / 2
        self.insLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30        
        self.prpLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.insEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.prpEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = self.height1 - 70
        tmpx = 130 * wscale
        self.rejectBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = 330 * wscale
        self.declBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = ((self.width1 / 2) + (130 * wscale))
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def wordlogic(self):
        """ Set up the HTML table of the currently selected declension.
            Do some checking on the ending so the right one is selected
            and displayed in the line editors below.
            Fill out the GUI with the declension information.
        """
        self.rustr = self.parent.rustr
        self.instrumental = ""
        self.oblique = ""
        if self.rustr[-2:] == "ие" and not self.gencheck:
            answer = QMessageBox.question(self, "Ambiguous Ending", "Is the ending \"ие\" an adjectival noun?", QMessageBox.Yes, QMessageBox.No)
            if answer == QMessageBox.No:
                self.singgender = "nueter"
                self.decltype = 1
                self.stem = self.rustr[:-2]
                self.declnum = 2
                self.gencheck = True
                self.stemEdit.setText(self.stem)
            else:
                self.decltype = 6
                self.stem = self.rustr[:-2]
                if self.rustr[-3] in self.morphs.reqi:
                    if self.animated:
                        self.declnum = 18
                    else:
                        self.declnum = 19
                else:
                    if self.animated:
                        self.declnum = 16
                    else:
                        self.declnum = 17
                self.gencheck = True
                self.stemEdit.setText(self.stem)
        elif self.decltype < 3:
            if self.singgender == "masculine":
                if self.rustr[-2:] == "ий":
                    answer = QMessageBox.question(self, "Ambiguous Ending in Masculine", "Is the ending \"ий\" an adjectival noun?", QMessageBox.Yes, QMessageBox.No)
                    if answer == QMessageBox.Yes:
                        self.stem = self.rustr[:-2]
                        testchar = self.stem[-1]
                        if testchar in self.morphs.reqi:
                            if self.animated:
                                self.declnum = 18
                            else:
                                self.declnum = 19
                        elif self.animated:
                            self.declnum = 16
                        else:
                            self.declnum = 17
                    else:
                        self.stem = self.rustr[:-2]
                        if self.animated:
                            self.declnum = 10
                        else:
                            self.declnum = 11
                elif self.rustr[-2:] == "ец":
                    self.stem = self.rustr[:-2] + "ц"
                    if self.animated:
                        self.declnum = 0
                    else:
                        self.declnum = 1
                elif self.ending == "ь":
                    self.stem = self.rustr[:-1]
                    if self.animated:
                        self.declnum = 2
                    else:
                        self.declnum = 3
                elif self.rustr[-2:] == "ый":
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 14
                    else:
                        self.declnum = 15
                elif self.rustr[-2:] == "ой":
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 20
                    else:
                        self.declnum = 21
                elif self.ending == "й":
                    self.stem = self.rustr[:-1]
                    if self.animated:
                        self.declnum = 4
                    else:
                        self.declnum =  5
                else:
                    self.stem = self.rustr
                    if self.animated:
                        self.declnum = 0
                    else:
                        self.declnum = 1
            elif self.singgender == "feminine":
                if self.ending == "ь":
                    self.stem =self.rustr[:-1]
                    self.declnum = 5
                elif self.rustr[-2:] == "ая" and self.rustr[-3] in self.morphs.reqi:
                    self.stem = self.rustr[:-2]
                    self.declnum = 10
                elif self.rustr[-2:] == "ая":
                    self.stem = self.rustr[:-2]
                    self.declnum = 8
                elif self.rustr[-2:] == "яя":
                    self.stem = self.rustr[:-2]
                    self.declnum = 9
                elif self.rustr[-2:] == "ья":
                    self.stem = self.rustr[:-2]
                    self.declnum = 12
                elif self.ending == "я" and self.penul == "и":
                    self.stem =self.rustr[:-2]
                    self.declnum = 4
                elif self.ending == "а" and self.penul in self.morphs.reqi:
                    self.stem =self.rustr[:-1]
                    self.declnum = 2
                elif self.ending == "я" and self.penul in self.morphs.reqi:
                    self.stem =self.rustr[:-1]
                    self.declnum = 3
                elif self.ending == "а":
                    self.stem =self.rustr[:-1]
                    self.declnum = 0
                elif self.ending == "я":
                    self.stem =self.rustr[:-1]
                    self.declnum = 6
                else:
                    self.stem =self.rustr[:-1]
                    selfdeclnum = 0
            elif self.singgender == "nueter":
                if self.rustr[-2:] == "ое" and self.rustr[-3] in self.morphs.reqi:
                    self.stem = self.rustr[:-2]
                    self.declnum = 7
                elif self.rustr[-2:] == "ое":
                    self.stem = self.rustr[:-2]
                    self.declnum = 5
                elif self.rustr[-2:] == "ее":
                    self.stem = self.rustr[:-2]
                    self.declnum = 6
                elif self.rustr[-2:] == "ье":
                    self.stem = self.rustr[:-2]
                    self.declnum = 9
                elif self.ending == "е":
                    if self.penul == "и":
                        self.stem =self.rustr[:-2]
                        self.declnum = 2
                    else:
                        self.stem =self.rustr[:-1]
                        self.declnum = 1
                elif self.ending == "о":
                    self.stem =self.rustr[:-1]
                    self.declnum = 0
                elif self.rustr[-2:] == "мя":
                    self.stem =self.rustr[:-2]
                    self.declnum = 3
                else:
                    self.stem =self.rustr[:-1]
                    self.declnum = 0
        elif self.decltype > 2:
            if not (self.decltype == 6):
                self.enstr = self.enEdit.text()
                self.endings = self.enstr[-1]
                # Check to make sure the noun is not a collective noun,
                # and if not make the English noun plural.
                if self.endings != "s" and self.parent.sqldict["variety"] != "\'collective\'":
                    if self.endings == "y":
                        self.enEdit.setText(self.enstr[:-1] + "ies")
                    else:
                        self.endings = self.enstr[-2:]
                        if self.endings == "sh":
                            self.enEdit.setText(self.enstr + "es")
                        else:
                            self.enEdit.setText(self.enstr + "s")
            if self.decltype == 6:
                self.handlenums()
            elif self.singgender == "masculine":
                # Determine the declension to use.
                if self.declnum > 14:
                    self.declnum += 6
                    self.stem = self.rustr[:-2]
                elif self.rustr[-2:] == "ец":
                    self.stem = self.rustr[:-2] + "ц"
                    if self.animated:
                        self.declnum = 2
                    else:
                        self.declnum = 3
                elif self.ending in self.morphs.reqi:
                    if self.animated:
                        self.declnum = 8
                    else:
                        self.declnum = 9
                elif self.ending == "й" or self.declnum == 6 or self.declnum == 7:
                    self.stem =self.rustr[:-1]
                    if self.animated:
                        self.declnum = 4
                    else:
                        self.declnum = 5
                elif self.ending == "ь":
                    self.stem =self.rustr[:-1]
                    if self.animated:
                        self.declnum = 10
                    else:
                        self.declnum = 11
                elif self.ending == "и" or self.ending == "ы" and self.penul in self.morphs.reqi:
                    self.stem =self.rustr[:-1]
                    if self.animated:
                        self.declnum = 8
                    else:
                        self.declnum = 9
                elif self.ending == "и" or self.ending == "ы":
                    self.stem = self.rustr[:-1]
                    if self.animated:
                        self.declnum = 0
                    else:
                        self.declnum = 1
                elif self.rustr[-4:] == "анин" or self.rustr[-4:] == "янин":
                    self.stem =self.rustr[:-3]
                    self.declnum = 15
                elif self.rustr[-2:] == "ат" or self.rustr[-2:] == "ят":
                    self.stem =self.rustr[:-1]
                    self.declnum = 14
                else:
                    if self.ending == "и" or self.ending == "ы":
                        self.stem = self.rustr[:-1]
                    if self.animated:
                        self.declnum = 0
                    else:
                        self.delnum = 1
            elif self.singgender == "feminine":
                # Determine which declension to use.
                if self.declnum == 8:
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 14
                    else:
                        self.declnum = 15
                elif self.declnum == 9:
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 16
                    else:
                        self.declnum = 17
                elif self.declnum == 10:
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 18
                    else:
                        self.declnum = 19
                elif self.declnum == 12:
                    self.stem = self.rustr[:-2]
                    if self.animated:
                        self.declnum = 22
                    else:
                        self.declnum = 23
                elif self.ending == "ь":
                    if self.animated:
                        self.declnum = 6
                    else:
                        self.declnum = 7 
                elif self.ending == "а":
                    if self.penul in self.morphs.reqi:
                        if self.animated:
                            self.declnum = 2
                        else:
                            self.declnum = 3
                    else:
                        if self.animated:
                            self.declnum = 0
                        else:
                            self.declnum = 1
                elif self.ending == "я":
                    tmpstr = self.penul + self.ending
                    if tmpstr == "ия":
                        self.stem = self.rustr[:-2]
                        if self.animated:
                            self.declnum = 10
                        else:
                            self.declnum = 11
                    else:
                        if self.animated:
                            self.declnum = 8
                        else:
                            self.declnum = 9
                else:
                    if self.animated:
                        self.declnum = 0
                    else:
                        self.declnum = 1
            elif self.singgender == "nueter":
                if (self.declnum < 5):
                    self.stem = self.rustr[:-1]
                else:
                    self.stem = self.rustr[:-2]
                # Determine the declension to use.
                if self.declnum > 3:
                    self.stem = self.rustr[:-2]
                    self.declnum += 1
                elif self.ending == "o":
                    self.stem = self.rustr[:-1]
                    self.declnum = 0
                elif self.ending == "е":
                    self.stem = self.rustr[:-1]
                    self.declnum = 1
                elif self.rustr[-2:] == "мя":
                    self.stem = self.rustr[:-2]
                    self.declnum = 3
        self.gencheck = True
        self.stemEdit.setText(self.stem)

    def handlenums(self):
        self.stem = self.rustr
        if not self.rustr in self.numbers:
            answer = QMessageBox.question(self, "Numeric Test", "Is this word a number?", QMessageBox.Yes, QMessageBox.No)
            if answer == QMessageBox.Yes:
                self.numeric = True
                index = self.stem.find("ь")
                if self.rustr[-1] == "ь":
                    self.stem = self.rustr[:-1]
                    self.decltype = 5
                    self.declnum = 12
                    self.instrumental = self.stem + "ью"
                elif index < (len(self.stem) - 1) and index >= 0:
                    tmpstr = self.stem[:index]
                    index += 1
                    tmpstr += "и"
                    tmpstr += self.stem[index:]
                    self.oblique = tmpstr
                    self.instrumental = self.rustr
                    tmpstr = self.instrumental[:index]
                    tmpstr += "ю"
                    tmpstr += self.instrumental[index:]
                    tmpstr += "ью"
                    self.instrumental = tmpstr
                    self.decltype = 5
                    self.declnum = 12
                    if self.stem.endswith("сот"):
                        self.stem = self.stem[:-3]
                        self.oblique = self.oblique[:-3]
                        self.instrumental = self.instrumental[:-5] + "стами"
                        self.decltype = 3
                        self.declnum = 15
                else:
                    self.stem = self.rustr
                    self.instrumental = self.stem + "а"
                    self.decltype = 3
                    self.declnum = 12
            else:
                self.declnum = 0
                self.decltype = 3
        elif self.rustr in self.numbers:
            self.stem = self.rustr
            self.decltype = 3
            self.declnum = 16
    
    def createobj(self):
        """ Create an HTML table of noun declensions.
        """
        self.tableView.clear()
        # A class to draw the HTML table.
        if self.numeric and self.rustr[-1] == "ь":
            self.stem = self.rustr
            self.nomEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][1])
            self.accEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][2])
            self.stem = self.rustr[:-1]
        elif len(self.oblique) > 0:
            self.stem = self.rustr
            self.nomEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][1])
            self.accEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][2])
            self.stem = self.oblique
        elif self.decltype > 2:
            self.nomEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][1])
            self.accEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][2])
        else:
            self.nomEdit.setText(self.rustr)
            self.accEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][2])
        if (self.stem[-2:] == "нк" or self.stem[-2:] == "тк") and self.decltype == 5:
            tmpstem = self.stem
            self.stem = self.stem[:-1] + "ок"
            if self.animated:
                 self.accEdit.setText(self.stem)
                 self.genEdit.setText(self.stem)
            else:
                self.accEdit.setText(tmpstem + self.morphs.datalist[self.decltype][self.declnum][2])
                self.genEdit.setText(self.stem)
            self.stem = self.stem[:-2] + "к"
        elif self.stem[-3:] == "ньк" and self.decltype == 5:
            tmpstem = self.stem
            self.stem = self.stem[:-2] + "ек"
            if self.animated:
                 self.accEdit.setText(self.stem)
                 self.genEdit.setText(self.stem)
            else:
                self.accEdit.setText(tmpstem + self.morphs.datalist[self.decltype][self.declnum][2])
                self.genEdit.setText(self.stem)
            self.stem = self.stem[:-2] + "ьк"
        else:
            self.accEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][2])
            self.genEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][3])
        self.datEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][4])
        if self.numeric:
            self.insEdit.setText(self.instrumental)
        else:
            self.insEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][5])
        self.prpEdit.setText(self.stem + self.morphs.datalist[self.decltype][self.declnum][6])
        self.numeric = False
        tmptable = DeclTable(self.morphs.datalist[self.decltype][self.declnum][0] + " " + self.morphs.datalist[self.decltype][self.declnum][1], self.declnum)
        tmptable.addrow(self.morphs.datalist[self.decltype][self.declnum])
        tmpstr = tmptable.table()
        # Put the table in the GUI.
        self.tableView.clear()
        self.tableView.setHtml(tmpstr)
        
    def updatestem(self):
        self.stem = self.stemEdit.text()
        self.penul = self.stem[-1]
        self.createobj()
        return
    
    def finddecl(self):
        """ Open a gui to choose the noun's declension.
        """
        chooser = NounDeclSel(self)
        chooser.exec()
        self.chopend()
        if self.decltype == 0:
            self.singgender = "masculine"
        elif self.decltype == 1:
            self.singgender = "nueter"
        elif self.decltype == 2:
            self.singgender= "feminine"
        self.createobj()
        сhooser = None
        return
    
    def chopend(self):
        if self.decltype == 6 or self.decltype < 3:
            if self.decltype == 6 or self.morphs.datalist[self.decltype][self.declnum][0] == "Blank" or \
                (self.decltype == 0 and self.declnum == 0) or (self.decltype == 0 and self.declnum == 1) or\
                (self.decltype == 0 and self.declnum == 4) or (self.decltype == 0 and self.declnum == 5) or\
                (self.decltype == 0 and self.declnum == 8):
                self.stem = self.rustr
            elif (self.decltype == 0 and self.declnum > 12) or (self.decltype == 1 and self.declnum > 4) or \
                (self.decltype == 2 and self.declnum > 7) or (self.decltype == 3 and self.declnum > 15) or \
                (self.decltype == 4 and self.declnum > 4) or (self.decltype == 5 and self.declnum > 13) or \
                (self.decltype == 0 and self.declnum == 10) or (self.decltype == 0 and self.declnum == 11) or \
                (self.decltype == 1 and self.declnum == 2) or (self.decltype == 1 and self.declnum == 3) or \
                (self.decltype == 2 and self.declnum == 10) or (self.decltype == 2 and self.declnum == 11):
                self.stem = self.rustr[:-2]
            elif (self.decltype == 0 and self.declnum == 13):
                self.stem = self.rustr[:-3]
            else:
                self.stem = self.rustr[:-1]
            self.stemEdit.setText(self.stem)

    def accept(self):
        """ Gather the data and create an SQL command to insert it into the database.
            Close the GUI.
        """
        tmpstr = ""
        if self.decltype == 6:
            self.buttonstart = 105
            cursize = self.size()
            sizeevent = QResizeEvent(cursize, cursize)
            self.resizeEvent(sizeevent)
            self.wordlogic()
            self.createobj()
            return    
        animation = self.parent.sqldict['animate']
        variety = self.parent.sqldict['variety']
        typeval = self.parent.sqldict['type']
        self.rustr = self.parent.rustr
        self.enstr = self.enEdit.text()
        x = self.enstr
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        tmpstr = x
        if self.decltype > 2:
            genderstr = "plural"
        else:
            genderstr = self.singgender
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.nomEdit.text(), 'nominative', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.accEdit.text(), 'accusative', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.genEdit.text(), 'genitive', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.datEdit.text(), 'dative', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.insEdit.text(), 'instrumental', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list([variety, typeval, self.rustr, tmpstr, genderstr, self.prpEdit.text(), 'prepositional', animation])
        self.parent.declension.append(self.decllist)
        self.decllist = list()
        if self.decltype > 2:
            self.close()
            return
        self.decltype += 3 # Shifts everything to plural.
        self.buttonstart = 105
        cursize = self.size()
        sizeevent = QResizeEvent(cursize, cursize)
        self.resizeEvent(sizeevent)
        self.wordlogic()
        self.createobj()
        return

    def displayhelp(self):
        """ Display a help file in HTML format.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()
            
    def cancel(self):
        """ Cancel the event.
        """
        self.parent.cancel = True
        self.parent.declension = list()
        self.close()

    def closeEvent(self, event):
        """ Close the form and pass along GUI sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        