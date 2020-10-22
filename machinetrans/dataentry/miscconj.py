#!/usr/bin/python3
"""
    MiscConj:  Machine Translation Data Entry -- Miscellaneous Conjugations.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 16, 2016, San Diego California United States of America
"""
import os, sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_miscconj import Ui_MiscConj
from machinetrans.data.wordmorph import WordMorph
from machinetrans.helpview import HelpView

class MiscConj(QDialog, Ui_MiscConj):
    """ A GUI to enter miscellaneous conjugations
        of Russian verbs. In particular the short form of 
        the past passive participle, the verbal adverb,
        and the imperatives.
    """
    
    helpfile = "/usr/share/machinetrans/resources/miscconj.html"
    parent = None
    labeltext = ""
    rustr = ""
    enstr = ""
    thirdpersonplural = ""
    firstpersonsingular = ""
    shortppp = True
    paststem = ""
    pppstem = ""
    pppend = ""
    adverbstem = ""
    verbaladverb = True
    pastadverb1 = ""
    pastadverb2 = ""
    adverbstem = ""
    presentadverb = ""
    enpastpassive = ""
    reflexive = False
    oneself = False
    imperfective = True
    sqlcommand = ""
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    morphs = None
    imperative = True
    quote = "\'"
    miscconj = dict()
    def __init__(self, parent=None):
        """ Initialize the GUI and fill it with data.
        """
        super(MiscConj, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        if self.parent.verbpages[3]:
            self.miscconj = self.parent.verbdict["page4"].copy()
            del self.parent.verbdict["page4"]
        else:
            self.miscconj.clear()
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        self.pppend = self.parent.pppend
        self.thirdpersonplural = self.parent.thirdpersonplural
        self.firstpersonsingular = self.parent.firstpersonsingular
        self.paststem = self.parent.paststem
        self.enpastpassive = self.parent.enppp
        self.shortppp = self.parent.shortppp
        # Imperfective verbs and perfective verbs have different verbal adverbs among other things.
        self.imperfective = self.parent.sqldict["imperfective"] == "\'imperfective\'"
        self.oneself = self.parent.oneself
        # Check for a reflexive verb.
        endchars = self.rustr[-2:]
        if endchars == "ся" or endchars == "сь":
            self.reflexive = True
            self.thirdpersonplural = self.thirdpersonplural[:-2]
            self.rustr = self.rustr[:-2]
        self.quitBttn.clicked.connect(self.cancel)
        self.backBttn.clicked.connect(self.back)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.advCheck.stateChanged.connect(self.changeAdv)
        self.spppCheck.stateChanged.connect(self.changesppp)
        self.impCheck.stateChanged.connect(self.imperativechg)
        self.stemEdit.firereturn.triggered.connect(self.adjstem)
        self.stemEdit.firefocus.triggered.connect(self.adjstem)
        self.mascEdit.firereturn.triggered.connect(self.setmasc)
        self.mascEdit.firefocus.triggered.connect(self.setmasc)
        self.femEdit.firereturn.triggered.connect(self.setfem)
        self.femEdit.firefocus.triggered.connect(self.setfem)
        self.nuetEdit.firereturn.triggered.connect(self.setnuet)
        self.nuetEdit.firefocus.triggered.connect(self.setnuet)
        self.plurEdit.firereturn.triggered.connect(self.setplur)
        self.plurEdit.firefocus.triggered.connect(self.setplur)
        self.enPresAdvEdit.firereturn.triggered.connect(self.setenpresadv)
        self.enPresAdvEdit.firefocus.triggered.connect(self.setenpresadv)
        self.enPastAdvEdit.firereturn.triggered.connect(self.setenpastadv)
        self.enPastAdvEdit.firefocus.triggered.connect(self.setenpastadv)
        self.presAdv.firereturn.triggered.connect(self.setrupresadv)
        self.presAdv.firefocus.triggered.connect(self.setrupresadv)
        self.pastAdv.firereturn.triggered.connect(self.setrupastadv1)
        self.pastAdv.firefocus.triggered.connect(self.setrupastadv1)
        self.pastAdv1.firereturn.triggered.connect(self.setrupastadv2)
        self.pastAdv1.firefocus.triggered.connect(self.setrupastadv2)
        self.enPPPEdit.firereturn.triggered.connect(self.setenppp)
        self.enPPPEdit.firefocus.triggered.connect(self.setenppp)
        self.enPPPEdit.setText(self.enpastpassive)
        ovat = False
        if self.parent.verbpages[3]:
            self.verbaladverb = self.miscconj["verbaladverb"]
            if self.verbaladverb:
                self.advCheck.setChecked(True)
                if self.miscconj["presadv"]:
                    self.presentadverb = self.miscconj["masculine present verbal adverb"]["declension"].strip("\'")
                    self.enpresadverb = self.miscconj["masculine present verbal adverb"]["enval"].strip("\'")
                    self.enPresAdvEdit.setText(self.enpresadverb)
                    self.presAdv.setText(self.presentadverb)
                if self.miscconj["pastadv1"]:
                    self.pastadverb1 = self.miscconj["masculine past verbal adverb 1"]["declension"].strip("\'")
                    self.pastAdv.setText(self.pastadverb1)
                if self.miscconj["pastadv2"]:
                    self.pastadverb2 = self.miscconj["masculine past verbal adverb 2"]["declension"].strip("\'")
                    self.pastAdv1.setText(self.pastadverb2)
                if self.miscconj["pastadv1"] or self.miscconj["pastadv2"]:
                    self.enpastadverb = self.miscconj["masculine past verbal adverb 2"]["enval"].strip("\'")
                if self.miscconj["pastadv1"] or self.miscconj["pastadv2"]:
                    self.enPastAdvEdit.setText(self.enpastadverb)
                if self.miscconj["imperative"]:
                    self.imperative = True
                    self.impCheck.setChecked(True)
                    if self.miscconj["fimperative"]:
                        self.enImpEdit.setText(self.miscconj["plural formal imperative"]["enval"].strip("\'"))
                    if self.miscconj["infimperative"]:
                        self.enImpEdit.setText(self.miscconj["masculine informal imperative"]["enval"].strip("\'"))
                else:
                    self.imperative = False
            else:
                self.verbaladverb = False
                self.advCheck.setChecked(False)
                self.enPresAdvEdit.setText("")
                self.enPresAdvEdit.setEnabled(False)
                self.enPastAdvEdit.setText("")
                self.enPastAdvEdit.setEnabled(False)
                self.presAdv.setText("")
                self.presAdv.setEnabled(False)
                self.pastAdv.setText("")
                self.pastAdv.setEnabled(False)
                self.pastAdv1.setText("")
                self.pastAdv1.setEnabled(False)
        else:
            self.miscconj["masculine present verbal adverb"] = dict()
            self.miscconj["masculine past verbal adverb 1"] = dict()
            self.miscconj["masculine past verbal adverb 2"] = dict()
            self.miscconj["plural formal imperative"] = dict()
            self.miscconj["masculine informal imperative"] = dict()
            if self.shortppp:
                self.miscconj["masculine short past passive"] = dict()
                self.miscconj["feminine short past passive"] = dict()
                self.miscconj["nueter short past passive"] = dict()
                self.miscconj["plural short past passive"] = dict()
                self.miscconj["pppstem"] = ""
            self.engconj()
            if len(self.rustr) > 5:
                ending = self.rustr[-5:]
                if ending == "овать" or ending == "евать":
                    ovat = True
                    self.pastadverb1 = self.rustr[:-2] + self.morphs.vrbadvb[3]
                    self.pastadverb2 = self.rustr[:-2] + self.morphs.vrbadvb[5]
                    if self.imperfective:
                        self.presentadverb = self.rustr[:-5] + "у" + self.morphs.vrbadvb[2]
                    if self.reflexive:
                        self.pastadverb1 += "сь"
                        self.pastadverb2 += "сь"
                        if self.imperfective:
                            self.presentadverb += "сь"
            self.adverbstem = self.thirdpersonplural[:-2]
            if not ovat:
                if (len(self.adverbstem) > 2):
                    endchars = self.adverbstem[-1]
                # Determine the verbal adverb.
                if self.reflexive:
                    if self.imperfective:
                        if endchars in self.morphs.sybillants:
                            self.presentadverb = self.adverbstem + self.morphs.vrbadvb[1] + "сь"
                        else:
                            self.presentadverb = self.adverbstem + self.morphs.vrbadvb[2] + "сь"
                    self.adverbstem = self.paststem
                    self.pastadverb1 = self.adverbstem + self.morphs.vrbadvb[3] + "ся"
                    self.pastadverb2 = self.adverbstem + self.morphs.vrbadvb[5] + "сь"
                else:
                    if self.imperfective:
                        if endchars in self.morphs.sybillants:
                            self.presentadverb = self.adverbstem + self.morphs.vrbadvb[1]
                        else:
                            self.presentadverb = self.adverbstem + self.morphs.vrbadvb[2]
                    self.adverbstem = self.paststem
                    self.pastadverb1 = self.adverbstem + self.morphs.vrbadvb[3]
                    self.pastadverb2 = self.adverbstem + self.morphs.vrbadvb[5]
            self.presAdv.setText(self.presentadverb)
            self.pastAdv.setText(self.pastadverb1)
            self.pastAdv1.setText(self.pastadverb2)
            self.miscconj["masculine present verbal adverb"]["declension"] = self.presentadverb
            self.miscconj["masculine present verbal adverb"]["enval"] = self.parent.enpresadv
            self.presAdv.setText(self.presentadverb)
            self.miscconj["masculine past verbal adverb 1"]["declension"] = self.pastadverb1
            self.miscconj["masculine past verbal adverb 1"]["enval"] = self.parent.enpastadv
            self.pastAdv.setText(self.pastadverb1)
            self.miscconj["masculine past verbal adverb 2"]["declension"] = self.pastadverb2
            self.miscconj["masculine past verbal adverb 2"]["enval"] = self.parent.enpastadv
            self.pastAdv1.setText(self.pastadverb2)
        if self.parent.verbpages[3]:
            self.shortppp = self.miscconj["shortppp"]
            if self.shortppp:
                self.enPPPEdit.setFocus()
                self.spppCheck.setChecked(True)
                self.mascEdit.setText(self.miscconj["masculine short past passive"]["declension"].strip("\'"))
                self.enPPPEdit.setText(self.miscconj["masculine short past passive"]["enval"].strip("\'")) 
                self.femEdit.setText(self.miscconj["feminine short past passive"]["declension"].strip("\'"))
                self.nuetEdit.setText(self.miscconj["nueter short past passive"]["declension"].strip("\'"))
                self.plurEdit.setText(self.miscconj["plural short past passive"]["declension"].strip("\'"))
                self.stemEdit.setText(self.miscconj["pppstem"].strip("\'"))
            else:
                self.spppCheck.setChecked(False)
                self.mascEdit.setText("")
                self.mascEdit.setEnabled(False)
                self.enPPPEdit.setText("") 
                self.enPPPEdit.setEnabled(False) 
                self.femEdit.setText("")
                self.femEdit.setEnabled(False) 
                self.nuetEdit.setText("")
                self.nuetEdit.setEnabled(False)
                self.plurEdit.setText("")
                self.plurEdit.setEnabled(False)
                self.stemEdit.setText("")
                self.stemEdit.setEnabled(False)
        else:
            if self.shortppp:
                self.shortpppconj()
                self.spppCheck.setChecked(True)
                self.mascEdit.setText(self.miscconj["masculine short past passive"]["declension"].strip("\'"))
                self.enPPPEdit.setText(self.miscconj["masculine short past passive"]["enval"].strip("\'")) 
                self.femEdit.setText(self.miscconj["feminine short past passive"]["declension"].strip("\'"))
                self.nuetEdit.setText(self.miscconj["nueter short past passive"]["declension"].strip("\'"))
                self.plurEdit.setText(self.miscconj["plural short past passive"]["declension"].strip("\'"))
                self.stemEdit.setText(self.miscconj["pppstem"].strip("\'"))
            else:
                self.spppCheck.setChecked(False)
                self.mascEdit.setText("")
                self.mascEdit.setEnabled(False)
                self.enPPPEdit.setText("") 
                self.enPPPEdit.setEnabled(False) 
                self.femEdit.setText("")
                self.femEdit.setEnabled(False) 
                self.nuetEdit.setText("")
                self.nuetEdit.setEnabled(False)
                self.plurEdit.setText("")
                self.nuetEdit.setEnabled(False)
                self.plurEdit.setText("")
                self.stemEdit.setEnabled(False)

        if self.parent.verbpages[3]:
            if self.miscconj["imperative"]:
                self.impCheck.setChecked(True)
                if self.miscconj["infimperative"]:
                    self.ruInfImpEdit.setText(self.miscconj["masculine informal imperative"]["declension"].strip("\'"))
                if self.miscconj["fimperative"]:
                    self.ruFormImpEdit.setText(self.miscconj["plural formal imperative"]["declension"].strip("\'"))
                if self.miscconj["infimperative"] or self.miscconj["fimperative"]:
                    if self.miscconj.get("plural formal imperative"):
                        self.enImpEdit.setText(self.miscconj["plural formal imperative"]["enval"].strip("\'"))
                    else:
                        self.enImpEdit.setText(self.miscconj["masculine informal imperative"]["enval"].strip("\'"))
            else:
                self.impCheck.setChecked(False)
                self.ruInfImpEdit.setEnabled(False)
                self.ruFormImpEdit.setEnabled(False)
                self.enImpEdit.setEnabled(False)
        else:
            self.impCheck.setChecked(True)
            # Obtain the stem of the first person singular of the verb.
            if self.reflexive:
                self.firstpersonsingular = self.firstpersonsingular[:-2]
            # Correct for consonant change in the first person.
            index1 = 0
            index2 = 0
            for x in range(len(self.parent.presstem) - 1, 0, -1):
                if self.parent.presstem[x] in self.morphs.consonants:
                    index1 = x
                    break
            for x in range(len(self.firstpersonsingular) - 1, 0, -1):
                if self.firstpersonsingular[x] in self.morphs.consonants:
                    index2 = x
                    break
            if self.firstpersonsingular[index2] != 'г':
                charitem = self.parent.presstem[index1]
                tmpstr = self.firstpersonsingular[:index2]
                tmpstr += charitem
                index2 += 1
                tmpstr += self.firstpersonsingular[index2:]
                self.firstpersonsingular = tmpstr
            # Calculate the imperative.
            self.imperative = True
            # Calculate the imperative.
            # Test for verbs ending in "ить" and "и," first checking for a reflexive verb.
            if self.rustr.endswith("ся") or self.rustr.endswith("сь"):
                verbtmp = self.rustr[:-2]
            else:
                verbtmp = self.rustr
            if verbtmp[-3:] == 'ить' or verbtmp[-2:] == 'ти':
                if verbtmp[-3:] == 'ить':
                    tmpstr = verbtmp[:-3]
                else:
                    tmpstr = verbtmp[:-2]
                tmpstr1 = tmpstr + "и"
                self.ruInfImpEdit.setText(tmpstr1)
                tmpstr1 = tmpstr + "ите"
                self.ruFormImpEdit.setText(tmpstr1)
            else:
                tmpstr = self.firstpersonsingular[:-1]
                if (tmpstr[-1] in self.morphs.consonants):
                    tmpstr1 = tmpstr + "и"
                    self.ruInfImpEdit.setText(tmpstr1)
                    tmpstr1 = tmpstr + "ите"
                    self.ruFormImpEdit.setText(tmpstr1)
                else:
                    tmpstr1 = tmpstr + self.morphs.vrbimp[1]
                    self.ruInfImpEdit.setText(tmpstr1)
                    tmpstr1 = tmpstr + self.morphs.vrbimp[2]
                    self.ruFormImpEdit.setText(tmpstr1)
            if self.reflexive:
                tmpstr = self.ruInfImpEdit.text()
                tmpstr += "сь"
                self.ruInfImpEdit.setText(tmpstr)
                tmpstr = self.ruFormImpEdit.text()
                tmpstr += "сь"
                self.ruFormImpEdit.setText(tmpstr)
            self.miscconj["masculine informal imperative"]["declension"] = self.ruInfImpEdit.text()
            self.miscconj["plural formal imperative"]["declension"] = self.ruFormImpEdit.text()
            self.miscconj["plural formal imperative"]["enval"] = self.enImpEdit.text()
            self.miscconj["masculine informal imperative"]["enval"] = self.enImpEdit.text()
        self.parent.verbpages[3] = True
        
    def shortpppconj(self):
        self.pppstem = self.parent.pppstem
        self.pppend = self.parent.pppend
        self.stemEdit.setText(self.pppstem)
        # Determine the short for of the past passive participle, if any.
        if self.pppend == 'нн':
            self.pppend = 'н'
        if self.reflexive:
            self.miscconj["masculine short past passive"]["declension"] = self.pppstem + self.pppend + "ся"
            self.miscconj["feminine short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[2] + "сь"
            self.miscconj["nueter short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[3] + "сь"
            self.miscconj["plural short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[4] + "сь"
        else:
            self.miscconj["masculine short past passive"]["declension"] = self.pppstem + self.pppend
            self.miscconj["feminine short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[2]
            self.miscconj["nueter short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[3]
            self.miscconj["plural short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[4]
        self.miscconj["pppstem"] = self.stemEdit.text()
        self.miscconj["masculine short past passive"]["enval"] = self.enpastpassive
        self.miscconj["feminine short past passive"]["enval"] = self.enpastpassive
        self.miscconj["nueter short past passive"]["enval"] = self.enpastpassive
        self.miscconj["plural short past passive"]["enval"] = self.enpastpassive
    
            
    def engconj(self):
        """ Conjugate the english word data and display it.
        """
        if self.parent.verbpages[3]:
            return
        else:
            verb = self.parent.enpasttense
            if self.enstr[:6] == "to be ":
                if self.imperfective:
                    if self.oneself:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "being " + verb + " yourself"
                        self.enPresAdvEdit.setText(self.miscconj["masculine present verbal adverb"]["enval"].strip("\'"))
                    else:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "being " + verb
                        self.enPresAdvEdit.setText(self.miscconj["masculine present verbal adverb"]["enval"].strip("\'"))
                if self.oneself:
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "having been " + verb + " yourself"
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "having been " + verb + " yourself"
                else:
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "having been " + verb
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "having been " + verb
                self.enPastAdvEdit.setText(self.miscconj["masculine past verbal adverb 2"]["enval"].strip("\'"))
                if self.imperative:
                    tmpstr = self.enstr[6:]
                    if self.oneself:
                        tmpstr = tmpstr[:-8]
                        self.miscconj["masculine informal imperative"]["enval"] = "be " + tmpstr + " yourself"
                        self.miscconj["plural formal imperative"]["enval"] = "be " + tmpstr + " yourself"
                    else:
                        self.miscconj["masculine informal imperative"]["enval"] = "be " + tmpstr
                        self.miscconj["plural formal imperative"]["enval"] = "be " + tmpstr
                    self.enImpEdit.setText(self.miscconj["masculine informal imperative"]["enval"].strip("\'"))
            elif self.enstr[:8] == "to have ":
                if self.imperfective:
                    if self.oneself:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "having " + verb + " yourself"
                    else:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "having " + verb
                    self.enPresAdvEdit.setText(self.miscconj["masculine present verbal adverb"]["enval"].strip("\'"))
                if self.oneself:
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "was having " + verb + " yourself"
                else:
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "was having " + verb
                if self.oneself:
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "was having " + verb + " yourself"
                else:
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "was having " + verb
                self.enPastAdvEdit.setText(self.miscconj["masculine past verbal adverb 1"]["enval"].strip("\'"))
                if self.imperative:
                    tmpstr = self.enstr[8:]
                    if self.oneself:
                        tmpstr = tmpstr[:-8]
                        self.miscconj["masculine informal imperative"]["enval"] = "have " + tmpstr + " yourself"
                        self.miscconj["plural formal imperative"]["enval"] = "have " + tmpstr + " yourself"
                    else:
                        self.miscconj["masculine informal imperative"]["enval"] = "have " + tmpstr
                        self.miscconj["plural formal imperative"]["enval"] = "have " + tmpstr
                    self.enImpEdit.setText(self.miscconj["masculine informal imperative"]["enval"].strip("\'"))
            else:
                if self.imperfective:
                    if self.oneself:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "is " + verb + " yourself"
                    else:
                        self.miscconj["masculine present verbal adverb"]["enval"] = "is " + verb
                    self.enPresAdvEdit.setText(self.miscconj["masculine present verbal adverb"]["enval"].strip("\'"))
                if self.imperative:
                    tmpstr = self.enstr[3:] # "to "
                    if self.oneself:
                        tmpstr = tmpstr[:-8]
                        self.miscconj["masculine informal imperative"]["enval"] = tmpstr + " yourself"
                        self.miscconj["plural formal imperative"]["enval"] = tmpstr + " yourself"
                    else:
                        self.miscconj["masculine informal imperative"]["enval"] = tmpstr
                        self.miscconj["plural formal imperative"]["enval"] = tmpstr
                    self.enImpEdit.setText(self.miscconj["masculine informal imperative"]["enval"].strip("\'"))
                if self.oneself:
                    verb = verb[:-8]
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "was " + verb + " yourself"
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "was " + verb + " yourself"
                else:
                    self.miscconj["masculine past verbal adverb 1"]["enval"] = "was " + verb
                    self.miscconj["masculine past verbal adverb 2"]["enval"] = "was " + verb
                self.enPastAdvEdit.setText(self.miscconj["masculine past verbal adverb 1"]["enval"].strip("\'"))
    
    def resizeEvent(self, event):
        """ Resize the GUI and save the sizing data.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 / 600
        wscale = self.width1 / 800
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 - 260) / 2
        self.spppCheck.setGeometry(tmpx, 20, 260, 25)
        tmpy = 50 * hscale
        tmpx = (self.width1 - 700) / 2
        self.enPPPLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.enPPPEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 80 * hscale
        tmpx = (self.width1 - 700) / 2
        self.stemLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.stemEdit.setGeometry(tmpx,tmpy, 330, 25)
        tmpy = 110 * hscale
        tmpx = (self.width1 - 700) / 2
        self.mascLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.femLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 20 * hscale
        tmpx = (self.width1 - 700) / 2
        self.mascEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 20
        self.femEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 160 * hscale
        tmpx = (self.width1 - 700) / 2
        self.nuetLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.plurLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 20 * hscale
        tmpx = (self.width1 - 700) / 2
        self.nuetEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 20
        self.plurEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 220 * hscale
        tmpx = (self.width1 / 2) - 100
        self.advCheck.setGeometry(tmpx, tmpy, 200, 25)
        tmpy = 250 * hscale
        tmpx = (self.width1 - 700) / 2
        self.enPresAdvLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.enPresAdvEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 280 * hscale
        tmpx = (self.width1 - 700) / 2
        self.enPastAdvLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.enPastAdvEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 700) / 2
        tmpy = 310 * hscale
        self.pastAdvLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.pastAdv.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy = 340 * hscale
        self.pastAdvLbl1.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.pastAdv1.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy = 370 * hscale
        self.presAdvLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.presAdv.setGeometry(tmpx, tmpy, 330, 25)
        tmpy = 400 * hscale
        tmpx = (self.width1 / 2) - 100
        self.impCheck.setGeometry(tmpx, tmpy, 200, 25)
        tmpx = (self.width1 - 700) / 2
        tmpy = 430 * hscale
        self.enImpLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.enImpEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = 460 * hscale
        tmpx = (self.width1 - 700) / 2
        self.ruInfImpLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 / 2) + 20
        self.ruFormImpLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpy += 30 * hscale
        tmpx = (self.width1 - 700) / 2
        self.ruInfImpEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 20
        self.ruFormImpEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 570) / 2
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 - 150) / 2
        self.backBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + 120
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
        
    def adjstem(self):
        """ Account for a change in the stem editor for the short form past passive participle.
        """
        self.pppstem = self.stemEdit.text()
        if self.reflexive:
            self.miscconj["masculine short past passive"]["declension"] = self.pppstem + self.pppend + "ся"
            self.mascEdit.setText(self.miscconj["masculine short past passive"]["declension"].strip("\'"))
            self.miscconj["feminine short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[2] + "сь" 
            self.femEdit.setText(self.miscconj["feminine short past passive"]["declension"].strip("\'"))
            self.miscconj["nueter short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[3] + "сь"
            self.nuetEdit.setText(self.miscconj["nueter short past passive"]["declension"].strip("\'"))
            self.miscconj["plural short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[4] + "сь"
            self.plurEdit.setText(self.miscconj["plural short past passive"]["declension"].strip("\'"))
        else:
            self.miscconj["masculine short past passive"]["declension"] = self.pppstem + self.pppend
            self.mascEdit.setText(self.miscconj["masculine short past passive"]["declension"].strip("\'"))
            self.miscconj["feminine short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[2]
            self.femEdit.setText(self.miscconj["feminine short past passive"]["declension"].strip("\'"))
            self.miscconj["nueter short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[3]
            self.nuetEdit.setText(self.miscconj["nueter short past passive"]["declension"].strip("\'"))
            self.miscconj["plural short past passive"]["declension"] = self.pppstem + self.pppend + self.morphs.pppart[4]
            self.plurEdit.setText(self.miscconj["plural short past passive"]["declension"].strip("\'"))
    
    def setmasc(self):
        """ Get a changed Russian masculine short past passive participle.
        """
        self.miscconj["masculine short past passive"]["declension"] = self.mascEdit.text()
     
    def setfem(self):
        """ Get a changed Russian feminine short past passive participle.
        """
        self.miscconj["feminine short past passive"]["declension"] = self.femEdit.text()
        
    def setnuet(self):
        """ Get a changed Russian nueter short past passive participle.
        """
        self.miscconj["nueter short past passive"]["declension"] = self.nuetEdit.text()
        
    def setplur(self):
        """ Get a changed Russian plural short past passive participle.
        """
        self.miscconj["plural short past passive"]["declension"] = self.plurEdit.text()
        
    def setenpresadv(self):
        """ Get a changed English present tense verbal adverb.
        """
        self.miscconj["masculine present verbal adverb"]["enval"] = self.enPresAdvEdit.text()
        
    def setenpastadv(self):
        """ Get a changed English past tense verbal adverb.
        """
        self.miscconj["masculine past verbal adverb 1"]["enval"] = self.enPastAdvEdit.text()
        self.miscconj["masculine past verbal adverb 2"]["enval"] = self.enPastAdvEdit.text()
    
    def setrupresadv(self):
        """ Get a changed Russian present tense verbal adverb.
        """
        self.miscconj["masculine present verbal adverb"]["declension"] = self.presAdv.text()
        
    def setrupastadv1(self):
        """ Get a changed Russian past tense verbal adverb.
        """
        self.miscconj["masculine past verbal adverb 1"]["declension"] = self.pastAdv.text()
    
    def setrupastadv2(self):
        """ Get a changed Russian past tense verbal adverb.
        """
        self.miscconj["masculine past verbal adverb 2"]["declension"] = self.pastAdv1.text()
        
    def setenppp(self):
        """ Get a changed English past passive participle.
        """
        self.enpastpassive = self.enPPPEdit.text()
    
    def accept(self):
        """ Gather the data and create and SQL command to insert it into
            the database.  Close the form.
        """
        self.miscconj["verbaladverb"] = self.advCheck.isChecked()
        self.verbaladverb = self.advCheck.isChecked()
        self.miscconj["shortppp"] = self.spppCheck.isChecked()
        self.shortppp = self.spppCheck.isChecked()
        self.miscconj["imperative"] = self.impCheck.isChecked()
        sqlpart = dict()
        sqlpart["name"] = "\'" + self.apostrophe(self.parent.enstr) + "\'"
        sqlpart["runame"] = "\'" + self.parent.rustr + "\'"
        sqlpart["objcase"] = self.parent.sqldict["objcase"]
        sqlpart["animate"] = "\'animate\'"
        self.enpastpassive = self.enPPPEdit.text()
        self.enpastpassive = self.apostrophe(self.enpastpassive)
        if self.shortppp:
            sqlpart["variety"] = "\'short past passive\'"
            sqlpart["gender"] = "\'masculine\'"
            sqlpart["enval"] = "\'" + self.enpastpassive + "\'"
            sqlpart["declension"] = "\'" + self.mascEdit.text() + "\'"
            sqlpart["wordcase"] = "\'nominative\'"
            self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            sqlpart["variety"] = "\'short past passive\'"
            sqlpart["gender"] = "\'feminine\'"
            sqlpart["enval"] = "\'" + self.enpastpassive + "\'"
            sqlpart["declension"] = "\'" + self.femEdit.text() + "\'"
            sqlpart["wordcase"] = "\'nominative\'"
            self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            sqlpart["variety"] = "\'short past passive\'"
            sqlpart["gender"] = "\'nueter\'"
            sqlpart["enval"] = "\'" + self.enpastpassive + "\'"
            sqlpart["declension"] = "\'" + self.nuetEdit.text() + "\'"
            sqlpart["wordcase"] = "\'nominative\'"
            self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            sqlpart["variety"] = "\'short past passive\'"
            sqlpart["gender"] = "\'plural\'"
            sqlpart["enval"] = "\'" + self.enpastpassive + "\'"
            sqlpart["declension"] = "\'" + self.plurEdit.text() + "\'"
            sqlpart["wordcase"] = "\'nominative\'"
            self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            self.miscconj["pppstem"] = self.stemEdit.text()
        elif self.miscconj.get("masculine short past passive"):
            del self.miscconj["masculine short past passive"]
            del self.miscconj["feminine short past passive"]
            del self.miscconj["nueter short past passive"]
            del self.miscconj["plural short past passive"]
            del self.miscconj["pppstem"]
        if self.verbaladverb:
            tmpstr = self.presAdv.text()
            if len(tmpstr) > 0:
                sqlpart["variety"] = "\'present verbal adverb\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enPresAdvEdit.text()) + "\'"
                sqlpart["declension"] = "\'" + tmpstr + "\'"
                sqlpart["wordcase"] = "\'nominative\'"
                self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
                self.miscconj["presadv"] = True
            else:
                if self.miscconj.get("masculine present verbal adverb"):
                    del self.miscconj["masculine present verbal adverb"]
                self.miscconj["presadv"] = False
            tmpstr = self.pastAdv.text()
            if len(tmpstr) > 0:
                sqlpart["variety"] = "\'past verbal adverb 1\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enPastAdvEdit.text()) + "\'"
                sqlpart["declension"] = "\'" + tmpstr + "\'"
                sqlpart["wordcase"] = "\'nominative\'"
                self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
                self.miscconj["pastadv1"] = True
            else:
                if self.miscconj.get("masculine past verbal adverb 1"):
                    del self.miscconj["masculine past verbal adverb 1"]
                self.miscconj["pastadv1"] = False
            tmpstr = self.pastAdv1.text()
            if len(tmpstr) > 0:
                sqlpart["variety"] = "\'past verbal adverb 2\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enPastAdvEdit.text()) + "\'"
                sqlpart["declension"] = "\'" + tmpstr + "\'"
                sqlpart["wordcase"] = "\'nominative\'"
                self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
                self.miscconj["pastadv2"] = True
            else:
                if self.miscconj.get("masculine past verbal adverb 2"):
                    del self.miscconj["masculine past verbal adverb 2"]    
                self.miscconj["pastadv2"] = False
        else:
            del self.miscconj["masculine present verbal adverb"]
            del self.miscconj["masculine past verbal adverb 1"]
            del self.miscconj["masculine past verbal adverb 2"]
        if self.miscconj["imperative"]:
            tmpstr = self.ruInfImpEdit.text()
            if len(tmpstr) > 0:
                self.miscconj["infimperative"] = True
                sqlpart["variety"] = "\'informal imperative\'"
                sqlpart["gender"] = "\'masculine\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enImpEdit.text()) + "\'"
                sqlpart["declension"] = "\'" + tmpstr + "\'"
                sqlpart["wordcase"] = "\'nominative\'"
                self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            else:
                if self.miscconj.get("masculine informal imperative"):
                    del self.miscconj["masculine informal imperative"]
                self.miscconj["infimperative"] = False
            tmpstr = self.ruFormImpEdit.text()
            if len(tmpstr) > 0:
                self.miscconj["fimperative"] = True
                sqlpart["variety"] = "\'formal imperative\'"
                sqlpart["gender"] = "\'plural\'"
                sqlpart["enval"] = "\'" + self.apostrophe(self.enImpEdit.text()) + "\'"
                sqlpart["declension"] = "\'" + tmpstr + "\'"
                sqlpart["wordcase"] = "\'nominative\'"
                self.miscconj[sqlpart["gender"].strip(self.quote) + " " + sqlpart["variety"].strip(self.quote)] = sqlpart.copy()
            else:
                if self.miscconj.get("plural formal imperative"):
                    del self.miscconj["plural formal imperative"]
                self.miscconj["fimperative"] = False
        else:
            if self.miscconj.get("masculine informal imperative"):
                del self.miscconj["masculine informal imperative"]
            self.miscconj["infimperative"] = False
            if self.miscconj.get("plural formal imperative"):
                del self.miscconj["plural formal imperative"]
            self.miscconj["fimperative"] = False
            
        self.parent.verbdict["page4"] = self.miscconj.copy()
        self.close()
        
    def apostrophe(self, x):
        """ Echo the apostrophes found in an English word ''
            so they can be put in the database.
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
    
    def changeAdv(self):
        """ Account for setting and unsetting the 
            verbal adverb check box.
        """
        if not self.advCheck.isChecked():
            self.verbaladverb = False
            self.enPresAdvEdit.setText("")
            self.enPresAdvEdit.setEnabled(False)
            self.enPastAdvEdit.setText("")
            self.enPastAdvEdit.setEnabled(False)
            self.presAdv.setText("")
            self.presAdv.setEnabled(False)
            self.pastAdv.setText("")
            self.pastAdv.setEnabled(False)
            self.pastAdv1.setText("")
            self.pastAdv1.setEnabled(False)
        else:
            self.verbaladverb = True
            if self.miscconj.get("masculine present verbal adverb"):
                del self.miscconj["masculine present verbal adverb"]
            if self.miscconj.get("masculine past verbal adverb 1"):
                del self.miscconj["masculine past verbal adverb 1"]
            if self.miscconj.get("masculine past verbal adverb 2"):
                del self.miscconj["masculine past verbal adverb 2"]
            self.enPresAdvEdit.setEnabled(True)
            self.enPresAdvEdit.setText(self.enapresdverb)
            self.enPastAdvEdit.setEnabled(True)
            self.enPastAdvEdit.setText(self.enpastadverb)
            self.presAdv.setEnabled(True)
            self.presAdv.setText(self.presentadverb)
            self.pastAdv.setEnabled(True)
            self.pastAdv.setText(self.pastadverb1)
            self.pastAdv1.setEnabled(True)
            self.pastAdv1.setText(self.pastadverb2)
    
    def changesppp(self):
        """ Allow for setting and unsetting the short past passive participle
            check box.
        """
        if self.spppCheck.isChecked():
            self.shortppp = True
            self.shortpppconj()
            self.spppCheck.setChecked(True)
            self.mascEdit.setEnabled(True)
            self.mascEdit.setText(self.miscconj["masculine short past passive"]["declension"].strip("\'"))
            self.enPPPEdit.setEnabled(True) 
            self.enPPPEdit.setText(self.miscconj["masculine short past passive"]["enval"].strip("\'")) 
            self.femEdit.setEnabled(True) 
            self.femEdit.setText(self.miscconj["feminine short past passive"]["declension"].strip("\'"))
            self.nuetEdit.setEnabled(True)
            self.nuetEdit.setText(self.miscconj["nueter short past passive"]["declension"].strip("\'"))
            self.plurEdit.setEnabled(True)
            self.plurEdit.setText(self.miscconj["plural short past passive"]["declension"].strip("\'"))
            self.stemEdit.setEnabled(True)
            self.stemEdit.setText(self.miscconj["pppstem"].strip("\'"))
        else:
            if self.miscconj.get("masculine short past passive"):
                del self.miscconj["masculine short past passive"]
                del self.miscconj["feminine short past passive"]
                del self.miscconj["nueter short past passive"]
                del self.miscconj["plural short past passive"]
                del self.miscconj["pppstem"]
                
            self.shortppp = False
            self.spppCheck.setChecked(False)
            self.mascEdit.setText("")
            self.mascEdit.setEnabled(False)
            self.enPPPEdit.setText("") 
            self.enPPPEdit.setEnabled(False) 
            self.femEdit.setText("")
            self.femEdit.setEnabled(False) 
            self.nuetEdit.setText("")
            self.nuetEdit.setEnabled(False)
            self.plurEdit.setText("")
            self.plurEdit.setEnabled(False)
            self.stemEdit.setText("")
            self.stemEdit.setEnabled(False)

    def imperativechg(self):
        """ Allow for setting and unsetting the imperative check box.
        """
        if self.impCheck.isChecked():
            self.miscconj["imperative"] = True
            self.impCheck.setChecked(True)
            self.ruInfImpEdit.setText(self.miscconj["masculine informal imperative"]["declension"].strip("\'"))
            self.ruFormImpEdit.setText(self.miscconj["plural formal imperative"]["declension"].strip("\'"))
            self.enImpEdit.setText(self.miscconj["plural formal imperative"]["enval"].strip("\'"))
        else:
            self.miscconj["imperative"] = False
            self.ruInfImpEdit.setText("")
            self.ruInfImpEdit.setEnabled(False)
            self.ruFormImpEdit.setText("")
            self.ruFormImpEdit.setEnabled(False)
            self.enImpEdit.setText("")
            self.enImpEdit.setEnabled(False)

    def displayhelp(self):
        """ Display a help page for this gui in HTML.
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