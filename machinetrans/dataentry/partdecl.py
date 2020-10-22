#!/usr/bin/python3
"""
    PartDecl:  Machine Translation Data Entry -- Russian Participle Declension.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    June 29, 2016, San Diego California United States of America
"""
import os, sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_partdecl import Ui_PartDecl
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView

class PartDecl(QDialog, Ui_PartDecl):
    """ A GUI to enter Russian participles and their declensions.
        A Russian participle is an adjectival construct.
        This GUI allows the user to adjust for participles
        that do not have regular forms, some verbs do not have all the 
        varieties of participles. In particular, perfective
        verbs do not have the present tense forms.
            To manage the participles the data is divided up into 
        four tenses and five genders as follows:
        Genders: (0) Masculine Animate, (1) Masculine Inanimate, (2) Feminine, (3) Nueter,  (4) Plural Animate, (5) Plural Inanimate
        Tenses: (0) Present Active, (1) Present Passive, (2) Past Active, (3) Past Passive
    """
    helpfile = "/usr/share/machinetrans/resources/partdecl.html"
    parent = None
    partconj = dict()
    labeltext = ""
    rustr = ""
    enstr = ""
    reflexive = False
    oneself = False
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    imperfective = True
    motion = False
    geometry = list()    
    morphs = None
    types = None
    conjlist = list()
    vowels = list(["a", "e", "i", "o", "u"])
    thirdpersonplural = ""
    firstpersonplural = ""
    stem3 = ""
    stem4 = ""
    mascpresentactiveanim = list()
    mascpresentactiveinan = list()
    mascpastactiveanim = list()
    mascpastactiveinan = list()
    mascpresentpassiveanim = list()
    mascpresentpassiveinan = list()
    mascpastpassiveanim = list()
    mascpastpassiveinan = list()
    fempresentactive = list()
    fempastactive = list()
    fempresentpassive = list()
    fempastpassive = list()
    nuetpresentactive = list()
    nuetpastactive = list()
    nuetpresentpassive = list()
    nuetpastpassive = list()
    plurpresentactiveanim = list()
    plurpresentactiveinan = list()
    plurpastactiveanim = list()
    plurpastactiveinan = list()
    plurpresentpassiveanim = list()
    plurpresentpassiveinan = list()
    plurpastpassiveanim = list()
    plurpastpassiveinan = list()
    enpartkeys = ("mascpresentactiveanim", "mascpresentactiveinan", "mascpastactiveanim", \
        "mascpastactiveinan", "mascpresentpassiveanim", "mascpresentpassiveinan", \
        "mascpastpassiveanim", "mascpastpassiveinan", "fempresentactive", "fempastactive", \
        "fempresentpassive", "fempastpassive", "nuetpresentactive", "nuetpastactive", \
        "nuetpresentpassive", "nuetpastpassive", "plurpresentactiveanim", "plurpresentactiveinan", \
        "plurpastactiveanim", "plurpastactiveinan", "plurpresentpassiveanim", "plurpresentpassiveinan", \
        "plurpastpassiveanim", "plurpastpassiveinan")
    enpartvals = dict()
    tense = 0
    used = False
    gender = 0
    verblist = list()
    endings = list(["щ", "", "вш", "нн"])
    
    def __init__(self, parent=None):
        """ Intialize the GUI create the data lists for the various
            participial declensions and display the one for masculine
            present active participles if the verb is imperfective.
            and masculine past active participles if perfective.
        """
        super(PartDecl, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.types = self.parent.types
        if not self.parent.verbpages[1]:
            self.partconj.clear()
        else:
            self.partconj = self.parent.verbdict["page2"].copy()
            del self.parent.verbdict["page2"]
            self.enpartvals.clear()
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.rustr =  self.parent.rustr
        self.enstr = self.parent.enstr
        # Set the title with the verb infinitive.
        tmpstr = self.titleLbl.text()
        tmpstr += " " + self.rustr
        self.titleLbl.setText(tmpstr)
        ending = self.rustr[-2:]
        if ending == "ся" or ending == "сь":
            self.reflexive = True
            self.rustr = self.rustr[: -2]
        self.imperfective = self.parent.imperfective
        self.motion = self.parent.sqldict["variety"] == "\'motion\'"
        endchars = self.rustr[-2:]
        # Check for a reflexive verb.
        if endchars == "ся" or ending == "сь":
            self.reflexive = True
            self.oneself = self.parent.oneself
            self.rustr = self.rustr[:-2]
        # Check for an imperfective verb.
        if self.imperfective:
            self.thirdpersonplural = self.parent.thirdpersonplural
            self.firstpersonplural = self.parent.firstpersonplural
            endchars = self.thirdpersonplural[-3:]
            if endchars == "тся":
                self.thirdpersonplural = self.thirdpersonplural[:-3]
                self.firstpersonplural = self.firstpersonplural[:-2]
            else:
                self.thirdpersonplural = self.thirdpersonplural[:-1]
        else:
            self.parb.setEnabled(False)
            self.pprb.setEnabled(False)
        # Get the English verb stem and conjugate the english.
        if self.parent.verbpages[1]:
            self.thirdpersonplural = self.partconj["stem1"]
            self.firstpersonplural = self.partconj["stem2"]
            self.stem3 = self.partconj["stem3"]
            self.stem4 = self.partconj["stem4"]
        else:
            self.partconj["stem1"] = self.thirdpersonplural
            self.partconj["stem2"] = self.firstpersonplural
            self.stem3 = self.rustr[:-2]
            self.partconj["stem3"] = self.stem3
            self.stem4 = self.stem3[:]
            self.partconj["stem4"] = self.stem4
        if self.parent.verbpages[1]:
            for x in self.enpartkeys:
                self.enpartvals[x] = self.partconj[x]
        else:
            if self.enstr[:6] == "to be ":
                verb = self.enstr[6:]
                self.enpartvals["mascpresentactiveanim"] = "being " + verb
                self.enpartvals["mascpresentactiveinan"] = "being " + verb
                self.enpartvals["fempresentactive"] = "being " + verb
                self.enpartvals["nuetpresentactive"] = "being " + verb
                self.enpartvals["mascpastactiveanim"] = "was being " + verb
                self.enpartvals["mascpastactiveinan"] = "was being " + verb
                self.enpartvals["fempastactive"] = "was being " + verb
                self.enpartvals["nuetpastactive"] = "was being " + verb
                self.enpartvals["mascpresentpassiveanim"] = "is " + verb
                self.enpartvals["mascpresentpassiveinan"] = "is " + verb
                self.enpartvals["fempresentpassive"] = "is " + verb
                self.enpartvals["nuetpresentpassive"] = "is " + verb
                self.enpartvals["mascpastpassiveanim"] = "was " + verb
                self.enpartvals["mascpastpassiveinan"] = "was " + verb
                self.enpartvals["fempastpassive"] = "was " + verb
                self.enpartvals["nuetpastpassive"] = "was " + verb
                self.enpartvals["plurpresentactiveanim"] = "being " + verb
                self.enpartvals["plurpresentactiveinan"] = "being " + verb
                self.enpartvals["plurpastactiveanim"] = "were being " + verb
                self.enpartvals["plurpastactiveinan"] = "were being " + verb
                self.enpartvals["plurpresentpassiveanim"] = "are " + verb
                self.enpartvals["plurpresentpassiveinan"] = "are " + verb
                self.enpartvals["plurpastpassiveanim"] = "were " + verb
                self.enpartvals["plurpastpassiveinan"] = "were " + verb
            elif self.enstr[:8] == "to have ":
                verb = self.enstr[8:]
                self.enpartvals["mascpresentactiveanim"] = "having " + verb
                self.enpartvals["mascpresentactiveinan"] = "having " + verb
                self.enpartvals["fempresentactive"] = "having " + verb
                self.enpartvals["nuetpresentactive"] = "having " + verb
                self.enpartvals["mascpastactiveanim"] = "was having " + verb
                self.enpartvals["mascpastactiveinan"] = "was having " + verb
                self.enpartvals["fempastactive"] = "was having " + verb
                self.enpartvals["nuetpastactive"] = "was having " + verb
                self.enpartvals["mascpresentpassiveanim"] = "has " + verb
                self.enpartvals["mascpresentpassiveinan"] = "has " + verb
                self.enpartvals["fempresentpassive"] = "has " + verb
                self.enpartvals["nuetpresentpassive"] = "has " + verb
                self.enpartvals["mascpastpassiveanim"] = "had " + verb
                self.enpartvals["mascpastpassiveinan"] = "had " + verb
                self.enpartvals["fempastpassive"] = "had " + verb
                self.enpartvals["nuetpastpassive"] = "had " + verb
                self.enpartvals["plurpresentactiveanim"] = "having " + verb
                self.enpartvals["plurpresentactiveinan"] = "having " + verb
                self.enpartvals["plurpastactiveanim"] = "were having " + verb
                self.enpartvals["plurpastactiveinan"] = "were having " + verb
                self.enpartvals["plurpresentpassiveanim"] = "have " + verb
                self.enpartvals["plurpresentpassiveinan"] = "have " + verb
                self.enpartvals["plurpastpassiveanim"] = "had " + verb
                self.enpartvals["plurpastpassiveinan"] = "had " + verb
            else:
                if self.enstr[:3] == "to ":
                    tmpstr = self.enstr[3:]
                else:
                    tmpstr = self.enstr
                if tmpstr.endswith(" oneself"):
                    tmpstr = tmpstr[:-8]
                tmpstr = tmpstr.strip()
                index = tmpstr.find(" ")
                if index > 0:
                    tmpstr1 = tmpstr[:index]
                    tmpstr2 = tmpstr[index:]
                    if tmpstr1.endswith("e"):
                        tmpstr1 = tmpstr1[:-1]
                    if self.imperfective:
                        self.enpartvals["mascpresentactiveanim"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpresentactiveinan"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["fempresentactive"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["nuetpresentactive"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpastactiveanim"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpastactiveinan"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["fempastactive"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["nuetpastactive"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpresentpassiveanim"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["mascpresentpassiveinan"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["fempresentpassive"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["nuetpresentpassive"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["mascpastpassiveanim"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["mascpastpassiveinan"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["fempastpassive"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["nuetpastpassive"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpresentactiveanim"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpresentactiveinan"] = tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpastactiveanim"] = "were " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpastactiveinan"] = "were " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpresentpassiveanim"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpresentpassiveinan"] = "being " + tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpastpassiveanim"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpastpassiveinan"] = tmpstr1 + "ed" + tmpstr2
                        if self.oneself:
                            for x in self.enpartkeys:
                                if "plur" in x:
                                    self.enpartvals[x] += " themselves"
                                else:
                                    self.enpartvals[x] += " oneself"
                    else:
                        self.enpartvals["mascpastactiveanim"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpastactiveinan"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["fempastactive"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["nuetpastactive"] = "was " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["mascpastpassiveanim"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["mascpastpassiveinan"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["fempastpassive"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["nuetpastpassive"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpastactiveanim"] = "were " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpastactiveinan"] = "were " + tmpstr1 + "ing" + tmpstr2
                        self.enpartvals["plurpastpassiveanim"] = tmpstr1 + "ed" + tmpstr2
                        self.enpartvals["plurpastpassiveinan"] = tmpstr1 + "ed" + tmpstr2
                        if self.oneself:
                            for x in self.enpartkeys:
                                if "past" in x:
                                    if "plur" in x:
                                        self.enpartvals[x] += " themselves"
                                    else:
                                        self.enpartvals[x] += " oneself"
                else:
                    if tmpstr.endswith("e"):
                        tmpstr = tmpstr[:-1]
                    elif tmpstr.endswith("y"):
                        tmpstr = tmpstr[:-1] + "i"
                    if self.imperfective:
                        self.enpartvals["mascpresentactiveanim"] = tmpstr + "ing"
                        self.enpartvals["mascpresentactiveinan"] = tmpstr + "ing"
                        self.enpartvals["fempresentactive"] = tmpstr + "ing"
                        self.enpartvals["nuetpresentactive"] = tmpstr + "ing"
                        self.enpartvals["mascpastactiveanim"] = "was " + tmpstr + "ing"
                        self.enpartvals["mascpastactiveinan"] = "was " + tmpstr + "ing"
                        self.enpartvals["fempastactive"] = "was " + tmpstr + "ing"
                        self.enpartvals["nuetpastactive"] = "was " + tmpstr + "ing"
                        self.enpartvals["mascpresentpassiveanim"] = "being " + tmpstr + "ed"
                        self.enpartvals["mascpresentpassiveinan"] = "being " + tmpstr + "ed"
                        self.enpartvals["fempresentpassive"] = "being " + tmpstr + "ed"
                        self.enpartvals["nuetpresentpassive"] = "being " + tmpstr + "ed"
                        self.enpartvals["mascpastpassiveanim"] = tmpstr + "ed"
                        self.enpartvals["mascpastpassiveinan"] = tmpstr + "ed"
                        self.enpartvals["fempastpassive"] = tmpstr + "ed"
                        self.enpartvals["nuetpastpassive"] = tmpstr + "ed"
                        self.enpartvals["plurpresentactiveanim"] = tmpstr + "ing"
                        self.enpartvals["plurpresentactiveinan"] = tmpstr + "ing"
                        self.enpartvals["plurpastactiveanim"] = "were " + tmpstr + "ing"
                        self.enpartvals["plurpastactiveinan"] = "were " + tmpstr + "ing"
                        self.enpartvals["plurpresentpassiveanim"] = "being " + tmpstr + "ed"
                        self.enpartvals["plurpresentpassiveinan"] = "being " + tmpstr + "ed"
                        self.enpartvals["plurpastpassiveanim"] = tmpstr + "ed"
                        self.enpartvals["plurpastpassiveinan"] = tmpstr + "ed"
                        if self.oneself:
                            for x in self.enpartkeys:
                                if "plur" in x:
                                    self.enpartvals[x] += " themselves"
                                else:
                                    self.enpartvals[x] += " oneself"
                    else:
                        self.enpartvals["mascpastactiveanim"] = "was " + tmpstr + "ed"
                        self.enpartvals["mascpastactiveinan"] = "was " + tmpstr + "ed"
                        self.enpartvals["fempastactive"] = "was " + tmpstr + "ed"
                        self.enpartvals["nuetpastactive"] = "was " + tmpstr + "ed"
                        self.enpartvals["mascpastpassiveanim"] = tmpstr + "ed"
                        self.enpartvals["mascpastpassiveinan"] = tmpstr + "ed"
                        self.enpartvals["fempastpassive"] = tmpstr + "ed"
                        self.enpartvals["nuetpastpassive"] = tmpstr + "ed"
                        self.enpartvals["plurpastactiveanim"] = "were " + tmpstr + "ed"
                        self.enpartvals["plurpastactiveinan"] = "were " + tmpstr + "ed"
                        self.enpartvals["plurpastpassiveanim"] = tmpstr + "ed"
                        self.enpartvals["plurpastpassiveinan"] = tmpstr + "ed"
                        if self.oneself:
                            for x in self.enpartkeys:
                                if "past" in x:
                                    if "plur" in x:
                                        self.enpartvals[x] += " themselves"
                                    else:
                                        self.enpartvals[x] += " oneself"

            # Collect the data for browsing the pages.
            for x in self.enpartkeys:
                self.partconj[x] = self.enpartvals[x]

        # Connect the signals and slots.
        self.nomEdit.firereturn.triggered.connect(self.alter)
        self.accEdit.firereturn.triggered.connect(self.alter)
        self.genEdit.firereturn.triggered.connect(self.alter)
        self.datEdit.firereturn.triggered.connect(self.alter)
        self.insEdit.firereturn.triggered.connect(self.alter)
        self.prpEdit.firereturn.triggered.connect(self.alter)
        self.enEdit.firereturn.triggered.connect(self.alter)
        self.stemEdit.firereturn.triggered.connect(self.stemchange)    
        self.endEdit.firereturn.triggered.connect(self.endchange)    
        self.nomEdit.firefocus.triggered.connect(self.alter)
        self.accEdit.firefocus.triggered.connect(self.alter)
        self.genEdit.firefocus.triggered.connect(self.alter)
        self.datEdit.firefocus.triggered.connect(self.alter)
        self.insEdit.firefocus.triggered.connect(self.alter)
        self.prpEdit.firefocus.triggered.connect(self.alter)
        self.enEdit.firefocus.triggered.connect(self.alter)
        self.stemEdit.firefocus.triggered.connect(self.stemchange)    
        self.endEdit.firefocus.triggered.connect(self.endchange)    
        # Connect up the radio buttons.
        self.parb.released.connect(self.pa)
        self.pprb.released.connect(self.pp)
        self.pastarb.released.connect(self.pasta)
        self.pastprb.released.connect(self.pastp)
        self.mascanimrb.released.connect(self.masculineanim)
        self.mascinanrb.released.connect(self.masculineinan)
        self.femrb.released.connect(self.feminine)
        self.nuetrb.released.connect(self.nueter)
        self.pluranimrb.released.connect(self.pluralanim)
        self.plurinanrb.released.connect(self.pluralinan)
        self.quitBttn.clicked.connect(self.cancel)
        self.backBttn.clicked.connect(self.back)
        self.acceptBttn.clicked.connect(self.accept)
        self.changeBttn.clicked.connect(self.changeeng)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.presaCheck.clicked.connect(self.callgender)
        self.prespCheck.clicked.connect(self.callgender)
        self.pastaCheck.clicked.connect(self.callgender)
        self.pastpCheck.clicked.connect(self.callgender)
        # Initialize the form for an imperfective verb.
        if not self.parent.verbpages[1]:
            if self.imperfective:
                self.tense = 0
                self.parb.setChecked(True)
                self.presaCheck.setChecked(True)
                self.prespCheck.setChecked(True)
                self.pastaCheck.setChecked(True)
                self.pastpCheck.setChecked(True)
                self.parent.pastactive = True
            else:
                # Initialze the form for a perfective verb.
                self.tense = 2
                self.pastarb.setChecked(True)
                self.presaCheck.setEnabled(False)
                self.prespCheck.setEnabled(False)
                self.pastaCheck.setChecked(True)
                self.pastpCheck.setChecked(True)
                self.parent.pastactive = True
            if self.motion:
                # Initialize the form for a verb of motion.
                if self.imperfective:
                    self.presaCheck.setChecked(True)
                else:
                    self.presaCheck.setChecked(False)
                self.pastaCheck.setChecked(True)
                self.prespCheck.setChecked(False)
                self.pastpCheck.setChecked(False)
            self.partconj["presaen"] = self.presaCheck.isEnabled()
            self.partconj["prespen"] = self.prespCheck.isEnabled()
            self.partconj["pastaen"] = self.pastaCheck.isEnabled()
            self.partconj["pastpen"] = self.pastpCheck.isEnabled()
            self.partconj["presa"] = self.presaCheck.isChecked()
            self.partconj["presp"] = self.prespCheck.isChecked()
            self.partconj["pasta"] = self.pastaCheck.isChecked()
            self.partconj["pastp"] = self.pastpCheck.isChecked()
        else:
            self.presaCheck.setEnabled(self.partconj["presaen"])
            self.prespCheck.setEnabled(self.partconj["prespen"])
            self.pastaCheck.setEnabled(self.partconj["pastaen"])
            self.pastpCheck.setEnabled(self.partconj["pastpen"])
            self.presaCheck.setChecked(self.partconj["presa"])
            self.prespCheck.setChecked(self.partconj["presp"])
            self.pastaCheck.setChecked(self.partconj["pasta"])
            self.pastpCheck.setChecked(self.partconj["pastp"])
        self.mascanimrb.setChecked(True)
        if self.parent.verbpages[1]:
            self.endings[0] = self.partconj["ending1"]
            self.endings[1] = self.partconj["ending2"]
            self.endings[2] = self.partconj["ending3"]
            self.endings[3] = self.partconj["ending4"]
        # Display the data for the masculine participle.
        self.stemEdit.setText(self.thirdpersonplural)
        self.endEdit.setText(self.endings[0])
        self.createdecl()
        self.parent.verbpages[1] = True
        
        
    def resizeEvent(self, event):
        """ Resize the GUI and store sizing information.
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
        self.titleLbl.setGeometry(10, 10, tmpwidth, 30)
        tmpy = 40 * hscale
        self.tenseBox.setGeometry(10, tmpy, tmpwidth, tmpy)
        tmpint = tmpwidth / 4
        tmpx = 20
        tmpy = 20 * hscale
        self.parb.setGeometry(tmpx, tmpy, 170, 25)
        tmpx += tmpint
        self.pprb.setGeometry(tmpx, tmpy, 170, 25)
        tmpx += tmpint
        self.pastarb.setGeometry(tmpx, tmpy, 170, 25)
        tmpx += tmpint
        self.pastprb.setGeometry(tmpx, tmpy, 170, 25)
        tmpy = 90 * hscale
        self.genderBox.setGeometry(10, tmpy, tmpwidth, tmpy)
        tmpx = 70
        tmpy = 20 * hscale
        self.mascanimrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = (self.width1 - 200) / 2
        self.mascinanrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = tmpwidth - 200
        self.femrb.setGeometry(tmpx, tmpy, 150, 25)
        tmpx = 70
        tmpy = 50 * hscale
        self.nuetrb.setGeometry(tmpx, tmpy, 150, 25)
        tmpx = (self.width1 - 200) / 2
        self.pluranimrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = tmpwidth - 250
        self.plurinanrb.setGeometry(tmpx, tmpy, 200, 25)
        tmpy = 190 * hscale
        tmpint = 30 * hscale
        tmpx = (self.width1 - 740) / 2
        self.nomLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.accLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 25 * hscale
        tmpx = (self.width1 - 740) / 2
        self.nomEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.accEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += tmpint
        tmpx = (self.width1 - 740) / 2
        self.genLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.datLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 25 * hscale
        tmpx = (self.width1 - 740) / 2
        self.genEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.datEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += tmpint
        tmpx = (self.width1 - 740) / 2
        self.insLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.prpLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 25 * hscale
        tmpx = (self.width1 - 740) / 2
        self.insEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + 30
        self.prpEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpy = 360 * hscale
        tmpx = (self.width1 - 740) / 2 + 50
        self.presaCheck.setGeometry(tmpx, tmpy, 200, 30)
        tmpx = (self.width1 / 2) + 80
        self.pastaCheck.setGeometry(tmpx, tmpy, 200, 30)
        tmpy += 30
        tmpx = (self.width1 - 740) / 2 + 50
        self.prespCheck.setGeometry(tmpx, tmpy, 200, 30)
        tmpx = (self.width1 / 2) + 80
        self.pastpCheck.setGeometry(tmpx, tmpy, 200, 30)
        tmpy = 420 * hscale
        tmpx = (self.width1 - 740) / 2
        self.stemLbl.setGeometry(tmpx, tmpy, 80, 25)
        tmpx += 100
        self.stemEdit.setGeometry(tmpx, tmpy, 230, 25)
        tmpx = (self.width1 / 2) + 10
        self.endLbl.setGeometry(tmpx, tmpy, 80, 25)
        tmpx += 100
        self.endEdit.setGeometry(tmpx, tmpy, 230, 25)
        tmpy = 470 * hscale
        tmpx = (self.width1 - 680) / 2
        self.enLbl.setGeometry(tmpx, tmpy, 80, 25)
        tmpx += 100
        self.enEdit.setGeometry(tmpx, tmpy, 340, 25)
        tmpx = (self.width1 / 2) + (130 * wscale)
        tmpy = 460 * hscale
        self.changeBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 - 600) / 2
        tmpy = self.height1 - 70
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) - 60
        self.backBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = self.width1 - (((self.width1 - 600) / 2) + 150)
        self.acceptBttn.setGeometry(tmpx, tmpy , 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
    
    def stemchange(self):
        """ Record and propagate a stem change from the Line Editor for the Russian stem.
            This works only on the current tense displayed, except for the past tenses.
        """
        if self.tense == 0:
            self.thirdpersonplural = self.stemEdit.text()
            self.partconj["stem1"] = self.thirdpersonplural
        elif self.tense == 1:
            self.firstpersonplural = self.stemEdit.text()
            self.partconj["stem2"] = self.firstpersonplural
        elif self.tense == 2:
            self.stem3 = self.stemEdit.text()
            self.partconj["stem3"] = self.stem3
        elif self.tense == 3:
            self.stem4 = self.stemEdit.text()
            self.partconj["stem4"] = self.stem4
        self.createdecl()
        
    def endchange(self):
        """ Record and propagate the change in an infix between the stem and the 
            adjectival endings.  Works only on the tense displayed.
        """
        if self.tense == 0:
            self.endings[0] = self.endEdit.text()
            self.partconj["ending1"] = self.endings[0]
        elif self.tense == 1:
            self.endings[1] = self.endEdit.text()
            self.partconj["ending2"] = self.endings[1]
        elif self.tense == 2:
            self.endings[2] = self.endEdit.text()
            self.partconj["ending3"] = self.endings[2]
        else:
            self.endings[3] = self.endEdit.text()
            self.partconj["ending4"] = self.endings[3]
        self.createdecl()
        
    def createdecl(self):
        """ Create the declensions.
            This is a seperate method because altering stem
            and endings are allowed in this GUI.
        """
        self.mascpresentactiveanim = list()
        self.mascpresentactiveinan = list()
        self.mascpastactiveanim = list()
        self.mascpastactiveinan = list()
        self.mascpresentpassiveanim = list()
        self.mascpresentpassiveinan = list()
        self.mascpastpassiveanim = list()
        self.mascpastpassiveinan = list()
        self.fempresentactive = list()
        self.fempastactive = list()
        self.fempresentpassive = list()
        self.fempastpassive = list()
        self.nuetpresentactive = list()
        self.nuetpastactive = list()
        self.nuetpresentpassive = list()
        self.nuetpastpassive = list()
        self.plurpresentactiveanim = list()
        self.plurpresentactiveinan = list()
        self.plurpastactiveanim = list()
        self.plurpastactiveinan = list()
        self.plurpresentpassiveanim = list()
        self.plurpresentpassiveinan = list()
        self.plurpastpassiveanim = list()
        self.plurpastpassiveinan = list()
        if not self.used and self.parent.verbpages[1]:
            self.createfromdata()
        elif self.reflexive:
            if self.imperfective:
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftanim[y]
                    self.mascpresentactiveanim.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftinan[y]
                    self.mascpresentactiveinan.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftanim[y]
                    self.mascpresentpassiveanim.append(self.firstpersonplural + self.endings[1] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftinan[y]
                    self.mascpresentpassiveinan.append(self.firstpersonplural + self.endings[1] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjfemideclsft[y]
                    self.fempresentactive.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjfemideclhrd[y]
                    self.fempresentpassive.append(self.firstpersonplural + self.endings[1] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjnuetdeclsft[y]
                    self.nuetpresentactive.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjnuetdeclhrd[y]
                    self.nuetpresentpassive.append(self.firstpersonplural + self.endings[1] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftanim[y]
                    self.plurpresentactiveanim.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftinan[y]
                    self.plurpresentactiveinan.append(self.thirdpersonplural + self.endings[0] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftanim[y]
                    self.plurpresentpassiveanim.append(self.firstpersonplural + self.endings[1] + x + "ся")
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftinan[y]
                    self.plurpresentpassiveinan.append(self.firstpersonplural + self.endings[1] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjmascdeclsftanim[y]
                self.mascpastactiveanim.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjmascdeclsftinan[y]
                self.mascpastactiveinan.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjmascdeclhrdanim[y]
                self.mascpastpassiveanim.append(self.stem4 + self.endings[3] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjmascdeclhrdinan[y]
                self.mascpastpassiveinan.append(self.stem4 + self.endings[3] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjfemideclsft[y]
                self.fempastactive.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjfemideclhrd[y]
                self.fempastpassive.append(self.stem4 + self.endings[3] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjnuetdeclsft[y]
                self.nuetpastactive.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjnuetdeclhrd[y]
                self.nuetpastpassive.append(self.stem4 + self.endings[3] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjplurdeclsftanim[y]
                self.plurpastactiveanim.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjplurdeclsftinan[y]
                self.plurpastactiveinan.append(self.stem3 + self.endings[2] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjplurdeclhrdanim[y]
                self.plurpastpassiveanim.append(self.stem4 + self.endings[3] + x + "ся")
            for y in range(1,7):
                x = self.morphs.adjplurdeclhrdinan[y]
                self.plurpastpassiveinan.append(self.stem4 + self.endings[3] + x + "ся")
        else:
            if self.imperfective:
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftanim[y]
                    self.mascpresentactiveanim.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjmascdeclsftinan[y]
                    self.mascpresentactiveinan.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjmascdeclhrdanim[y]
                    self.mascpresentpassiveanim.append(self.firstpersonplural + self.endings[1] + x)
                for y in range(1,7):
                    x = self.morphs.adjmascdeclhrdinan[y]
                    self.mascpresentpassiveinan.append(self.firstpersonplural + self.endings[1] + x)
                for y in range(1,7):
                    x = self.morphs.adjfemideclsft[y]
                    self.fempresentactive.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjfemideclhrd[y]
                    self.fempresentpassive.append(self.firstpersonplural + self.endings[1] + x)
                for y in range(1,7):
                    x = self.morphs.adjnuetdeclsft[y]
                    self.nuetpresentactive.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjnuetdeclhrd[y]
                    self.nuetpresentpassive.append(self.firstpersonplural + self.endings[1] + x)
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftanim[y]
                    self.plurpresentactiveanim.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjplurdeclsftinan[y]
                    self.plurpresentactiveinan.append(self.thirdpersonplural + self.endings[0] + x)
                for y in range(1,7):
                    x = self.morphs.adjplurdeclhrdanim[y]
                    self.plurpresentpassiveanim.append(self.firstpersonplural + self.endings[1] + x)
                for y in range(1,7):
                    x = self.morphs.adjplurdeclhrdinan[y]
                    self.plurpresentpassiveinan.append(self.firstpersonplural + self.endings[1] + x)
            for y in range(1,7):
                x = self.morphs.adjmascdeclsftanim[y]
                self.mascpastactiveanim.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjmascdeclsftinan[y]
                self.mascpastactiveinan.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjmascdeclhrdanim[y]
                self.mascpastpassiveanim.append(self.stem4 + self.endings[3] + x)
            for y in range(1,7):
                x = self.morphs.adjmascdeclhrdinan[y]
                self.mascpastpassiveinan.append(self.stem4 + self.endings[3] + x)
            for y in range(1,7):
                x = self.morphs.adjfemideclsft[y]
                self.fempastactive.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjfemideclhrd[y]
                self.fempastpassive.append(self.stem4 + self.endings[3] + x)
            for y in range(1,7):
                x = self.morphs.adjnuetdeclsft[y]
                self.nuetpastactive.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjnuetdeclhrd[y]
                self.nuetpastpassive.append(self.stem4 + self.endings[3] + x)
            for y in range(1,7):
                x = self.morphs.adjplurdeclsftanim[y]
                self.plurpastactiveanim.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjplurdeclsftinan[y]
                self.plurpastactiveinan.append(self.stem3 + self.endings[2] + x)
            for y in range(1,7):
                x = self.morphs.adjplurdeclhrdanim[y]
                self.plurpastpassiveanim.append(self.stem4 + self.endings[3] + x)
            for y in range(1,7):
                x = self.morphs.adjplurdeclhrdinan[y]
                self.plurpastpassiveinan.append(self.stem4 + self.endings[3] + x)
        self.used = True
        self.callgender()
    
    def createfromdata(self):
        """ Used when browsing the pages.  Ensures that any altered data is still the same on the screen.
        """
        if self.partconj["presa"]:
            self.mascpresentactiveanim = self.getlist("masculine present active animate")
            self.mascpresentactiveinan = self.getlist("masculine present active inanimate")
            self.fempresentactive = self.getlist("feminine present active inanimate")
            self.nuetpresentactive = self.getlist("nueter present active inanimate")
            self.plurpresentactiveanim = self.getlist("plural present active animate")
            self.plurpresentactiveinan = self.getlist("plural present active inanimate")
        if self.partconj["presp"]:
            self.mascpresentpassiveanim = self.getlist("masculine present passive animate")
            self.mascpresentpassiveinan = self.getlist("masculine present passive inanimate")
            self.fempresentpassive = self.getlist("feminine present passive inanimate")
            self.nuetpresentpassive = self.getlist("nueter present passive inanimate")
            self.plurpresentpassiveanim = self.getlist("plural present passive animate")
            self.plurpresentpassiveinan = self.getlist("plural present passive inanimate")
        if self.partconj["pasta"]:
            self.mascpastactiveanim = self.getlist("masculine past active animate")
            self.mascpastactiveinan = self.getlist("masculine past active inanimate")
            self.fempastactive = self.getlist("feminine past active inanimate")
            self.nuetpastactive = self.getlist("nueter past active inanimate")
            self.plurpastactiveanim = self.getlist("plural past active animate")
            self.plurpastactiveinan = self.getlist("plural past active inanimate")
        if self.partconj["pastp"]:
            self.mascpastpassiveanim = self.getlist("masculine past passive animate")
            self.mascpastpassiveinan = self.getlist("masculine past passive inanimate")
            self.fempastpassive = self.getlist("feminine past passive inanimate")
            self.nuetpastpassive = self.getlist("nueter past passive inanimate")
            self.plurpastpassiveanim = self.getlist("plural past passive animate")
            self.plurpastpassiveinan = self.getlist("plural past passive inanimate")
        if self.partconj["presa"]:
            self.pa()
            return
        if self.partconj["presp"]:
            self.pp()
            return
        if self.partconj["pasta"]:
            self.pasta()
            return
        if self.partconj["pastp"]:
            self.pastp()
            return
        

    def extractval(self, item):
        """ Extract one item from a line of partconj with sorted keys.
            The item that corresponds to "declension" is the declined participle.
        """
        vars = list()
        values = list()
        for x in sorted(item.keys()):
            vars.append(x)
            values.append(item[x].strip("\'"))
        decl = vars.index("declension")
        return values[decl]

    def getlist(self, itemstr):
        """ Get an ordered list of conjugations corresponding to the order of the
            WordMorph class declension list by using that list to index the data.
        """
        verb = dict()
        result = list()
        for x in range(1,7):
            y = self.types.declension[x]
            tmpstr = itemstr + " " + y
            data = self.partconj[tmpstr]
            result.append(self.extractval(data))
        return result
                
    def masculineanim(self):
        """ Fill the GUI with "masculine animate" information for the selected tense.
        """
        self.gender = 0
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.mascpresentactiveanim)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.mascpresentpassiveanim)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.mascpastactiveanim)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.mascpastpassiveanim)
            else:
                self.blankform()

    def masculineinan(self):
        """ Fill the GUI with "masculine inanimate" information for the selected tense.
        """
        self.gender = 1
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.mascpresentactiveinan)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.mascpresentpassiveinan)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.mascpastactiveinan)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.mascpastpassiveinan)
            else:
                self.blankform()
    
    def feminine(self):
        """ Fill the GUI with "feminine" information for the selected tense.
        """
        self.gender = 2
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.fempresentactive)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.fempresentpassive)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.fempastactive)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.fempastpassive)
            else:
                self.blankform()
            
    def nueter(self):
        """ Fill the GUI with "nueter" information for the selected tense.
        """
        self.gender = 3
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.nuetpresentactive)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.nuetpresentpassive)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.nuetpastactive)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.nuetpastpassive)
            else:
                self.blankform()

    def pluralanim(self):
        """ Fill the GUI with "plural animate" information for the selected tense.
        """
        self.gender = 4
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.plurpresentactiveanim)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.plurpresentpassiveanim)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.plurpastactiveanim)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.plurpastpassiveanim)
            else:
                self.blankform()

    def pluralinan(self):
        """ Fill the GUI with "plural inanimate" information for the selected tense.
        """
        self.gender = 5
        if self.imperfective:
            if self.tense == 0:
                if self.presaCheck.isChecked():
                    self.fillform(self.plurpresentactiveinan)
                else:
                    self.blankform()
            elif self.tense == 1:
                if self.prespCheck.isChecked():
                    self.fillform(self.plurpresentpassiveinan)
                else:
                    self.blankform()
        if self.tense == 2:
            if self.pastaCheck.isChecked():
                self.fillform(self.plurpastactiveinan)
            else:
                self.blankform()
        elif self.tense == 3:
            if self.pastpCheck.isChecked():
                self.fillform(self.plurpastpassiveinan)
            else:
                self.blankform()

    def pa(self):
        """ Present Active Participle tense selector.
        """
        self.tense = 0
        self.stemEdit.setText(self.thirdpersonplural)
        self.callgender()
        
    def pp(self):
        """ Present Passive Participle tense selector.
        """
        self.tense = 1
        self.stemEdit.setText(self.firstpersonplural)
        self.callgender()

    def pasta(self):
        """ Past Active Participle tense selector.
        """
        self.parent.pastactive = True
        self.tense = 2
        self.stemEdit.setText(self.stem3)
        self.callgender()

    def pastp(self):
        """ Past Passive Participle tense selector.
        """
        self.tense = 3
        self.stemEdit.setText(self.stem4)
        self.callgender()
        
    def callgender(self):
        """ Calls the proper gender of participial declensions.
            The tense must be selected before hand.
            Also enable or disable the radio buttons
            and declensions based upon which check boxes are selected.
        """
        self.parb.setEnabled(self.presaCheck.isChecked())
        self.pprb.setEnabled(self.prespCheck.isChecked())
        self.pastarb.setEnabled(self.pastaCheck.isChecked())
        self.pastprb.setEnabled(self.pastpCheck.isChecked())
        if self.tense == 0:
            self.stemEdit.setText(self.thirdpersonplural)
            self.endEdit.setText(self.endings[0])
        elif self.tense == 1:
            self.stemEdit.setText(self.firstpersonplural)
            self.endEdit.setText(self.endings[1])
        elif self.tense == 2:
            self.stemEdit.setText(self.stem3)
            self.endEdit.setText(self.endings[2])
        elif self.tense == 3:
            self.stemEdit.setText(self.stem4)
            self.endEdit.setText(self.endings[3])
        if self.gender == 0:
            self.masculineanim()
        elif self.gender == 1:
            self.masculineinan()
        elif self.gender == 2:
            self.feminine()
        elif self.gender == 3:
            self.nueter()
        elif self.gender == 4:
            self.pluralanim()
        else:
            self.pluralinan()

    def english(self):
        """ Display the English translation
            for the selected tense and gender of participle.
        """
        if self.tense == 0:
            if self.gender == 0:
                self.enEdit.setText(self.enpartvals["mascpresentactiveanim"])
            elif self.gender == 1:
                self.enEdit.setText(self.enpartvals["mascpresentactiveinan"])
            elif self.gender == 2:
                self.enEdit.setText(self.enpartvals["fempresentactive"])
            elif self.gender == 3:
                self.enEdit.setText(self.enpartvals["nuetpresentactive"])
            elif self.gender == 4:
                self.enEdit.setText(self.enpartvals["plurpresentactiveanim"])
            elif self.gender == 5:
                self.enEdit.setText(self.enpartvals["plurpresentactiveinan"])
        elif self.tense == 1:
            if self.gender == 0:
                self.enEdit.setText(self.enpartvals["mascpresentpassiveanim"])
            elif self.gender == 1:
                self.enEdit.setText(self.enpartvals["mascpresentpassiveinan"])
            elif self.gender == 2:
                self.enEdit.setText(self.enpartvals["fempresentpassive"])
            elif self.gender == 3:
                self.enEdit.setText(self.enpartvals["nuetpresentpassive"])
            elif self.gender == 4:
                self.enEdit.setText(self.enpartvals["plurpresentpassiveanim"])
            elif self.gender == 5:
                self.enEdit.setText(self.enpartvals["plurpresentpassiveinan"])
        elif self.tense == 2:
            if self.gender == 0:
                self.enEdit.setText(self.enpartvals["mascpastactiveanim"])
            elif self.gender == 1:
                self.enEdit.setText(self.enpartvals["mascpastactiveinan"])
            elif self.gender == 2:
                self.enEdit.setText(self.enpartvals["fempastactive"])
            elif self.gender == 3:
                self.enEdit.setText(self.enpartvals["nuetpastactive"])
            elif self.gender == 4:
                self.enEdit.setText(self.enpartvals["plurpastactiveanim"])
            elif self.gender == 5:
                self.enEdit.setText(self.enpartvals["plurpastactiveinan"])
        elif self.tense == 3:
            if self.gender == 0:
                self.enEdit.setText(self.enpartvals["mascpastpassiveanim"])
            elif self.gender == 1:
                self.enEdit.setText(self.enpartvals["mascpastpassiveinan"])
            elif self.gender == 2:
                self.enEdit.setText(self.enpartvals["fempastpassive"])
            elif self.gender == 3:
                self.enEdit.setText(self.enpartvals["nuetpastpassive"])
            elif self.gender == 4:
                self.enEdit.setText(self.enpartvals["plurpastpassiveanim"])
            elif self.gender == 5:
                self.enEdit.setText(self.enpartvals["plurpastpassiveinan"])

    def fillform(self, verbdata):
        """ Add the declension data to the Line Editors.
        """
        self.nomEdit.setText(verbdata[0])
        self.accEdit.setText(verbdata[1])
        self.genEdit.setText(verbdata[2])
        self.datEdit.setText(verbdata[3])
        self.insEdit.setText(verbdata[4])
        self.prpEdit.setText(verbdata[5])
        self.english()

    def blankform(self):
        """ Clear the  Line Editors.  
            This is the result of a check box being unchecked.
        """
        self.nomEdit.setText("")
        self.accEdit.setText("")
        self.genEdit.setText("")
        self.datEdit.setText("")
        self.insEdit.setText("")
        self.prpEdit.setText("")
        self.enEdit.setText("")
    
    def alter(self):
        """ Propgate altered data to the various lists that are
            effected by user input to the Line Editors.
        """
        self.verblist = list()
        self.verblist.append(self.nomEdit.text())
        self.verblist.append(self.accEdit.text())
        self.verblist.append(self.genEdit.text())
        self.verblist.append(self.datEdit.text())
        self.verblist.append(self.insEdit.text())
        self.verblist.append(self.prpEdit.text())
        if self.gender == 0:
            self.altermascanim()
        elif self.gender == 1:
            self.altermascinan()
        elif self.gender == 2:
            self.alterfem()
        elif self.gender == 3:
            self.alternuet()
        elif self.gender == 4:
            self.alterpluranim()
        else:
            self.alterplurinan()
        self.alterenglish()
    
    def changeeng(self):
        """ Takes the value in the English line editor and distributes
            it to all the values of the displayed tense for that participle.
        """
        if self.tense == 0:
            self.enpartvals["mascpresentactiveanim"] = self.enEdit.text()
            self.enpartvals["mascpresentactiveinan"] = self.enEdit.text()
            self.enpartvals["fempresentactive"] = self.enEdit.text()
            self.enpartvals["nuetpresentactive"] = self.enEdit.text()
            self.enpartvals["plurpresentactiveanim"] = self.enEdit.text()
            self.enpartvals["plurpresentactiveinan"] = self.enEdit.text()
        elif self.tense == 1:
            self.enpartvals["mascpresentpassiveanim"] = self.enEdit.text()
            self.enpartvals["mascpresentpassiveinan"] = self.enEdit.text()
            self.enpartvals["fempresentpassive"] = self.enEdit.text()
            self.enpartvals["nuetpresentpassive"] = self.enEdit.text()
            self.enpartvals["plurpresentpassiveanim"] = self.enEdit.text()
            self.enpartvals["plurpresentpassiveinan"] = self.enEdit.text()
        elif self.tense == 2:
            self.enpartvals["mascpastactiveanim"] = self.enEdit.text()
            self.enpartvals["mascpastactiveinan"] = self.enEdit.text()
            self.enpartvals["fempastactive"] = self.enEdit.text()
            self.enpartvals["nuetpastactive"] = self.enEdit.text()
            self.enpartvals["plurpastactiveanim"] = self.enEdit.text()
            self.enpartvals["plurpastactiveinan"] = self.enEdit.text()
        elif self.tense == 3:
            self.enpartvals["mascpastpassiveanim"] = self.enEdit.text()
            self.enpartvals["mascpastpassiveinan"] = self.enEdit.text()
            self.enpartvals["fempastpassive"] = self.enEdit.text()
            self.enpartvals["nuetpastpassive"] = self.enEdit.text()
            self.enpartvals["plurpastpassiveanim"] = self.enEdit.text()
            self.enpartvals["plurpastpassiveinan"] = self.enEdit.text()
        
    
    def alterenglish(self):
        """ Alter the English data for a specific tense and gender.
        """
        if self.tense == 0:
            if self.gender == 0:
                self.enpartvals["mascpresentactiveanim"] = self.enEdit.text()
            elif self.gender == 1:
                self.enpartvals["mascpresentactiveinan"] = self.enEdit.text()
            elif self.gender == 2:
                self.enpartvals["fempresentactive"] = self.enEdit.text()
            elif self.gender == 3:
                self.enpartvals["nuetpresentactive"] = self.enEdit.text()
            elif self.gender == 4:
                self.enpartvals["plurpresentactiveanim"] = self.enEdit.text()
            elif self.gender == 5:
                self.enpartvals["plurpresentactiveinan"] = self.enEdit.text()
        elif self.tense == 1:
            if self.gender == 0:
                self.enpartvals["mascpresentpassiveanim"] = self.enEdit.text()
            elif self.gender == 1:
                self.enpartvals["mascpresentpassiveinan"] = self.enEdit.text()
            elif self.gender == 2:
                self.enpartvals["fempresentpassive"] = self.enEdit.text()
            elif self.gender == 3:
                self.enpartvals["nuetpresentpassive"] = self.enEdit.text()
            elif self.gender == 4:
                self.enpartvals["plurpresentpassiveanim"] = self.enEdit.text()
            elif self.gender == 5:
                self.enpartvals["plurpresentpassiveinan"] = self.enEdit.text()
        elif self.tense == 2:
            if self.gender == 0:
                self.enpartvals["mascpastactiveanim"] = self.enEdit.text()
            elif self.gender == 1:
                self.enpartvals["mascpastactiveinan"] = self.enEdit.text()
            elif self.gender == 2:
                self.enpartvals["fempastactive"] = self.enEdit.text()
            elif self.gender == 3:
                self.enpartvals["nuetpastactive"] = self.enEdit.text()
            elif self.gender == 4:
                self.enpartvals["plurpastactiveanim"] = self.enEdit.text()
            elif self.gender == 5:
                self.enpartvals["plurpastactiveinan"] = self.enEdit.text()
        elif self.tense == 3:
            if self.gender == 0:
                self.enpartvals["mascpastpassiveanim"] = self.enEdit.text()
            elif self.gender == 1:
                self.enpartvals["mascpastpassiveinan"] = self.enEdit.text()
            elif self.gender == 2:
                self.enpartvals["fempastpassive"] = self.enEdit.text()
            elif self.gender == 3:
                self.enpartvals["nuetpastpassive"] = self.enEdit.text()
            elif self.gender == 4:
                self.enpartvals["plurpastpassiveanim"] = self.enEdit.text()
            elif self.gender == 5:
                self.enpartvals["plurpastpassiveinan"] = self.enEdit.text()

    def altermascanim(self):
        """ Alter the "masculine animate" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.mascpresentactiveanim = self.verblist
            if self.tense == 1:
                self.mascpresentpassiveanim = self.verblist
        if self.tense == 2:
            self.mascpastactiveanim = self.verblist
        if self.tense == 3:
            self.mascpastpassiveanim = self.verblist
                
    def altermascinan(self):
        """ Alter the "masculine inanimate" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.mascpresentactiveinan = self.verblist
            if self.tense == 1:
                self.mascpresentpassiveinan = self.verblist
        if self.tense == 2:
            self.mascpastactiveinan = self.verblist
        if self.tense == 3:
            self.mascpastpassiveinan = self.verblist

    def alterfem(self):
        """ Alter the "feminine" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.fempresentactive = self.verblist
            if self.tense == 1:
                self.fempresentpassive = self.verblist
        if self.tense == 2:
            self.fempastactive = self.verblist
        if self.tense == 3:
            self.fempastpassive = self.verblist

    def alternuet(self):
        """ Alter the "nueter" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.nuetpresentactive = self.verblist
            if self.tense == 1:
                self.nuetpresentpassive = self.verblist
        if self.tense == 2:
            self.nuetpastactive = self.verblist
        if self.tense == 3:
            self.nuetpastpassive = self.verblist

    def alterpluranim(self):
        """ Alter the "plural animate" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.plurpresentactiveanim = self.verblist
            if self.tense == 1:
                self.plurpresentpassiveanim = self.verblist
        if self.tense == 2:
            self.plurpastactiveanim = self.verblist
        if self.tense == 3:
            self.plurpastpassiveanim = self.verblist

    def alterplurinan(self):
        """ Alter the "plural inanimate" data for the selected tense.
        """
        if self.imperfective:
            if self.tense == 0:
                self.plurpresentactiveinan = self.verblist
            if self.tense == 1:
                self.plurpresentpassiveinan = self.verblist
        if self.tense == 2:
            self.plurpastactiveinan = self.verblist
        if self.tense == 3:
            self.plurpastpassiveinan = self.verblist

    """
            The database template for participles.
            
            CREATE TABLE participles( 
                name text DEFAULT '', 
                runame text DEFAULT '',
                variety prtcpl_var DEFAULT 'past passive' ,
                gender gender_var DEFAULT 'masculine',
                declension text DEFAULT '',
                enval text DEFAULT '',
                wordcase case_var DEFAULT 'nominative',
                );
    """
    
    def accept(self): 
        """ Gather the data from all the lists and create
            a series of SQL commands to insert the data into
            the database and close the GUI.
        """
        for x in range(4):
            y = self.types.participles[x]
            self.partconj[y] = dict()
        sqlpart = dict()
        if self.pastpCheck.isChecked():
            self.parent.enppp = self.enpartvals["mascpastpassiveanim"]
            self.parent.pppend = self.endings[3]
        else:
            self.parent.pppend = ""
        self.enstr = self.parent.enstr
        self.enstr = self.apostrophe(self.enstr)
        sqlpart["name"] = "\'" + self.enstr + "\'"
        sqlpart["runame"] = "\'" + self.parent.rustr + "\'"
        sqlpart["objcase"] = self.parent.sqldict["objcase"]
        if self.imperfective:
            if self.presaCheck.isChecked():
                sqlpart["animate"] = "\'animate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpresentactiveanim"]) + "\'"
                self.addlist(sqlpart, self.mascpresentactiveanim)
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpresentactiveinan"]) + "\'"
                self.addlist(sqlpart, self.mascpresentactiveinan)
            if self.prespCheck.isChecked():
                sqlpart["animate"] = "\'animate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpresentpassiveanim"]) + "\'"
                self.addlist(sqlpart, self.mascpresentpassiveanim)
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpresentpassiveinan"]) + "\'"
                self.addlist(sqlpart, self.mascpresentpassiveinan)
        if self.pastaCheck.isChecked():
            sqlpart["animate"] = "\'animate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'masculine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpastactiveanim"]) + "\'"
            self.addlist(sqlpart, self.mascpastactiveanim)
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'masculine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpastactiveinan"]) + "\'"
            self.addlist(sqlpart, self.mascpastactiveinan)
        if self.pastpCheck.isChecked():
            sqlpart["animate"] = "\'animate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'masculine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpastpassiveanim"]) + "\'"
            self.addlist(sqlpart, self.mascpastpassiveanim)
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'masculine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["mascpastpassiveinan"]) + "\'"
            self.addlist(sqlpart, self.mascpastpassiveinan)
        if self.imperfective:
            if self.presaCheck.isChecked():
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'feminine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["fempresentactive"]) + "\'"
                self.addlist(sqlpart, self.fempresentactive)
            if self.prespCheck.isChecked():
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'feminine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["fempresentpassive"]) + "\'"
                self.addlist(sqlpart, self.fempresentpassive)
        if self.pastaCheck.isChecked():
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'feminine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["fempastactive"]) + "\'"
            self.addlist(sqlpart, self.fempastactive)
        if self.pastpCheck.isChecked():
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'feminine\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["fempastpassive"]) + "\'"
            self.addlist(sqlpart, self.fempastpassive)        
        if self.imperfective:
            if self.presaCheck.isChecked():
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'nueter\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["nuetpresentactive"]) + "\'"
                self.addlist(sqlpart, self.nuetpresentactive)
            if self.prespCheck.isChecked():
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'nueter\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["nuetpresentpassive"]) + "\'"
                self.addlist(sqlpart, self.nuetpresentpassive)
        if self.pastaCheck.isChecked():
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'nueter\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["nuetpastactive"]) + "\'"
            self.addlist(sqlpart, self.nuetpastactive)
        if self.pastpCheck.isChecked():
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'nueter\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["nuetpastpassive"]) + "\'"
            self.addlist(sqlpart, self.nuetpastpassive)
        if self.imperfective:
            if self.presaCheck.isChecked():
                sqlpart["animate"] = "\'animate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'plural\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpresentactiveanim"]) + "\'"
                self.addlist(sqlpart, self.plurpresentactiveanim)
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present active\'"
                sqlpart["gender"] = "\'plural\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpresentactiveinan"]) + "\'"
                self.addlist(sqlpart, self.plurpresentactiveinan)
            if self.prespCheck.isChecked():
                sqlpart["animate"] = "\'animate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'plural\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpresentpassiveanim"]) + "\'"
                self.addlist(sqlpart, self.plurpresentpassiveanim)
                sqlpart["animate"] = "\'inanimate\'"
                sqlpart["variety"] = "\'present passive\'"
                sqlpart["gender"] = "\'plural\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpresentpassiveinan"]) + "\'"
                self.addlist(sqlpart, self.plurpresentpassiveinan)
        if self.pastaCheck.isChecked():
            sqlpart["animate"] = "\'animate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'plural\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpastactiveanim"]) + "\'"
            self.addlist(sqlpart, self.plurpastactiveanim)
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past active\'"
            sqlpart["gender"] = "\'plural\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpastactiveinan"]) + "\'"
            self.addlist(sqlpart, self.plurpastactiveinan)
        if self.pastpCheck.isChecked():
            self.parent.shortpp = True
            self.parent.pppstem = self.stem4
            sqlpart["animate"] = "\'animate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'plural\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpastpassiveanim"]) + "\'"
            self.addlist(sqlpart, self.plurpastpassiveanim)
            sqlpart["animate"] = "\'inanimate\'"
            sqlpart["variety"] = "\'past passive\'"
            sqlpart["gender"] = "\'plural\'"
            sqlpart["enval"] = "\'" + self.apostrophe(self.enpartvals["plurpastpassiveinan"]) + "\'"
            self.addlist(sqlpart, self.plurpastpassiveinan)
        else:
            self.parent.shortpp = False
        for x in self.enpartkeys:
            self.partconj[x] = self.enpartvals[x]
        self.partconj["presaen"] = self.presaCheck.isEnabled()
        self.partconj["prespen"] = self.prespCheck.isEnabled()
        self.partconj["pastaen"] = self.pastaCheck.isEnabled()
        self.partconj["pastpen"] = self.pastpCheck.isEnabled()
        self.partconj["presa"] = self.presaCheck.isChecked()
        self.partconj["presp"] = self.prespCheck.isChecked()
        self.partconj["pasta"] = self.pastaCheck.isChecked()
        self.partconj["pastp"] = self.pastpCheck.isChecked()
        self.partconj["stem1"] = self.thirdpersonplural
        self.partconj["stem2"] = self.firstpersonplural
        self.partconj["stem3"] = self.stem3
        self.partconj["stem4"] = self.stem4
        self.partconj["ending1"] = self.endings[0]
        self.partconj["ending2"] = self.endings[1]
        self.partconj["ending3"] = self.endings[2]
        self.partconj["ending4"] = self.endings[3]
        self.parent.pppstem = self.stem4
        self.parent.shortppp = self.pastpCheck.isChecked()
        self.parent.verbdict["page2"] = self.partconj.copy()
        self.close()
        
    def apostrophe(self, x):
        index = x.find('\'')
        while(index >= 0):
            tmpstr1 = x[:index]
            tmpstr1 += '\''
            tmpstr1 += x[index:]
            x = tmpstr1
            tmpint = index + 2
            index = x.find('\'', tmpint)
        return x

    def addlist(self, sqlpart, partlist):
        """ Create a single SQL command to insert one line of data.
        """
        for q in range(6):
            sqlpart["declension"] = "\'" + partlist[q] + "\'"
            sqlpart["wordcase"] = "\'" + self.types.declension[q + 1] + "\'"
            tmpstr = sqlpart["gender"].strip("\'") + " " + sqlpart["variety"].strip("\'") + " " + sqlpart["animate"].strip("\'") + " " + self.types.declension[q + 1]
            self.partconj[tmpstr] = sqlpart.copy()
                
    def cancel(self):
        """ Cancel the event.
        """
        self.parent.cancel = True
        self.close()
           
    def displayhelp(self):
        """ Display an HTML help page for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def back(self):
        """ Go back one page in the data entry process.
        """
        self.parent.sqllist = list()
        self.parent.back = True
        self.accept()

    def closeEvent(self, event):
        """ Close the GUI and pass along sizing information.
        """
        self.parent.geometry = self.geometry
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()            