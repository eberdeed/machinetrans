#!/usr/bin/python3
"""
    PronounDecl:  Machine Translation Data Entry -- Russian Pronoun Declension Entry.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 1, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from machinetrans.userinterfaces.ui_pronoundecl import Ui_PronounDecl
from machinetrans.data.wordmorph import WordMorph
from machinetrans.data.wordtype import WordType
from machinetrans.dataentry.pronlist import PronList
from machinetrans.dataentry.pronadjsel import PronAdjSel
from machinetrans.helpview import HelpView

class PronounDecl(QDialog, Ui_PronounDecl):
    """ A GUI to enter Russian pronoun declensions.
    """
    pronounlist = True
    endings = list()
    animbool = False
    helpfile = "/usr/share/machinetrans/resources/pronoundecl.html"
    parent = None
    labeltext = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()
    morphs = None
    types = None
    decllist = list()
    decltype = 0
    declnum = 0
    rustr = ""
    enstr = ""
    stem = ""
    groupindex = 0
    singleindex = 0
    group = False
    # The declension name.
    pronname = "personal1a"
    prongender = list(["masculine", "feminine", "nueter", "plural"])
    genderindex = 1
    addall = False
    conjlist = list()
    itemlist = list()
    itemdict = dict()
    declensions = list(["nominative", "accusative", "genitive", "dative", "instrumental", "prepositional"])
    cancel = False
    pronountypes = list()
    def __init__(self, parent=None):
        """ Initialize the GUI and display the data for the pronoun "I".
        """
        super(PronounDecl, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.types = self.parent.types
        self.rustr = self.parent.rustr
        self.pronountypes = list(self.types.pronouns)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        ending = self.rustr[-2:]
        self.genderBox.setVisible(False)
        self.genderBox.setEnabled(False)
        self.mascanimrb.setVisible(False)
        self.mascanimrb.setEnabled(False)
        self.mascinanrb.setVisible(False)
        self.mascinanrb.setEnabled(False)
        self.femrb.setVisible(False)
        self.femrb.setEnabled(False)
        self.nuetrb.setVisible(False)
        self.nuetrb.setEnabled(False)
        self.pluranimrb.setVisible(False)
        self.pluranimrb.setEnabled(False)
        self.plurinanrb.setVisible(False)
        self.plurinanrb.setEnabled(False)
        self.typeDrop.clear()
        # Add the above lists to the dropdowns (QComboBoxes).
        self.typeDrop.addItems(self.pronountypes)
        # Connect the signals to their methods.
        self.typeDrop.currentIndexChanged.connect(self.typesel)
        self.mascanimrb.clicked.connect(self.mascanim)
        self.mascinanrb.clicked.connect(self.mascinan)
        self.femrb.clicked.connect(self.fem)
        self.nuetrb.clicked.connect(self.nuet)
        self.pluranimrb.clicked.connect(self.pluranim)
        self.plurinanrb.clicked.connect(self.plurinan)
        self.acceptBttn.clicked.connect(self.accept)
        self.endingBttn.clicked.connect(self.displayadj)
        self.singBttn.clicked.connect(self.singular)
        self.groupBttn.clicked.connect(self.groupval)
        self.pronBttn.clicked.connect(self.displaydata)
        self.rejectBttn.clicked.connect(self.cancelgui)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.stemEdit.firereturn.triggered.connect(self.chgstem)
        self.stemEdit.firefocus.triggered.connect(self.chgstem)
        self.endings = self.morphs.declension[self.decltype][self.declnum][:]
        self.stem = "мн"
        self.stemEdit.setText(self.stem)
        self.createdeclsingle()
                                        

    def setTitle(self):
        """ Set the title to the current pronoun.
        """
        tmpstr = "Russian Pronoun Declension For " + self.rustr.capitalize()
        self.titleLbl.setText(tmpstr)

    def resizeEvent(self, event):
        """ Resize the form and record sizing information.
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
        self.titleLbl.setGeometry(10, 10, tmpwidth, 30)
        tmpy = 70 * hscale
        self.genderBox.setGeometry(10, tmpy, tmpwidth, 80)
        tmpy = 20
        self.mascanimrb.setGeometry(10, tmpy, 250, 25)
        tmpx = (self.width1 / 2) - 120
        self.mascinanrb.setGeometry(tmpx, tmpy, 250, 25)
        tmpx = self.width1 - 180
        self.femrb.setGeometry(tmpx, tmpy, 130, 25)
        tmpy = 50
        tmpx = 20
        self.nuetrb.setGeometry(tmpx, tmpy, 150, 25)
        tmpx = (self.width1 / 2) - 120
        self.pluranimrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = self.width1 - 250
        self.plurinanrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpy = hscale * 170
        tmpx = (self.width1 - 720) / 2
        self.typeLbl.setGeometry(tmpx, tmpy, 180, 30)
        tmpy = hscale * 200
        self.typeDrop.setGeometry(tmpx, tmpy, 180, 35)
        tmpx = (self.width1 / 2) - 160
        self.enLbl.setGeometry(tmpx, tmpy, 130, 25)
        tmpx = (self.width1 / 2) + 30        
        self.enEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 240 * hscale
        tmpx = (self.width1 - 740) / 2
        self.stemLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.stemEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 280 * hscale
        tmpx = (self.width1 - 740) / 2
        self.nomLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.accLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.nomEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.accEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 - 740) / 2
        tmpy = hscale * 350
        self.genLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.datLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.genEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.datEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 420 * hscale
        tmpx = (self.width1 - 740) / 2
        self.insLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.prpLbl.setGeometry(tmpx, tmpy, 340, 30)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2
        self.insEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpx = (self.width1 / 2) + 30        
        self.prpEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = self.height1 - (120 * hscale)
        tmpx = (self.width1 - 540) / 2
        self.singBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + 120
        self.groupBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 740) / 2
        self.rejectBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += 200
        self.endingBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1) / 2 + 20
        self.pronBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += 200
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
    
    def addallpronouns(self):
        """ Use the WordMorphs class to store a list of all 
            Russian pronouns and their declensions.
            A series of SQL commands is created to add 
            all the data to the database.
        """
        self.parent.sqlcommand = ""
        basecommand = "INSERT INTO pronouns "
        for x in self.morphs.singlekeys:
            tmplist = self.morphs.pronouns[x]
            self.enstr = tmplist[0]
            self.rustr = tmplist[1]
            self.itemdict = dict()
            self.itemdict["name"] = self.apostrophe(self.enstr)
            self.itemdict["runame"] = self.rustr
            self.conjlist = tmplist[1:7]
            self.itemdict["variety"] = tmplist[7]
            self.itemdict["gender"] = "masculine"
            self.itemdict["animate"] = "animate"
            for x in range(len(self.conjlist)):
                cols = "("
                data = "("
                for y in self.itemdict:
                    cols += y + ", "
                    data += "\'" + self.itemdict[y] + "\', "
                cols += "wordcase, "
                data += "\'" + self.declensions[x] + "\', "
                cols += "declension) VALUES"
                data += "\'" + self.conjlist[x] + "\');\n"
                if len(self.conjlist[x]) > 0:
                    self.parent.sqlcommand += basecommand + cols + data
                else:
                    print("\n\nError on pronoun add.\n\n")
        for x in self.morphs.groupkeys:
            grouplist = self.morphs.pronouns[x].copy()
            for y in range(6):
                tmplist = grouplist[y]
                self.enstr = tmplist[0]
                self.rustr = tmplist[1]
                self.itemdict = dict()
                self.itemdict["name"] = self.apostrophe(self.enstr)
                self.itemdict["runame"] = self.rustr
                self.conjlist = tmplist[1:7]
                self.itemdict["variety"] = grouplist[6]
                if y == 0:
                    self.itemdict["gender"] = "masculine"
                    self.itemdict["animate"] = "animate"
                elif y == 1:
                    self.itemdict["gender"] = "masculine"
                    self.itemdict["animate"] = "inanimate"
                elif y == 2:
                    self.itemdict["gender"] = "feminine"
                    self.itemdict["animate"] = "inanimate"
                elif y == 3:
                    self.itemdict["gender"] = "nueter"
                    self.itemdict["animate"] = "inanimate"
                elif y == 4:
                    self.itemdict["gender"] = "plural"
                    self.itemdict["animate"] = "animate"
                else:
                    self.itemdict["gender"] = "plural"
                    self.itemdict["animate"] = "inanimate"
                for x in range(6):
                    cols = "("
                    data = "("
                    for y in self.itemdict:
                        cols += y + ", "
                        data += "\'" + self.itemdict[y] + "\', "
                    cols += "wordcase, "
                    data += "\'" + self.declensions[x] + "\', "
                    cols += "declension) VALUES"
                    data += "\'" + self.conjlist[x] + "\');\n"
                    self.parent.sqlcommand += basecommand + cols + data
                
        self.parent.cancel = False
        self.close()
        
    def createdeclsingle(self):
        """ Add the selected single pronoun declension to the Line Editors on the form.
        """
        tmpstr = self.morphs.singlekeys[self.singleindex]
        self.itemlist = list(self.morphs.pronouns[tmpstr])
        self.enstr = self.itemlist[0]
        self.rustr = self.itemlist[1]
        self.setTitle()
        self.conjlist = self.itemlist[1:7]
        self.nomEdit.setText(self.conjlist[0])
        self.accEdit.setText(self.conjlist[1])
        self.genEdit.setText(self.conjlist[2])
        self.datEdit.setText(self.conjlist[3])
        self.insEdit.setText(self.conjlist[4])
        self.prpEdit.setText(self.conjlist[5])
        index = self.pronountypes.index(self.itemlist[7])
        self.typeDrop.setCurrentIndex(index)
        self.enEdit.setText(self.enstr)
        if index != self.pronountypes.index("personal"):
            tmpstr = self.rustr[:-1]
        else:
            tmpstr = self.rustr
        self.stemEdit.setText(tmpstr)
    
    def createdeclgroup(self):
        """ Add the selected group pronoun declension to the Line Editors on the form.
        """
        self.itemlist = list()
        tmpstr = self.morphs.groupkeys[self.groupindex]
        prongroup = self.morphs.pronouns[tmpstr]
        for x in range(6):
            tmplist = list(prongroup[x])
            tmplist.pop(0)
            self.itemlist.append(tmplist)
        index = self.pronountypes.index(prongroup[6])
        self.typeDrop.setCurrentIndex(index)
        self.enstr = prongroup[0][0]
        self.enEdit.setText(self.enstr)
        self.rustr = prongroup[0][1]
        tmpstr = self.rustr[:-2]
        self.stemEdit.setText(tmpstr)
    
    def createdecladj(self):
        """ Create a group pronoun with a given adjectival ending as
            selected by the calling method.
        """
        self.stem = self.stemEdit.text()
        endinggroup = self.morphs.declension[self.decltype].copy()
        self.itemlist.clear()
        for x in range(6):
            conjlist = list()
            for z in range(1, 7):
                y = endinggroup[x][z]
                conjlist.append(self.stem + y)
            self.itemlist.append(conjlist)
                
        
    def mascanim(self):
        """  Select the masculine animate gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 0
        self.drawpronouns()

    def mascinan(self):
        """  Select the masculine inanimate gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 1
        self.drawpronouns()

    def fem(self):
        """  Select the feminine gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 2
        self.drawpronouns()

    def nuet(self):
        """  Select the nueter gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 3
        self.drawpronouns()

    def pluranim(self):
        """  Select the plural animate gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 4
        self.drawpronouns()

    def plurinan(self):
        """  Select the plural inanimate gender and display it.
        """
        self.recordpronouns()
        self.genderindex = 5
        self.drawpronouns()

    def singular(self):
        """ Select the single pronoun mode and display a pronoun.
        """
        self.group = False
        self.pronounlist = False
        self.displaydata()
        
    def groupval(self):
        """ Select the group pronoun mode and display a gender of the group.
        """
        self.group = True
        self.pronounlist = False
        self.displaydata()
        
    def displaydata(self):
        """ Either get a value from the pronoun list and display it, or
            display an existing value in either single or group mode
            based one the "group" boolean variable.
        """
        if self.pronounlist:
            pronlist = PronList(self)
            pronlist.activateWindow()
            pronlist.exec()
            if self.addall:
                self.addallpronouns()
                return
        if self.cancel:
            self.cancelgui()
        if self.group:
            self.genderBox.setVisible(True)
            self.genderBox.setEnabled(True)
            self.mascanimrb.setVisible(True)
            self.mascanimrb.setEnabled(True)
            self.mascinanrb.setVisible(True)
            self.mascinanrb.setEnabled(True)
            self.femrb.setVisible(True)
            self.femrb.setEnabled(True)
            self.nuetrb.setVisible(True)
            self.nuetrb.setEnabled(True)
            self.pluranimrb.setVisible(True)
            self.pluranimrb.setEnabled(True)
            self.plurinanrb.setVisible(True)
            self.plurinanrb.setEnabled(True)
            self.createdeclgroup()
            self.drawpronouns()
        else:
            self.genderBox.setVisible(False)
            self.genderBox.setEnabled(False)
            self.mascanimrb.setVisible(False)
            self.mascanimrb.setEnabled(False)
            self.mascinanrb.setVisible(False)
            self.mascinanrb.setEnabled(False)
            self.femrb.setVisible(False)
            self.femrb.setEnabled(False)
            self.nuetrb.setVisible(False)
            self.nuetrb.setEnabled(False)
            self.pluranimrb.setVisible(False)
            self.pluranimrb.setEnabled(False)
            self.plurinanrb.setVisible(False)
            self.plurinanrb.setEnabled(False)
            self.createdeclsingle()
        self.pronounlist = True
        
    def displayadj(self):
        """ Get an adjectival family of endings and add it
            to the existing stem and display it.
        """
        adjgui = PronAdjSel(self)
        adjgui.exec()
        if not self.genderBox.isEnabled():
            self.genderBox.setVisible(True)
            self.genderBox.setEnabled(True)
            self.mascanimrb.setVisible(True)
            self.mascanimrb.setEnabled(True)
            self.mascinanrb.setVisible(True)
            self.mascinanrb.setEnabled(True)
            self.femrb.setVisible(True)
            self.femrb.setEnabled(True)
            self.nuetrb.setVisible(True)
            self.nuetrb.setEnabled(True)
            self.pluranimrb.setVisible(True)
            self.pluranimrb.setEnabled(True)
            self.plurinanrb.setVisible(True)
            self.plurinanrb.setEnabled(True)
        self.endings = self.morphs.declension[self.decltype][1]
        self.mascinanrb.setChecked(True)
        self.createdecladj()
        self.drawpronouns()

        
    def chgstem(self):
        """ Change the stem and reset all the values to 
            include this stem as the root of the pronoun.
        """
        self.stem = self.stemEdit.text()
        self.createdecladj()
        self.drawpronouns()
    
    def recordpronouns(self):
        """ Get the current values from the line editors for the 
            pronoun being edited.
        """
        self.itemlist[self.genderindex][0] = self.nomEdit.text()
        self.itemlist[self.genderindex][1] = self.accEdit.text()
        self.itemlist[self.genderindex][2] = self.genEdit.text()
        self.itemlist[self.genderindex][3] = self.datEdit.text()
        self.itemlist[self.genderindex][4] = self.insEdit.text()
        self.itemlist[self.genderindex][5] = self.prpEdit.text()

            
    def drawpronouns(self):
        """ Place the values in the line editors.
        """
        self.nomEdit.setText(self.itemlist[self.genderindex][0])
        self.accEdit.setText(self.itemlist[self.genderindex][1])
        self.genEdit.setText(self.itemlist[self.genderindex][2])
        self.datEdit.setText(self.itemlist[self.genderindex][3])
        self.insEdit.setText(self.itemlist[self.genderindex][4])
        self.prpEdit.setText(self.itemlist[self.genderindex][5])
            
    def typesel(self):
        """ Use a drop down to select the pronoun type.
        """
        index = self.typeDrop.currentIndex()
        self.itemdict["variety"] = self.pronountypes[index]
    
    def accept(self):
        """ Gather the data from the GUI and 
            create a the SQL commands to insert 
            the given pronoun and its declensions 
            into the database.
        """
        self.parent.cancel = False
        self.itemdict.clear()
        basecommand = "INSERT INTO pronouns "
        self.parent.sqlcommand = ""
        if not self.group:
            decltxt = list()
            decltxt.append(self.nomEdit.text())
            decltxt.append(self.accEdit.text())
            decltxt.append(self.genEdit.text())
            decltxt.append(self.datEdit.text())
            decltxt.append(self.insEdit.text())
            decltxt.append(self.prpEdit.text())
            self.itemdict["name"] = self.apostrophe(self.enEdit.text())
            self.itemdict["runame"] = self.nomEdit.text()
            self.itemdict["gender"] = "masculine"
            self.itemdict["animate"] = "animate"
            index = self.typeDrop.currentIndex()
            self.itemdict["variety"] = self.pronountypes[index]
            for x in range(len(decltxt)):
                cols = "("
                data = "("
                for y in self.itemdict:
                    cols += y + ", "
                    data += "\'" + self.itemdict[y] + "\', "
                cols += "wordcase, "
                data += "\'" + self.declensions[x] + "\', "
                cols += "declension) VALUES"
                data += "\'" + decltxt[x] + "\');\n"
                self.parent.sqlcommand += basecommand + cols + data
            self.close()
        else:
            self.recordpronouns()
            self.itemdict["name"] = self.apostrophe(self.enEdit.text())
            self.itemdict["runame"] = self.itemlist[0][0]
            for x in range(6):
                if x == 0:
                    self.itemdict["gender"] = "masculine"
                    self.itemdict["animate"] = "animate"
                elif x == 1:
                    self.itemdict["gender"] = "masculine"
                    self.itemdict["animate"] = "inanimate"
                elif x == 2:
                    self.itemdict["gender"] = "feminine"
                    self.itemdict["animate"] = "inanimate"
                elif x == 3:
                    self.itemdict["gender"] = "nueter"
                    self.itemdict["animate"] = "inanimate"
                elif x == 4:
                    self.itemdict["gender"] = "plural"
                    self.itemdict["animate"] = "animate"
                else:
                    self.itemdict["gender"] = "plural"
                    self.itemdict["animate"] = "inanimate"
                for y in range(6):
                    cols = "("
                    data = "("
                    for z in self.itemdict:
                        cols += z + ", "
                        data += "\'" + self.itemdict[z] + "\', "
                    cols += "wordcase, "
                    data += "\'" + self.declensions[y] + "\', "
                    cols += "declension) VALUES"
                    data += "\'" + self.itemlist[x][y] + "\');\n"
                    self.parent.sqlcommand += basecommand + cols + data
        self.close()
            
    def apostrophe(self, x):
        """ For each English word with an apostrophe echo
            with another apostrophe '' so that it will appear
            in the database.
        """
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        return x

    def displayhelp(self):
        """ Create an HTML help file for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def cancelgui(self):
        """ Cancel the event.
        """
        self.parent.cancel = True
        self.parent.declension = list()
        self.close()

    def closeEvent(self, event):
        """ Close the GUI and pass along sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        