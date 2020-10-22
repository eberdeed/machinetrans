#!/usr/bin/python3
"""
    VerbConjugation:  Machine Translation Data Entry -- Russian Verb Conjugation Data Entry.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    June 29, 2016, San Diego California United States of America
"""
import os, sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_verbconjugation import Ui_VerbConjugation
from machinetrans.data.wordmorph import WordMorph
from machinetrans.data.wordtype import WordType
from machinetrans.dataentry.verbconjsel import VerbConjSel
from machinetrans.helpview import HelpView

class VerbConjugation(QDialog, Ui_VerbConjugation):
    """ A GUI to enter Russian-English language verb data into
        a PostgreSQL database.  This is the first in a series
        of GUIs for verb conjugation.
    """
    
    helpfile = "/usr/share/machinetrans/resources/verbconjugation.html"
    parent = None
    labeltext = ""
    rustr = ""
    enstr = ""
    stem = None
    reflexive = False
    oneself = False
    imperfective = True
    cancel = False
    sqlcommand = ""
    basecommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    index = 0
    simpleconj = dict()
    geometry = list()    
    morphs = None
    types = None
    conjlist = list()
    vowels = list(["a", "e", "i", "o", "u"])
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the Russian
            verb conjugation.  Do some selection
            of the conjugation to be used.
        """
        super(VerbConjugation, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.types = self.parent.types
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        # Detect an imperfective verb.
        if not self.parent.verbpages[0]:
            self.simpleconj.clear()
        else:
            self.simpleconj = self.parent.verbdict["page1"].copy()
            del self.parent.verbdict["page1"]
        self.imperfective = self.parent.sqldict["imperfective"] == "\'imperfective\'"
        # Display the proper labelf for the English verb.
        self.labeltext = "Verb Conjugation for \n" + \
            self.enstr + " " + self.parent.tense
        tmplist = self.labeltext.split()
        self.labeltext = ""
        # Capitalize the whole label except "for."
        for x in tmplist:
            if x != "for":
                x = x.capitalize()
            else:
                x += "\n"
            self.labeltext += x + " "
        self.titleLbl.setText(self.labeltext)
        # Display the label for the Russian verb.
        self.labeltext = "Verb Conjugation for \n" + \
            self.parent.rustr + " " + self.parent.tense
        tmplist = self.labeltext.split()
        self.labeltext = ""
        # Capitalize the label except for the word "for."
        for x in tmplist:
            if x != "for":
                x = x.capitalize()
            else:
                x += "\n"
            self.labeltext += x + " "
        self.titleLblru.setText(self.labeltext)
        self.basecommand = self.parent.sqlcommand
        self.parent.sqlcommand = ""
        # Connect the buttons and check boxes.
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.passdata)
        self.recBttn.clicked.connect(self.eraseall)
        self.stemEdit.firereturn.triggered.connect(self.changeconj)
        self.stemEdit.firefocus.triggered.connect(self.changeconj)
        self.enVerbEdit.firereturn.triggered.connect(self.changeeng)
        self.enVerbEdit.firefocus.triggered.connect(self.changeeng)
        self.ruVerbEdit.firereturn.triggered.connect(self.changeruss)
        self.ruVerbEdit.firefocus.triggered.connect(self.changeruss)
        self.selfCheck.clicked.connect(self.myself)
        self.conjBttn.clicked.connect(self.verbconj)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.firstEdit.setFocus()
        self.caseBox.addItems(self.types.objcase)
        self.caseBox.setCurrentIndex(6)
        self.selfCheck.setChecked(False)
        self.enVerbEdit.setText(self.enstr)
        self.ruVerbEdit.setText(self.rustr)
        # Check to see if the Russian verb is reflexive.
        if self.parent.verbpages[0]:
            self.firstEditru.setText(self.simpleconj["first"]["conjugationru"].strip("\'"))
            self.secondEditru.setText(self.simpleconj["second"]["conjugationru"].strip("\'"))
            self.thirdEditru.setText(self.simpleconj["third"]["conjugationru"].strip("\'"))
            self.firstpEditru.setText(self.simpleconj["plural first"]["conjugationru"].strip("\'"))
            self.secondpEditru.setText(self.simpleconj["plural second"]["conjugationru"].strip("\'"))
            self.thirdpEditru.setText(self.simpleconj["plural third"]["conjugationru"].strip("\'"))
            self.firstEdit.setText(self.simpleconj["first"]["conjugation"].strip("\'"))
            self.secondEdit.setText(self.simpleconj["second"]["conjugation"].strip("\'"))
            self.thirdEdit.setText(self.simpleconj["third"]["conjugation"].strip("\'"))
            self.firstpEdit.setText(self.simpleconj["plural first"]["conjugation"].strip("\'"))
            self.thirdpEdit.setText(self.simpleconj["plural third"]["conjugation"].strip("\'"))
            self.stemEdit.setText(self.simpleconj["stem"])
            index = self.types.objcase.index(self.simpleconj["first"]["objcase"].strip("\'"))
            self.caseBox.setCurrentIndex(index)
            return
        else:
            self.ruconj()
            
    def ruconj(self):
        ending = self.rustr[-2:]
        if ending == "ся" or ending == "сь":
            self.reflexive = True
            self.oneself = True
            self.parent.oneself = True
            self.selfCheck.setChecked(True)
            self.rustr = self.rustr[: -2]
            self.caseBox.setCurrentIndex(6)
        self.engconj()
        # Check to see which conjugation to display.
        ending = self.rustr[-5:]
        if ending == "овать" or ending == "евать":
            self.index = 16
            self.conjugate()
            return
        ending = self.rustr[-3:]
        if ending == "ать":
            self.index = 0
        elif ending == "ять":
            self.index = 1
        elif ending == "гать":
            self.index = 5
        elif ending == "ить":
            self.index = 6
        elif ending == "еть":
            self.index = 10
        elif ending == "сти":
            self.index = 11
        elif ending == "зти":
            self.index = 12
        elif ending[-1] == "и":
            self.index = 10
        elif ending == "ыть":
            self.index = 17
        else:
            # We fail, you get conjugation 3.
            self.index = 2
        self.conjugate()
        self.parent.verbpages[0] = True
        
    def resizeEvent(self, event):
        """ Resize the GUI and record GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 / 600
        wscale = self.width1 / 800
        tmpy = 0
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 10, tmpwidth, 40)
        tmpx = (self.width1 - 560) /2
        tmpy = 50 * hscale
        self.selfCheck.setGeometry(tmpx, tmpy, 130, 25)
        tmpx += 150
        self.enVerbLbl.setGeometry(tmpx, tmpy, 170, 25)
        tmpx = (self.width1 / 2) - 70
        self.enVerbEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 80 * hscale
        tmpx = (self.width1 - 700) / 2
        self.firstLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 14
        self.secondLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy += 20
        self.firstEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 14
        self.secondEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 700) / 2
        tmpy = 130 * hscale
        self.thirdLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 14
        self.firstpLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 20
        tmpx = (self.width1 - 700) / 2
        self.thirdEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 14
        self.firstpEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 180 * hscale
        tmpx = (self.width1 - 700) / 2
        self.thirdpLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 20
        self.thirdpEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 190 * hscale
        tmpx = (self.width1 / 2) + 14
        self.recLbl.setGeometry(tmpx, tmpy, 200, 50)
        tmpx += 210
        self.recBttn.setGeometry(tmpx,tmpy, 150, 50)
        tmpy = 240 * hscale
        self.titleLblru.setGeometry(10, tmpy, tmpwidth, 40)
        tmpx = (self.width1 - 560) /2
        tmpy = 280 * hscale
        self.ruVerbLbl.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = (self.width1 / 2) - 50
        self.ruVerbEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 560) /2
        tmpy = 310 * hscale
        self.caseLbl.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = (self.width1 / 2) - 50
        self.caseBox.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 560) /2
        tmpy = 340 * hscale
        self.stemLbl.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = (self.width1 / 2) - 50
        self.stemEdit.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy = 370 * hscale
        tmpint = ((220 * hscale) / 3) - 30
        self.firstLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 14
        self.secondLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy += 20
        self.firstEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 14
        self.secondEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 700) / 2
        tmpy = 420 * hscale
        self.thirdLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 14
        self.firstpLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy += 20
        self.thirdEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 14
        self.firstpEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 470 * hscale
        tmpx = (self.width1 - 700) / 2
        self.secondpLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 14
        self.thirdpLblru.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy += 20
        self.secondpEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 14
        self.thirdpEditru.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = self.height1 - 70
        tmpx = (self.width1 - 620) / 2
        self.cancelBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 - 180) / 2
        self.conjBttn.setGeometry(tmpx, tmpy, 180, 50)
        tmpx = self.width1 - (((self.width1 - 620) / 2) + 150)
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
    
    def changeeng(self):
        """ Change the English value.
        """
        self.enstr = self.enVerbEdit.text()
        self.parent.enstr = self.enstr
        self.parent.sqldict["name"] = self.enstr
        self.engconj()
        
    def changeruss(self):
        """ Change the Russian value.
        """
        self.rustr = self.ruVerbEdit.text()
        self.parent.rustr = self.rustr
        self.parent.sqldict["runame"] = self.rustr
        self.ruconj()
        
    def eraseall(self):
        """ Reset the data cache "verbdict" so the data
            can be re-entered.
        """
        self.parent.verbdict.clear()
        self.simpleconj.clear()
        self.parent.verbpages = list([False, False, False, False])
        self.ruconj()
        
    def verbconj(self):
        """ Display a listing of all verb conjugations.
            Once one is selected, return to this GUI
            and display it.
        """
        self.cancel = False
        conj = VerbConjSel(self)
        conj.exec()
        if self.cancel:
            return
        else:
            self.conjugate()
                
    def changeconj(self):
        """ Change the stem for the conjugation
            and propagate it out to the Q
            LineEditors.
        """
        self.stem = self.stemEdit.text()
        self.conjugate()
        
    def engconj(self):
        """ Conjugate the English forms of the
            given verb.
        """
        if self.enstr[:6] == "to be ":
            self.tobeeng()
            return
        if self.enstr[:8] == "to have ":
            self.tohaveeng()
            return
        if self.enstr[:3] == "to ":
            tmpstr = self.enstr[3:]
        else:
            tmpstr = self.enstr
        if tmpstr.endswith(" oneself"):
            tmpstr = tmpstr[:-8]
        tmpstr = tmpstr.strip()
        tmpstr1 = tmpstr
        if self.imperfective:
            if self.oneself:
                self.firstEdit.setText(tmpstr + " myself")
                self.secondEdit.setText(tmpstr + " yourself")
                original = tmpstr
                index = tmpstr.find(" ")        
                if index > 0:
                    tmpstr1 = tmpstr[:index]
                    tmpstr2 = tmpstr[index:]
                    ending = tmpstr1[-1]
                    penul = tmpstr1[-2]
                    if ending == 'y' and not penul in self.vowels:
                        tmpstr1 = tmpstr[:-1]
                        tmpstr1 += "ies"
                    elif penul == "s" and ending == "h":
                        tmpstr1 += "es"
                    elif ending == "s":
                        tmpstr1 += "es"
                    else:
                        tmpstr1 += "s"
                    tmpstr1 += tmpstr2
                    self.thirdEdit.setText(tmpstr1 + " himself")
                else:
                    ending = tmpstr[-1]
                    penul = tmpstr[-2]
                    if ending == 'y' and not penul in self.vowels:
                        tmpstr = tmpstr[:-1]
                        tmpstr += "ies"
                    elif penul == "s" and ending == "h":
                        tmpstr += "es"
                    elif ending == "s":
                        tmpstr += "es"
                    else:
                        tmpstr += "s"
                    self.thirdEdit.setText(tmpstr + " himself")
                tmpstr = original
                self.firstpEdit.setText(tmpstr + " ourselves")
                self.thirdpEdit.setText(tmpstr + " themselves")
            else:
                self.firstEdit.setText(tmpstr)
                self.secondEdit.setText(tmpstr)
                original = tmpstr
                index = tmpstr.find(" ")        
                if index > 0:
                    tmpstr1 = tmpstr[:index]
                    tmpstr2 = tmpstr[index:]
                    ending = tmpstr1[-1]
                    penul = tmpstr1[-2]
                    if ending == 'y' and not penul in self.vowels:
                        tmpstr1 = tmpstr1[:-1]
                        tmpstr1 += "ies"
                    elif ending == "s":
                        tmpstr1 += "es"
                    else:
                        tmpstr1 += "s"
                    tmpstr1 += tmpstr2
                    self.thirdEdit.setText(tmpstr1)
                else:
                    ending = tmpstr[-1]
                    penul = tmpstr[-2]
                    if ending == 'y' and not penul in self.vowels:
                        tmpstr = tmpstr[:-1]
                        tmpstr += "ies"
                    elif ending == "s":
                        tmpstr += "es"
                    else:
                        tmpstr += "s"
                    self.thirdEdit.setText(tmpstr)
                tmpstr = original
                self.firstpEdit.setText(tmpstr)
                self.thirdpEdit.setText(tmpstr)
        else:
            if self.oneself:
                self.firstEdit.setText("will " + tmpstr + " myself")
                self.secondEdit.setText("will " + tmpstr + " yourself")
                self.thirdEdit.setText("will " + tmpstr1 + " himself")
                self.firstpEdit.setText("will " + tmpstr + " ourselves")
                self.thirdpEdit.setText("will " + tmpstr + " themselves")
            else:
                self.firstEdit.setText("will " + tmpstr)
                self.secondEdit.setText("will " + tmpstr)
                self.thirdEdit.setText("will " + tmpstr1)
                self.firstpEdit.setText("will " + tmpstr)
                self.thirdpEdit.setText("will " + tmpstr)
            
    def tobeeng(self):
        """ Conjugate an English verb preceded by "to be."
        """
        verb = self.enstr[6:]
        prep = None
        if verb.endswith(" by oneself") or verb.endswith(" to oneself"):
            self.oneself = True
            prep = verb[-11:-8]
            verb = verb[:-11]
        if self.oneself:
            if prep:
                self.firstEdit.setText("am " + verb + prep + " myself")
                self.secondEdit.setText("are " + verb + prep + " yourself")
                self.thirdEdit.setText("is " + verb + prep + " himself")
                self.firstpEdit.setText("are " + verb + prep + " ourselves")
                self.thirdpEdit.setText("are " + verb + prep + " themselves")
            else:
                self.firstEdit.setText("am " + verb + " myself")
                self.secondEdit.setText("are " + verb + " yourself")
                self.thirdEdit.setText("is " + verb + " himself")
                self.firstpEdit.setText("are " + verb + " ourselves")
                self.thirdpEdit.setText("are " + verb + " themselves")
        else:        
            self.firstEdit.setText("am " + verb)
            self.secondEdit.setText("are " + verb)
            self.thirdEdit.setText("is " + verb)
            self.firstpEdit.setText("are " + verb)
            self.thirdpEdit.setText("are " + verb)

    def tohaveeng(self):
        """ Conjugate an English verb preceded by "to have."
        """
        verb = self.enstr[8:]
        prep = None
        if verb.endswith(" by oneself") or verb.endswith(" to oneself"):
            self.oneself = True
            prep = verb[-11:-8]
            verb = verb[:-11]
        if self.oneself:
            if prep:
                self.firstEdit.setText("have " + verb + prep + " myself")
                self.secondEdit.setText("have " + verb + prep + " yourself")
                self.thirdEdit.setText("has " + verb + prep + " himself")
                self.firstpEdit.setText("have " + verb + prep + " ourselves")
                self.thirdpEdit.setText("have " + verb + prep + " themselves")
            else:
                self.firstEdit.setText("have " + verb + " myself")
                self.secondEdit.setText("have " + verb + " yourself")
                self.thirdEdit.setText("has " + verb + " himself")
                self.firstpEdit.setText("have " + verb + " ourselves")
                self.thirdpEdit.setText("have " + verb + " themselves")
        else:        
            self.firstEdit.setText("have " + verb)
            self.secondEdit.setText("have " + verb)
            self.thirdEdit.setText("has " + verb)
            self.firstpEdit.setText("have " + verb)
            self.thirdpEdit.setText("have " + verb)
    
    def conjugate(self):
        """ Verb conjugation displayed.
        """
        self.conjlist = list()
        if self.stem:
            tmpstr = self.stem
        elif self.index == 5:
            tmpstr = self.rustr[:-4]
        elif self.index == 10:
            tmpstr = self.rustr[:-2]
        elif self.index == 11 or self.index == 12:
            tmpstr = self.rustr[:-2]
        elif self.index == 16:
            tmpstr = self.rustr[:-5]
        else:
            tmpstr = self.rustr[: -3]
        self.stemEdit.setText(tmpstr)
        for y in range(1, 7):
            x = self.morphs.conjugations[self.index][y]
            self.conjlist.append(tmpstr + x)
        self.createconj()
        
    def createconj(self):
        """ Put the declension on the GUI.
        """
        if self.reflexive:
            self.conjlist[0] += "сь"
            self.conjlist[1] += "ся"
            self.conjlist[2] += "ся"
            self.conjlist[3] += "ся"
            self.conjlist[4] += "сь"
            self.conjlist[5] += "ся"
        self.firstEditru.setText(self.conjlist[0])
        self.secondEditru.setText(self.conjlist[1])
        self.thirdEditru.setText(self.conjlist[2])
        self.firstpEditru.setText(self.conjlist[3])
        self.secondpEditru.setText(self.conjlist[4])
        self.thirdpEditru.setText(self.conjlist[5])
    
    def myself(self):
        """ Toggle the English reflexive or not.
            Some Russian reflexives do not require
            an English "yourself" for example
            "to hope" "надеяться"
        """
        if self.oneself:
            self.oneself = False
            self.parent.oneself = False
            self.selfCheck.setChecked(False)
        else:
            self.oneself = True
            self.parent.oneself = True
            self.selfCheck.setChecked(True)
        self.engconj()
    
    def passdata(self):
        """ Gather the data and create a series of SQL
            commands to insert the data into the database.
        """
        tmpstr = ""
        self.parent.sqldict["objcase"] = "\'" + self.types.objcase[self.caseBox.currentIndex()] + "\'"
        lineitem = self.parent.sqldict.copy()
        x = lineitem["name"]
        x = x.strip('\'')
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["name"] = '\'' + x + '\''
        self.parent.sqldict["name"] = '\'' + x + '\''
        if self.reflexive:
            self.rustr += "ся"
        lineitem["runame"] = "\'" + self.rustr + "\'"
        self.parent.sqldict["runame"] = "\'" + self.rustr + "\'"
        lineitem["tense"] = "\'simple present\'"
        self.parent.sqldict["tense"] = "\'simple present\'"
        lineitem["person"] = "\'first\'"
        x = self.firstEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"    
        lineitem["conjugationru"] = "\'" + self.firstEditru.text() + "\'"
        self.simpleconj["first"] = lineitem.copy()
        lineitem.clear()
        lineitem = self.parent.sqldict.copy()
        lineitem["person"] = "\'second\'"
        x = self.secondEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"
        lineitem["conjugationru"] = "\'" + self.secondEditru.text() + "\'"
        self.simpleconj["second"] = lineitem.copy()
        lineitem.clear()
        lineitem = self.parent.sqldict.copy()
        lineitem["person"] = "\'third\'"
        x = self.thirdEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"
        lineitem["conjugationru"] = "\'" + self.thirdEditru.text() + "\'"
        self.simpleconj["third"] = lineitem.copy()
        lineitem.clear()
        lineitem = self.parent.sqldict.copy()
        lineitem["person"] = "\'plural first\'"
        x = self.firstpEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"
        lineitem["conjugationru"] = "\'" + self.firstpEditru.text() + "\'"
        self.simpleconj["plural first"] = lineitem.copy()
        lineitem.clear()
        lineitem = self.parent.sqldict.copy()
        lineitem["person"] = "\'plural second\'"
        x = self.secondEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"
        lineitem["conjugationru"] = "\'" + self.secondpEditru.text() + "\'"
        self.simpleconj["plural second"] = lineitem.copy()
        lineitem.clear()
        lineitem = self.parent.sqldict.copy()
        lineitem["person"] = "\'plural third\'"
        x = self.thirdpEdit.text()
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        lineitem["conjugation"] = "\'" + x + "\'"
        lineitem["conjugationru"] = "\'" + self.thirdpEditru.text() + "\'"
        self.simpleconj["plural third"] = lineitem.copy()
        lineitem.clear()
        self.simpleconj["stem"] = self.stemEdit.text()
        self.parent.presstem = self.stemEdit.text()
        self.parent.firstpersonsingular = self.firstEditru.text()
        self.parent.thirdpersonplural = self.thirdpEditru.text()
        if self.parent.sqldict["imperfective"] == "\'imperfective\'":
            self.parent.thirdpersonplural = self.thirdpEditru.text()
            self.parent.firstpersonplural = self.firstpEditru.text()
        self.parent.verbdict["page1"] = self.simpleconj.copy()
        self.parent.enpresadv = self.thirdEdit.text()
        self.close()
        
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
        
    def closeEvent(self, event):
        """ Close the GUI passing GUI sizing information.
        """
        self.parent.geometry = self.geometry
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()