#!/usr/bin/python3
"""
    PastConj:  Machine Translation Data Entry -- Russian Verb Past Tense Conjugations.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 16, 2016, San Diego California United States of America
"""
import os, sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_pastconj import Ui_PastConj
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView

class PastConj(QDialog, Ui_PastConj):
    """ A GUI to enter Russian verb past tense conjugations.
    """
    
    helpfile = "/usr/share/machinetrans/resources/pastconj.html"
    parent = None
    labeltext = ""
    rustr = ""
    enstr = ""
    paststem = ""
    thirdpersonplural = ""
    reflexive = False
    oneself = False
    imperfective = True
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    imperfective = True
    geometry = list()    
    morphs = None
    pastconj = dict()
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the data.
            Do some selection of the format for the data.
        """
        super(PastConj, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        if not self.parent.verbpages[2]:
            self.pastconj.clear()
        else:
            self.pastconj = self.parent.verbdict["page3"].copy()
            del self.parent.verbdict["page3"]
        # Make this GUI the size of the calling GUI.
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        self.paststem = ""
        self.sqlcommand = ""
        # Set the GUI label values.
        self.labeltext = self.rutitleLbl.text()
        self.labeltext += " " + self.rustr.capitalize()
        self.rutitleLbl.setText(self.labeltext)
        self.labeltext = self.titleLbl.text()
        self.labeltext += " " + self.enstr.capitalize()
        self.titleLbl.setText(self.labeltext)
        # The stem of the past tense.
        self.thirdpersonplural = self.parent.thirdpersonplural
        # Check for an imperfective verb.
        self.imperfective = self.parent.sqldict["imperfective"] == "\'imperfective\'"
        # Check for a reflexive verb.
        self.oneself = self.parent.oneself
        endchars = self.rustr[-2:]
        if endchars == "ся" or endchars == "сь":
            self.reflexive = True
            self.rustr = self.rustr[:-2]
        # Connect the signals to the methods.
        self.quitBttn.clicked.connect(self.cancel)
        self.backBttn.clicked.connect(self.back)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.stemEdit.firereturn.triggered.connect(self.stemchg)
        self.stemEdit.firefocus.triggered.connect(self.stemchg)
        self.verbEdit.firereturn.triggered.connect(self.verbchg)
        self.verbEdit.firefocus.triggered.connect(self.verbchg)
        # Check for the type of past tense verb.
        if self.parent.verbpages[2]:
            self.paststem = self.pastconj["stem"]
            self.rumascEdit.setText(self.pastconj["masculine"]["conjugationru"].strip("\'"))
            self.rufemEdit.setText(self.pastconj["feminine"]["conjugationru"].strip("\'"))
            self.runuetEdit.setText(self.pastconj["nueter"]["conjugationru"].strip("\'"))
            self.ruplurEdit.setText(self.pastconj["plural"]["conjugationru"].strip("\'"))
        else:
            endchars = self.rustr[-4:]
            if endchars == "нуть":
                self.paststem = self.rustr[:-4]
                self.rumascEdit.setText(self.paststem)
            endchars = self.rustr[-3:]
            if endchars == "зти" or endchars == "сти":
                self.paststem = self.rustr[:-2]
                if self.paststem[-2] == "е":
                    tmpstr = self.paststem[:-2] + "ё" + self.paststem[-1]
                    self.rumascEdit.setText(tmpstr)
            endchars = self.rustr[-2:]
            if endchars == "чь":
                self.paststem = self.rustr[:-2] + "г"
                self.rumascEdit.setText(self.paststem)
            endchars = self.rustr[-2:]
            if endchars == "ть":
                self.paststem = self.rustr[:-2]
                self.rumascEdit.setText(self.paststem + self.morphs.vrbpast[1])
            if self.paststem == "":
                self.paststem = self.rustr
                self.rumascEdit.setText(self.paststem + self.morphs.vrbpast[1])
            self.pastconj["stem"] = self.paststem
        self.rufemEdit.setText(self.paststem + self.morphs.vrbpast[2])
        self.runuetEdit.setText(self.paststem + self.morphs.vrbpast[3])
        self.ruplurEdit.setText(self.paststem + self.morphs.vrbpast[4])
        if self.reflexive:
            tmpstr = self.rumascEdit.text()
            tmpstr += "ся"
            self.rumascEdit.setText(tmpstr)
            tmpstr = self.rufemEdit.text()
            tmpstr += "сь"
            self.rufemEdit.setText(tmpstr)
            tmpstr = self.runuetEdit.text()
            tmpstr += "сь"
            self.runuetEdit.setText(tmpstr)
            tmpstr = self.ruplurEdit.text()
            tmpstr += "сь"
            self.ruplurEdit.setText(tmpstr)
        self.stemEdit.setText(self.paststem)
        if self.parent.verbpages[2]:
            self.verbEdit.setText(self.pastconj["enverb"])
            self.mascEdit.setText(self.pastconj["masculine"]["conjugation"].strip("\'"))
            self.femEdit.setText(self.pastconj["feminine"]["conjugation"].strip("\'"))
            self.nuetEdit.setText(self.pastconj["nueter"]["conjugation"].strip("\'"))
            self.plurEdit.setText(self.pastconj["plural"]["conjugation"].strip("\'"))
        else:
            # Display the English.
            if self.enstr[:6] == "to be ":
                tmpstr = self.enstr[6:]
                if tmpstr.endswith(" by oneself") or tmpstr.endswith(" to oneself"):
                    reflexive = tmpstr[-8:]
                    prep = reflexive [:4]
                    tmpstr = tmpstr[:-8]
                    self.pastconj["enverb"] = tmpstr
                if self.oneself:
                    self.mascEdit.setText("was being " + tmpstr + prep + "himself")
                    self.femEdit.setText("was being " + tmpstr + prep + "herself")
                    self.nuetEdit.setText("was being " + tmpstr + prep + "itself")
                    self.plurEdit.setText("were being " + tmpstr + prep + "themselves")
                else:
                    self.mascEdit.setText("was being " + tmpstr)
                    self.femEdit.setText("was being " + tmpstr)
                    self.nuetEdit.setText("was being " + tmpstr)
                    self.plurEdit.setText("were being " + tmpstr)                
            elif self.enstr[:8] == "to have ":
                tmpstr = self.enstr[8:]
                if tmpstr.endswith(" by oneself") or tmpstr.endswith(" to oneself"):
                    reflexive = tmpstr[-8:]
                    prep = reflexive [:4]
                    tmpstr = tmpstr[:-8]
                    self.pastconj["enverb"] = tmpstr
                if self.oneself:
                    self.mascEdit.setText("was having " + tmpstr + prep + "himself")
                    self.femEdit.setText("was having " + tmpstr + prep + "herself")
                    self.nuetEdit.setText("was having " + tmpstr + prep + "itself")
                    self.plurEdit.setText("were having " + tmpstr + prep + "themselves")
                else:
                    self.mascEdit.setText("was having " + tmpstr)
                    self.femEdit.setText("was having " + tmpstr)
                    self.nuetEdit.setText("was having " + tmpstr)
                    self.plurEdit.setText("were having " + tmpstr)                
            else:    
                if self.enstr[:3] == "to ":
                    tmpstr = self.enstr[3:]
                else:
                    tmpstr = self.enstr
                if tmpstr.endswith(" oneself"):
                    tmpstr = tmpstr[:-8]
                tmpstr = tmpstr.strip()
                tmpstr1 = tmpstr
                if self.imperfective:
                    index = tmpstr.find(" ")        
                    if index > 0:
                        tmpstr1 = tmpstr[:index]
                        tmpstr2 = tmpstr[index:]
                        endchars = tmpstr1[-1]
                        if endchars == "e":
                            tmpstr1 = tmpstr1[:-1]
                        tmpstr1 += "ing"
                        tmpstr = tmpstr1 + tmpstr2
                    else:
                        endchars = tmpstr[-1]
                        if endchars == "e":
                            tmpstr = tmpstr[:-1]
                        tmpstr += "ing"
                    self.pastconj["enverb"] = tmpstr
                    if self.oneself:
                        self.mascEdit.setText("was " + tmpstr + " himself")
                        self.femEdit.setText("was " + tmpstr + " herself")
                        self.nuetEdit.setText("was " + tmpstr + " itself")
                        self.plurEdit.setText("were " + tmpstr + " themselves")
                    else:
                        self.mascEdit.setText("was " + tmpstr)
                        self.femEdit.setText("was " + tmpstr)
                        self.nuetEdit.setText("was " + tmpstr)
                        self.plurEdit.setText("were " + tmpstr)                
                else:
                    index = tmpstr.find(" ")        
                    if index > 0:
                        tmpstr1 = tmpstr[:index]
                        tmpstr2 = tmpstr[index:]
                        endchars = tmpstr1[-1]
                        if endchars == "e":
                            tmpstr1 = tmpstr1[:-1]
                        elif endchars == "y":
                            tmpstr1 = tmpstr1[:-1] + "i"
                        tmpstr1 += "ed"
                        tmpstr = tmpstr1 + tmpstr2
                    else:
                        endchars = tmpstr[-1]
                        if endchars == "e":
                            tmpstr = tmpstr[:-1]
                        elif endchars == "y":
                            tmpstr = tmpstr[:-1] + "i"
                        tmpstr += "ed"
                    self.pastconj["enverb"] = tmpstr
                    if self.oneself:
                        self.mascEdit.setText("have " + tmpstr + " himself")
                        self.femEdit.setText("have " + tmpstr + " herself")
                        self.nuetEdit.setText("have " + tmpstr + " itself")
                        self.plurEdit.setText("have " + tmpstr + " themselves")
                    else:
                        self.mascEdit.setText("have " + tmpstr)
                        self.femEdit.setText("have " + tmpstr)
                        self.nuetEdit.setText("have " + tmpstr)
                        self.plurEdit.setText("have " + tmpstr)
            self.pastconj["enverb"] = tmpstr
            self.verbEdit.setText(tmpstr)
            self.pastconj["masculine"] = dict()
            self.pastconj["feminine"] = dict()
            self.pastconj["nueter"] = dict()
            self.pastconj["plural"] = dict()
            self.pastconj["masculine"]["conjugationru"] = self.rumascEdit.text()
            self.pastconj["feminine"]["conjugationru"] = self.rufemEdit.text()
            self.pastconj["nueter"]["conjugationru"] = self.runuetEdit.text()
            self.pastconj["plural"]["conjugationru"] = self.ruplurEdit.text()
            self.pastconj["masculine"]["conjugation"] = self.mascEdit.text()
            self.pastconj["feminine"]["conjugation"] = self.femEdit.text()
            self.pastconj["nueter"]["conjugation"] = self.nuetEdit.text()
            self.pastconj["plural"]["conjugation"] = self.plurEdit.text()
        self.parent.verbpages[2] = True
        
    def resizeEvent(self, event):
        """ Resize the GUI and store sizing information.
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
        self.rutitleLbl.setGeometry(10, 20, tmpwidth, 60)
        tmpy = 80 * hscale
        tmpx = (self.width1 - 700) / 2
        self.stemLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = self.width1 / 2 + 20
        self.stemEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 120 * hscale
        tmpx = (self.width1 - 700) / 2
        self.rumascLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20) 
        self.rufemLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 30
        tmpx = (self.width1 - 700) / 2
        self.rumascEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20) 
        self.rufemEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 190 * hscale
        tmpx = (self.width1 - 700) / 2
        self.runuetLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20)
        self.ruplurLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 30
        tmpx = (self.width1 - 700) / 2
        self.runuetEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20)
        self.ruplurEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpwidth = self.width1 - 20
        tmpy = 280 * hscale
        self.titleLbl.setGeometry(10, tmpy, tmpwidth, 60)
        tmpy = 330 * hscale
        tmpx = (self.width1 - 700) / 2
        self.verbLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = self.width1 / 2 + 20
        self.verbEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 370 * hscale
        tmpx = (self.width1 - 700) / 2
        self.mascLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20)
        self.femLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 30
        tmpx = (self.width1 - 700) / 2
        self.mascEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20)
        self.femEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 440 * hscale
        tmpx = (self.width1 - 700) / 2
        self.nuetLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = ((self.width1 / 2) + 20)
        self.plurLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 30
        tmpx = (self.width1 - 700) / 2
        self.nuetEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 / 2) + 20)
        self.plurEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = ((self.width1 - 540) / 2)
        tmpy = self.height1 - 80
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx =  (self.width1 - 150) / 2
        self.backBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + 120
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
        

    def accept(self):
        """ Gather the data from the GUI and create SQL
            commands to insert the data into the database.
        """
        sqllist = list()
        self.enstr = self.parent.enstr
        self.rustr = self.parent.rustr
        self.enstr = self.apostrophe(self.enstr)
        mascstr = self.apostrophe(self.mascEdit.text())
        femstr = self.apostrophe(self.femEdit.text())
        nuetstr = self.apostrophe(self.nuetEdit.text())
        plurstr = self.apostrophe(self.plurEdit.text())
        if self.imperfective:
            tense = "\'simple past\'"
        else:
            tense = "\'perfect simple past\'"
        tmplist = list()
        lineitem = dict()
        tmplist.append("\'third\'")
        tmplist.append("\'" + mascstr + "\'")
        tmplist.append("\'" + self.rumascEdit.text() + "\'")
        tmplist.append("\'masculine\'")
        sqllist.append(tmplist)
        tmplist = list()
        tmplist.append("\'third\'")
        tmplist.append("\'" + femstr + "\'")
        tmplist.append("\'" + self.rufemEdit.text() + "\'")
        tmplist.append("\'feminine\'")
        sqllist.append(tmplist)
        tmplist = list()
        tmplist.append("\'third\'")
        tmplist.append("\'" + nuetstr + "\'")
        tmplist.append("\'" + self.runuetEdit.text() + "\'")
        tmplist.append("\'nueter\'")
        sqllist.append(tmplist)
        tmplist = list()
        tmplist.append("\'plural third\'")
        tmplist.append("\'" + plurstr + "\'")
        tmplist.append("\'" + self.ruplurEdit.text() + "\'")
        tmplist.append("\'plural\'")
        sqllist.append(tmplist)
        """
            This is the schema for a past tense verb in the database.
                CREATE TABLE pastverbs(
                    name text DEFAULT '',
                    runame text DEFAULT '',
                    tense tense_var DEFAULT 'simple past', 
                    gender gender_var DEFAULT 'masculine',
                    conjugation text DEFAULT '',
                    conjugationru text DEFAULT '',
                    objcase obj_var DEFAULT 'accusative',
                    imperfective imperfective_var DEFAULT 'imperfective'
                    );
        """
        for q in sqllist:
            lineitem["name"] = "\'" + self.enstr + "\'"
            lineitem["runame"] = "\'" + self.rustr + "\'"
            lineitem["objcase"] = self.parent.sqldict["objcase"]
            lineitem["conjugation"] = q[1]
            lineitem["conjugationru"] = q[2]
            lineitem["gender"] = q[3]
            lineitem["imperfective"] = self.parent.sqldict["imperfective"]
            lineitem["tense"] = tense
            tmpstr = q[3].strip("\'")
            self.pastconj[tmpstr] = lineitem.copy()
            lineitem.clear()
        self.pastconj["enverb"] = self.verbEdit.text()
        self.parent.enpasttense = self.verbEdit.text()
        self.pastconj["stem"] = self.stemEdit.text()
        self.parent.paststem = self.stemEdit.text()
        self.parent.verbdict["page3"] = self.pastconj.copy()
        self.parent.enpastadv = mascstr
        self.close()
    
    def stemchg(self):
        """ Accept and propagate a stem throughout the GUI.
        """
        self.paststem = self.stemEdit.text()
        self.rumascEdit.setText(self.paststem + self.morphs.vrbpast[1])
        self.rufemEdit.setText(self.paststem + self.morphs.vrbpast[2])
        self.runuetEdit.setText(self.paststem + self.morphs.vrbpast[3])
        self.ruplurEdit.setText(self.paststem  + self.morphs.vrbpast[4])
        self.pastconj["stem"] = self.paststem

    def apostrophe(self, x):
        """ Echo any apostrophes found in an English word ''
            so that they appear in the database.
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
        
    def verbchg(self):
        """ Change the English verb and propagate the change.
        """
        tmpstr = self.verbEdit.text()
        if self.enstr[:6] == "to be ":
            tmpstr = self.enstr[6:]
            if tmpstr.endswith(" by oneself") or tmpstr.endswith(" to oneself"):
                reflexive = tmpstr[-8:]
                prep = reflexive [:4]
                tmpstr = self.verbEdit.text()
                self.pastconj["enverb"] = tmpstr
            if self.oneself:
                self.mascEdit.setText("was being " + tmpstr + prep + "himself")
                self.femEdit.setText("was being " + tmpstr + prep + "herself")
                self.nuetEdit.setText("was being " + tmpstr + prep + "itself")
                self.plurEdit.setText("were being " + tmpstr + prep + "themselves")
            else:
                self.mascEdit.setText("was being " + tmpstr)
                self.femEdit.setText("was being " + tmpstr)
                self.nuetEdit.setText("was being " + tmpstr)
                self.plurEdit.setText("were being " + tmpstr)                
        elif self.enstr[:8] == "to have ":
            tmpstr = self.enstr[8:]
            if tmpstr.endswith(" by oneself") or tmpstr.endswith(" to oneself"):
                reflexive = tmpstr[-8:]
                prep = reflexive [:4]
                tmpstr = self.verbEdit.text()
                self.pastconj["enverb"] = sel.verbEdit.text()
            if self.oneself:
                self.mascEdit.setText("was having " + tmpstr + prep + "himself")
                self.femEdit.setText("was having " + tmpstr + prep + "herself")
                self.nuetEdit.setText("was having " + tmpstr + prep + "itself")
                self.plurEdit.setText("were having " + tmpstr + prep + "themselves")
            else:
                self.mascEdit.setText("was having " + tmpstr)
                self.femEdit.setText("was having " + tmpstr)
                self.nuetEdit.setText("was having " + tmpstr)
                self.plurEdit.setText("were having " + tmpstr)                
        else:    
            if self.enstr[:3] == "to ":
                tmpstr = self.enstr[3:]
            else:
                tmpstr = self.enstr
            if tmpstr.endswith(" oneself"):
                tmpstr = tmpstr[:-8]
            tmpstr = self.verbEdit.text()
            if self.imperfective:
                if self.oneself:
                    self.mascEdit.setText("was " + tmpstr + " himself")
                    self.femEdit.setText("was " + tmpstr + " herself")
                    self.nuetEdit.setText("was " + tmpstr + " itself")
                    self.plurEdit.setText("were " + tmpstr + " themselves")
                else:
                    self.mascEdit.setText("was " + tmpstr)
                    self.femEdit.setText("was " + tmpstr)
                    self.nuetEdit.setText("was " + tmpstr)
                    self.plurEdit.setText("were " + tmpstr)                
            else:
                if self.oneself:
                    self.mascEdit.setText("have " + tmpstr + " himself")
                    self.femEdit.setText("have " + tmpstr + " herself")
                    self.nuetEdit.setText("have " + tmpstr + " itself")
                    self.plurEdit.setText("have " + tmpstr + " themselves")
                else:
                    self.mascEdit.setText("have " + tmpstr)
                    self.femEdit.setText("have " + tmpstr)
                    self.nuetEdit.setText("have " + tmpstr)
                    self.plurEdit.setText("have " + tmpstr)
        self.pastconj["enverb"] = self.verbEdit.text()
        self.parent.paststem = self.stemEdit.text()
   
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
           
    def back(self):
        """ Go back one page in the data entry process.
        """
        self.parent.back = True
        self.accept()

    def closeEvent(self, event):
        """ Close the GUI and pass along sizing information.
        """
        self.parent.geometry = self.geometry
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept() 