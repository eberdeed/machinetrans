#!/usr/bin/python3
"""
    DataEntry:  Machine Translation Data Entry.  
    This is a program to create a database of Russian-English terms.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 23, 2016, San Diego California United States of America
"""

import os, sys, pwd
import psycopg2 as pg_driver
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_dataentry import Ui_DataEntry
from machinetrans.data.wordtype import WordType
from machinetrans.dataentry.verbconjugation import VerbConjugation
from machinetrans.dataentry.sqlcheck import SQLCheck
from machinetrans.dataentry.sqltest import SQLTest
from machinetrans.dataentry.errordisplay import ErrorDisplay
from machinetrans.dataentry.sqldata import SQLData
from machinetrans.dataentry.declentry import DeclEntry
from machinetrans.data.wordmorph import WordMorph
from machinetrans.dataentry.adjdeclentry import AdjDeclEntry
from machinetrans.dataentry.partdecl import PartDecl
from machinetrans.dataentry.pastconj import PastConj
from machinetrans.dataentry.miscconj import MiscConj
from machinetrans.dataentry.pronoundecl import PronounDecl
from machinetrans.dataentry.shortadj import ShortAdj
from machinetrans.dataentry.invarlist import InvarList
from machinetrans.helpview import HelpView
class DataEntry(QDialog, Ui_DataEntry):
    """ A GUI to enter Russian-English language data into
        an PostgreSQL database.
    """
    # All the help files are in /usr/share/machinetrans/resources
    helpfile = "/usr/share/machinetrans/resources/dataentry.html"
    completed = True
    rustr = ""
    enstr = ""
    enpresadv = ""
    enpastadv = ""
    variety = ""
    imperfective = False
    verbpages = list([False, False, False, False])
    adjpages = list([False, False])
    rugen = ""
    wclass = ""
    tense = ""
    presstem = ""
    paststem = ""
    sqlcommand = ""
    adjcommand = ""
    shortadjcommand = ""
    shortppp = False
    shortadj = True
    quote = "\'"
    noexit = True
    sqldict = dict()
    verbdict = dict()
    finalkey = ""
    # Contains all the classifications for the 
    # different types of words and their subcategories.
    types = WordType()
    # Contains all the Russian declensions
    # and verb conjugations.
    morphs = None
    tagtext = ""
    verbconj = None
    declension = list()
    labeltext = ""
    errormessage = ""
    conn = None
    db = None
    noexit = True
    cancel = False
    contpage = True
    # Window geometry information that is saved from usage to usage.
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()
    pppend = ""
    pppstem = ""
    enppp = ""
    usrdir = ""
    # The configuration directory.
    confdir = ".config"
    progdir = ""
    # The configuration file.
    progconf = "machinetrans.conf"
    # The GUI label
    labeldata = "Data Entry for "
    thirdpersonplural = ""
    firstpersonplural = ""
    firstpersonsingular = ""
    back = False
    guicount = 0
    oneself = False
    sqllist = list()
    sqldata = None
    adjdict = dict()
    enpasttense = ""
    animate = False
    pastactive = False
    
    def __init__(self, parent=None):
        """ Initialize a Qt Dialog and open
            a connection to PostgreSQL.
        """
        super(DataEntry, self).__init__(parent)
        self.setupUi(self)
        try: 
            # Connect to the database.
            self.conn = pg_driver.connect(user = 'machinetrans', dbname = 'machinetrans', password = 'MachineTrans', host = 'localhost', 
            port = 5432)
            self.db = self.conn.cursor()
        except Exception as e:
            print("\n\tUnable to connect to the database \"machinetrans.\"\n")
            sys.exit(-1)
        # Get the user's home directory.
        self.usrdir = os.environ["HOME"]
        # Create the path to the configuration directory.
        self.confdir = os.path.join(self.usrdir, self.confdir)
        # Check for the existance of a configuration directory.
        if not os.path.exists(self.confdir):
            try:
                os.mkdir(self.confdir)
            except Exception as e:
                QMessageBox.critical(self, "Fatal Error", "Could not create the directory " \
                    + self.confdir + "\n" +  str(e), QMessageBox.Ok, QMessageBox.NoButton)
                sys.exit(1)
        else:
            # Make a path to the program's configuration directory.
            self.progdir = os.path.join(self.confdir, "machinetrans")
            # if the program's configuration directory does not exist, create it.
            if not os.path.exists(self.progdir):
                try:
                    os.mkdir(self.progdir)
                except Exception as e:
                    QMessageBox.critical(self, "Fatal Error", "Could not create the directory " \
                        + self.progdir + "\n" +  str(e), QMessageBox.Ok, QMessageBox.NoButton)
                    sys.exit(1)
            else:
                # The directory exists, so load the window geometry.
                fname = os.path.join(self.progdir, self.progconf)
                if os.path.exists(fname):
                    try:
                        textfile = open(fname, newline='\n', encoding='utf-8')
                        geomlist = textfile.readlines()
                        textfile.close()
                    except Exception as e:
                        QMessageBox.warning(self, "Program Error", "Could not read the configuration file:  " \
                            + fname + " Error:  " +  str(e), QMessageBox.Ok, QMessageBox.NoButton)
                    if (len(geomlist) >= 4):
                        try:
                            tmpstr = geomlist[0].rstrip('\n')
                            self.winx = float(tmpstr)
                        except Exception as e:
                            print("Error converting geometry:  " + str(e))
                        try:
                            tmpstr = geomlist[1].rstrip('\n')
                            self.winy = float(tmpstr)
                        except Exception as e:
                            print("Error converting geometry:  " + str(e))
                        try:
                            tmpstr = geomlist[2].rstrip('\n')
                            self.width1 = float(tmpstr)
                        except Exception as e:
                            print("Error converting geometry:  " + str(e))
                        try:
                            tmpstr = geomlist[3].rstrip('\n')
                            self.height1 = float(tmpstr)
                        except Exception as e:
                            print("Error converting geometry:  " + str(e))
        # Check to see if all the variables have valid data, and if so, resize the GUI.
        if (self.winx >= 0 and self.winy >= 0 and self.width1 > 0 and self.height1 > 0):
            self.setGeometry(self.winx, self.winy, self.width1, self.height1)
        # Set the current working directory to the user's home directory.
        self.currdir = self.usrdir
        self.labeltext = self.labeldata
        # Here I create a list of my set and sort it.
        # This creates a stable appearance in the GUI,
        # otherwise it would appear differently each time,
        # because a set is a hash.
        for x in sorted(self.types.wordclass):
            if x == "participle":
                x = "participle *"
            elif x == "past tense verb":
                x = "past tense verb *"
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)
        self.quitBttn.clicked.connect(self.close)
        self.listDisplay.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listDisplay.itemClicked.connect(self.itemSelect)
        self.sqlBttn.clicked.connect(self.checksql)
        self.acceptBttn.clicked.connect(self.nextlist)
        self.cancelBttn.clicked.connect(self.wordclasses)
        self.dataBttn.clicked.connect(self.displaydata)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.morphs = WordMorph()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record GUI sizing information.
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
        self.titleLbl.setGeometry(10, 10, tmpwidth, 40)
        tmpx = 100 * wscale
        tmpy = 120 * hscale
        tmpwidth = 600 * wscale
        tmpheight = 300 * hscale
        self.listDisplay.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpint = self.width1 / 5
        tmpx = (self.width1 - ((tmpint * 4) + 130)) / 2
        self.quitBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.dataBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.cancelBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.sqlBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
        
        
    def wordclasses(self):
        """ Create the list for the main word classification: Nouns, verbs, etc.
        """
        self.setVisible(True)
        self.activateWindow()
        self.cancel = False
        self.wclass = ""
        self.sqlcommand = ""
        self.sqldict = dict()
        self.labeltext = self.labeldata
        self.titleLbl.setText(self.labeltext)
        self.listDisplay.clear()
        for x in sorted(self.types.wordclass):
            if x == "participle":
                x = "participle *"
            elif x == "past tense verb":
                x = "past tense verb *"
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)
        self.listDisplay.itemClicked.disconnect()
        self.listDisplay.itemClicked.connect(self.itemSelect)
        self.acceptBttn.clicked.disconnect()
        self.acceptBttn.clicked.connect(self.nextlist)
        
    def itemSelect(self):
        """ Select an item from the word class list.
        """
        tagval = None
        self.tagtext = ''
        tagval = self.listDisplay.selectedItems()
        self.tagtext = tagval[0].text()
        self.wclass = self.tagtext
        if self.wclass == "past tense verb *":
            self.wclass = "pastverb"
        elif self.wclass == "participle *":
            self.wclass = "participle"
    
    def closeEvent(self, event):
        """ Close the GUI and prompt for data consolidation (removal of duplicates.)
            In database consolidation a temporary table of unique entries is created, 
            the original table is deleted, and the temporary table is then renamed as
            the original. 
            The window geometry information is written to the configuration file.
        """
        self.noexit = False
        self.sqlcommand = ""
        for x in sorted(self.types.wordclass):
            if x == "past tense verb":
                x = "pastverb"
            tmpstr = x + "s"
            self.tense = ("CREATE TABLE tmpTable AS SELECT DISTINCT * FROM {0};\n" + 
                "DROP TABLE {0};\nALTER TABLE tmpTable RENAME TO {0};\n")
            self.tense = self.tense.format(tmpstr)
            self.sqlcommand += self.tense
        self.finalize()
        # Set the file name for the configuration file.
        fname = os.path.join(self.progdir, self.progconf)
        try:
            textfile = open(fname, "w", newline="\n", encoding="utf-8")
            for x in self.geometry:
                textfile.write(str(x) + "\n")
            textfile.close()
        except Exception as e:
            print("\n\nUnable to save program window geometry.\n\n")
        event.accept()
        
         
    def displaydata(self):
        """ Display and edit the data in the current postgresql table selected.
        """
        if self.wclass == "":
            QMessageBox.warning(self, "No Word Class Selected!",\
                "You need to select a word class before looking at its data.", \
                QMessageBox.Ok, QMessageBox.NoButton)
        elif self.wclass == "participle *":
            self.wclass = "participle"
        elif self.wclass == "past tense verb *":
            self.wclass = "pastverb"
        else:
            self.setVisible(False)
            # This GUI allows editing and deletion of database table rows.
            datagui = SQLData(self)
            datagui.activateWindow()
            datagui.exec()
            self.setVisible(True)
            self.activateWindow()
            self.acceptBttn.setFocus()
        
    def nextlist(self):
        """ Direct the program into the selected word type and 
            initialize the SQL command.
        """
        if self.wclass == "":
            QMessageBox.critical(self, "Error on Word Type",\
                "No word type selected.",\
                QMessageBox.Ok, QMessageBox.NoButton)
            return
        self.sqlcommand = "INSERT INTO " + self.wclass + "s "
        if self.wclass == "noun":
            self.noun()
        elif self.wclass == "adjective":
            self.adjective()
        elif self.wclass == "pronoun":
            self.pronoun()
        elif self.wclass == "verb":
            self.verb()
        elif self.wclass == "interrogative":
            self.interrogative()
        elif self.wclass == "interjection":
            self.interjection()
        elif self.wclass == "invariant":
            self.invariant()
        elif self.wclass == "adverb":
            self.adverb()
        elif self.wclass == "preposition":
            self.preposition()
        elif self.wclass == "conjunction":
            self.conjunction()
        elif self.wclass == "symbol":
            self.symbol()
        elif self.wclass == "participle":
            QMessageBox.warning(self, "Data Check Only", "The \"participle\" entry " \
                "is for data checking only.  To enter a participle use \"verb\".")
        elif self.wclass == "pastverb":
            QMessageBox.warning(self, "Data Check Only", "The \"past tense verbs\" entry " \
                "is for data checking only.  To enter a past tense verb use \"verb\".")
        else:
            QMessageBox.critical(self, "Error on Word Type",\
                "The current word type: " + self.wclass + " is unaccounted for.",\
                QMessageBox.Ok, QMessageBox.NoButton)
        return
        
    def noun(self):
        """ Enter a noun and go to the noun variety.
        """
        self.enstr = ""
        self.completed = True
        while len(self.enstr) == 0 and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Noun.", "Noun Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = ""
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = self.enstr
        else:
            self.wordclasses()
            return
        self.rustr = ""
        self.completed = True
        while len(self.rustr) == 0 and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Noun.", "Russian Noun:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = ""
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = self.rustr
            self.listDisplay.clear()
            for x in sorted(self.types.nouns):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.nounanim)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.nounanim)
        else:
            self.wordclasses()

    def nounanim(self):
        """ Create the correct SQL dictionary entry and direct the program to endsql.
        """
        self.tagtext = ''
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict["variety"] = self.tagtext
            self.listDisplay.clear()
            for x in sorted(self.types.animate):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.nounvar)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.nounvar)
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")

        
    def nounvar(self):
        """ Create the correct SQL dictionary entry and direct the program to endsql.
        """
        self.tagtext = ''
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict["animate"] = self.tagtext
            self.listDisplay.clear()
            for x in sorted(self.types.nountype):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endsql)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endsql)
            self.finalkey = "type"
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")

    def endsql(self):
        """ Create the SQL dictionary entry, create the proper GUI
            for the given word type.  This method handles nouns and adjectives. 
        """
        self.sqldata = None
        self.adjdict.clear()
        self.tagtext = ''
        self.declension = list()
        self.contpage = True
        self.adjpages = list([False, False])
        self.shortadj = True
        self.adjcommand = ""
        self.shortadjcommand = ""
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict[self.finalkey] = self.tagtext
            if self.wclass == "noun":
                self.setVisible(False)
                decline = DeclEntry(self)
                decline.activateWindow()
                decline.exec()
                if self.cancel or len(self.declension) == 0:
                    self.setVisible(True)
                    self.activateWindow()
                    self.wordclasses()
                    return
                basecommand = self.sqlcommand
                self.sqlcommand = ""
                for x in self.declension:
                    cols = "("
                    data = "("
                    cols += "variety, "
                    data += "\'" + x[0] + "\', "
                    cols += "type, "
                    data += "\'" + x[1] + "\', "
                    cols += "runame, "
                    data += "\'" + x[2] + "\', "
                    cols += "name, "
                    data += "\'" + x[3] + "\', "
                    cols += "gender, "
                    data += "\'" + x[4] + "\', "
                    cols += "declension, "
                    data += "\'" + x[5] + "\', "
                    cols += "wordcase, "
                    data += "\'" + x[6] + "\', "
                    cols += "animate) VALUES"
                    data += "\'" + x[7] + "\');\n"
                    self.sqlcommand += basecommand + cols + data
            elif self.wclass == "adjective":
                basecommand = self.sqlcommand
                self.sqldict[self.finalkey] = "\'" + self.sqldict[self.finalkey] + "\'"
                if self.tagtext == "descriptive":
                    self.setVisible(False)
                    while self.contpage:
                        self.sqldict["variety"] = "\'descriptive\'"
                        decline = AdjDeclEntry(self)
                        decline.activateWindow()
                        decline.exec()
                        self.setVisible(True)
                        if self.cancel:
                            self.activateWindow()
                            self.wordclasses()
                            return
                        self.sqldict["variety"] = "\'short adjective\'"
                        adjgui = ShortAdj(self)
                        adjgui.activateWindow()
                        adjgui.exec()
                        self.setVisible(True)
                        if self.cancel:
                            self.activateWindow()
                            self.wordclasses()
                            return
                    self.sqlcommand = self.adjcommand
                    if self.shortadj:
                       self.sqlcommand += self.shortadjcommand
                    self.activateWindow()
                elif self.tagtext == "comparative":
                    engcomp = ""
                    self.completed = True
                    while len(engcomp) == 0 and self.completed:
                        engcomp, self.completed = QInputDialog.getText(self, "English Comparative", "Comparative Adjective Value:")
                        if engcomp and not engcomp[0] in self.morphs.enall:
                            QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                            engcomp = ""
                        if self.completed:
                            self.sqldict["name"] = "\'" + engcomp + "\'"
                        else:
                            self.wordclasses()
                            return
                    rucomp = ""
                    self.completed = True
                    while len(rucomp) == 0 and self.completed:
                        rucomp, self.completed = QInputDialog.getText(self, "Russian Comparative", "Russian Comparative Adjective:")
                        if rucomp and not rucomp[0] in self.morphs.ruall:
                            QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                            rucomp = ""
                        if self.completed:
                            self.sqldict["declension"] = "\'" + rucomp + "\'"
                        else:
                            self.wordclasses()
                            return
                    self.sqldict["runame"] = "\'" + self.rustr + "\'"
                    self.sqldict["gender"] = "\'masculine\'"
                    self.sqldict["wordcase"] = "\'nominative\'"
                    self.sqldict["animate"] = "\'inanimate\'"
                    self.sqldict["variety"] = "\'comparative\'"
                    cols = "("
                    data = "("
                    for y in self.sqldict:
                        cols += y + ", "
                        data += self.sqldict[y] + ", "
                    cols = cols[:-2] + ") VALUES"
                    data = data[:-2] + ");\n"
                    self.sqlcommand = basecommand + cols + data
                elif self.tagtext == "superlative":
                    self.setVisible(False)
                    self.sqldict["variety"] = "\'superlative\'"
                    decline = AdjDeclEntry(self)
                    decline.activateWindow()
                    decline.exec()
                    self.setVisible(True)
                    self.activateWindow()
                    if self.cancel:
                        self.wordclasses()
                        return
                    self.sqlcommand = self.adjcommand
            self.noexit = True
            self.finalize()
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")
        
        
    def verb(self):
        """ Enter a verb and go to the verb variety.
        """
        self.verbpages = list([False, False, False, False])
        self.sqldict.clear()
        self.verbdict.clear()
        self.enstr = None
        self.pppend = ""
        self.pppstem = ""
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Verb.", "Verb Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.enstr + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Verb.", "Russian Verb:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.verbs):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.verbvar)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.verbvar)
        else:
            self.wordclasses()
            
    def verbvar(self):
        """ Create the correct SQL dictionary item, 
            and go to the "verbact" method.
        """
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict["variety"] = "\'" + self.tagtext + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.imperfective):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.verbact)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.verbact)
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")
        
    def verbact(self):
        """ Display a series of GUI "pages" for the entry of a complete Russian
            verb-participle conjugation-declension, which can contain up to 105 entries.
            Because I wanted the verb pages to be browsable backwards and forwards
            they use a separate dictionary called "verbdict" and not the regular
            "sqldict" that most of the other pages use.  However, they draw their
            basic data from "sqldict."
        """
        self.cancel = False
        self.noexit = True
        self.back = False
        self.guicount = 0
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if not tagval:
            QMessageBox.warning(self, "No Item Selected", "This menu requires a selected item.")
            return
        self.tagtext = tagval[0].text()
        self.sqldict["imperfective"] = "\'" + self.tagtext + "\'"
        self.imperfective = self.tagtext == "imperfective"
        self.listDisplay.clear()
        self.setVisible(False)
        while self.guicount < 4:
            if self.guicount == 0:
                # Basic verb conjugation.
                verbconj = VerbConjugation(self)
                verbconj.activateWindow()
                verbconj.exec()
            elif self.guicount == 1:
                # Participle declension, up to four varietys.
                verbpart = PartDecl(self)
                verbpart.activateWindow()
                verbpart.exec()
            elif self.guicount == 2:
                # Past tense conjugation.
                verbpast = PastConj(self)
                verbpast.activateWindow()
                verbpast.exec()
            elif self.guicount == 3:
                # Verbal-adverbs and imperatives.
                verbmisc = MiscConj(self)
                verbmisc.activateWindow()
                verbmisc.exec()
            if self.cancel:
                # Action cancelled.
                self.setVisible(True)
                self.activateWindow()
                self.wordclasses()
                return
            if self.back:
                # Go back one page and re-enter.
                self.guicount -= 1
                self.back = False
            else:
                self.guicount += 1
        # Creating SQL for the basic verb.
        self.sqlcommand = ""
        basecommand = "INSERT INTO verbs "
        for x in self.types.person:
            cols = "("
            data = "("
            for y in sorted(self.verbdict["page1"][x]):
                cols += y + ", "
                data += self.verbdict["page1"][x][y] + ", "
            cols = cols[:-2] + ") VALUES"
            data = data[:-2] + ");\n"
            self.sqlcommand += basecommand + cols + data
        # Moving on to participles.
        basecommand = "INSERT INTO participles "
        parttypes = sorted(self.verbdict["page2"].keys())
        for x in parttypes:
            present = False
            for z in self.types.gender:
                if z in x:
                    present = True
                if present:
                    cols = "("
                    data = "("
                    datatypes = sorted(self.verbdict["page2"][x].keys())
                    for y in datatypes:
                        cols += y + ", "
                        data += self.verbdict["page2"][x][y] + ", "
                    cols = cols[:-2] + ") VALUES"
                    data = data[:-2] + ");\n"
                    self.sqlcommand += basecommand + cols + data
                    break
        basecommand = "INSERT INTO pastverbs "
        parttypes = sorted(self.verbdict["page3"].keys())
        for x in parttypes:
            present = False
            for z in self.types.gender:
                if z in x:
                    cols = "("
                    data = "("
                    for y in sorted(self.verbdict["page3"][x]):
                        cols += y + ", "
                        data += self.verbdict["page3"][x][y] + ", "
                    cols = cols[:-2] + ") VALUES"
                    data = data[:-2] + ");\n"
                    self.sqlcommand += basecommand + cols + data
        basecommand = "INSERT INTO participles "
        parttypes = sorted(self.verbdict["page4"].keys())
        for x in parttypes:
            if x != "pppstem" and not isinstance(self.verbdict["page4"][x], bool):
                cols = "("
                data = "("
                for y in sorted(self.verbdict["page4"][x]):
                    cols += y + ", "
                    data += self.verbdict["page4"][x][y] + ", "
                cols = cols[:-2] + ") VALUES"
                data = data[:-2] + ");\n"
                self.sqlcommand += basecommand + cols + data
        self.finalize()
        self.setVisible(True)
        self.wordclasses()
        

    def adjective(self):
        """ Enter an adjective and go to endsql.
        """
        self.enstr = ""
        self.completed = True
        while len(self.enstr) ==  0 and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Adjective.", "Adjective Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = ""
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.enstr + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = ""
        self.completed = True
        while len(self.rustr) == 0 and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Adjective.", "Russian Adjective:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = ""
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.adjectives):
                if x == "short adjective":
                    continue
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endsql)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endsql)
            self.finalkey = "variety"
        else:
            self.wordclasses()

    def pronoun(self):
        """ Display the pronoun GUI. The pronoun GUI allows for 
            automatic entry of the pronouns, which reside in the 
            WordMorph class, or alternatively individual items 
            or pronoun groups can be entered or edited.
        """
        self.setVisible(False)
        prongui = PronounDecl(self)
        prongui.activateWindow()
        prongui.exec()
        if self.cancel:
            self.wordclasses()
        else:
            self.finalize()

    def interrogative(self):
        """ Enter an interrogative and go to the interrogative variety.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Interrogative.", "Interrogative:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Interrogative.", "Russian Interrogative:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.interrogs):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.interrogvar)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.interrogvar)
        else:
            self.wordclasses()

    def interrogvar(self):
        """ Get the variety, update the SQL dictionary and 
            enter it into the database.
        """
        tagval = None
        self.tagtext = ''
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict["variety"] = "\'" + self.tagtext + "\'"
            cols = "("
            data = "("
            for y in self.sqldict:
                cols += y + ", "
                data += self.sqldict[y] + ", "
            cols = cols[:-2] + ") VALUES"
            data = data[:-2] + ");\n"
            self.sqlcommand = self.sqlcommand + cols + data
            self.finalize()
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")
            

    def interjection(self):
        """ Enter an interjection and then insert it into
            the database.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Interjection.", "Interjection Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Interjection.", "Russian Interjection:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            cols = "("
            data = "("
            for y in self.sqldict:
                cols += y + ", "
                data += self.sqldict[y] + ", "
            cols = cols[:-2] + ") VALUES"
            data = data[:-2] + ");\n"
            self.sqlcommand = self.sqlcommand + cols + data
            self.finalize()
        else:
            self.wordclasses()
        
    def invariant(self):
        """ Enter an invariant item (no declension).
            Display the invariant GUI, which allows
            for entering multiple invariant values,
            and the editing and deleting of existing values.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Invariant.", "Invariant Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Invariant.", "Russian Invariant:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
        else:
            self.wordclasses()
            return
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        self.variety = None
        self.completed = False
        entries = list(self.types.invariant)
        entries.sort()
        while not self.variety and not self.completed:
            self.variety, self.completed = QInputDialog.getItem(self, "Type", "Invariant Type", entries)
        if self.completed:
            self.sqldict["variety"] = "\'" + self.variety + "\'"
        else:
            self.wordclasses()
            return
        invardecl = QInputDialog.getItem(self, "Object Declension", "Select the declension of the noun that follows this word.", 
            self.types.declension)
        if invardecl[1]:
            self.sqldict["wordcase"] = "\'" + invardecl[0] + "\'"
            self.setVisible(False)
            invargui = InvarList(self)
            invargui.activateWindow()
            invargui.exec()
            self.wordclasses()
        else:
            self.wordclasses()

    def adverb(self):
        """ Enter an adverb and go to "endnocase."
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Adverb.", "Adverb Value:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Adverb.", "Russian Adverb:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.adverbs):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endnocase)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endnocase)
            self.finalkey = "variety"
        else:
            self.wordclasses()

    def endnocase(self):
        """ Finalize the SQL command and commit the data.
            This is the reflection of endsql but with no
            declension information.
        """
        self.noexit = True
        self.tagtext = ''
        tagval = None
        tagval = self.listDisplay.selectedItems()
        if tagval:
            self.tagtext = tagval[0].text()
            self.sqldict[self.finalkey] = "\'" + self.tagtext + "\'"
            cols = "("
            data = "("
            for x in self.sqldict:
                cols += x + ", "
                data += self.sqldict[x] + ", "
            cols = cols[:-2]
            data = data[: -2]
            cols += ") VALUES"
            data += ");"
            self.sqlcommand += cols + data
            self.finalize()
        else:
            QMessageBox.warning(self, "No Item Selected", "You must select an item from the list or cancel.")
        
    def preposition(self):
        """ Enter a preposition and go to endnocase.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Preposition.", "Preposition:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Preposition.", "Russian Preposition:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
        else:
            self.wordclasses()
            return
        self.completed = True
        self.objcase = None
        while not self.objcase and self.completed:
            self.objcase, self.completed = QInputDialog.getItem(self, "Case.", "Case:", self.types.objcase)
        if self.completed:
            self.sqldict["objcase"] = "\'" + self.objcase  + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.prepositions):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endnocase)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endnocase)
            self.finalkey = "variety"
        else:
            self.wordclasses()
        
    def conjunction(self):
        """ Enter an conjunction and go to endnocase.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Conjunction.", "Conjunction:")
            if self.enstr and not self.enstr[0] in self.morphs.enall:
                QMessageBox.warning(self, "Non-English Character", "A non-english character was entered for an english word.")
                self.enstr = None
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Conjunction.", "Russian Conjunction:")
            if self.rustr and not self.rustr[0] in self.morphs.ruall:
                QMessageBox.warning(self, "Non-Cyrillic Character", "A non-cyrillic character was entered for an russian word.")
                self.rustr = None
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.conjunctions):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endnocase)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endnocase)
            self.finalkey = "variety"
        else:
            self.wordclasses()
                
    def symbol(self):
        """ Enter an symbol and go to endnocase.
        """
        self.enstr = None
        self.completed = True
        while not self.enstr and self.completed:
            self.enstr, self.completed = QInputDialog.getText(self, "Symbol.", "Symbol:")
        self.labeltext += self.enstr + " "
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["name"] = "\'" + self.apostrophe(self.enstr) + "\'"
        else:
            self.wordclasses()
            return
        self.rustr = None
        self.completed = True
        while not self.rustr and self.completed:
            self.rustr, self.completed = QInputDialog.getText(self, "Symbol.", "Russian Symbol:")
        self.labeltext += self.rustr
        self.titleLbl.setText(self.labeltext)
        if self.completed:
            self.sqldict["runame"] = "\'" + self.rustr + "\'"
            self.listDisplay.clear()
            for x in sorted(self.types.symbols):
                item = QListWidgetItem(x)
                self.listDisplay.addItem(item)
            self.listDisplay.itemClicked.disconnect()
            self.listDisplay.itemClicked.connect(self.endnocase)
            self.acceptBttn.clicked.disconnect()
            self.acceptBttn.clicked.connect(self.endnocase)
            self.finalkey = "variety"
        else:
            self.wordclasses()

    def displayhelp(self):
        """ Display an HTML help file located in /usr/share/machinetrans/resources
            in its own gui.  This is dependent on the variable "helpfile."
        """
        self.setVisible(False)
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.setVisible(True)
        self.activateWindow()
            
    def finalize(self):
        """ Show the user the SQL command in a gui and prompt for commit.
        """
        self.setVisible(False)
        sql = SQLCheck(self)
        sql.activateWindow()
        sql.exec()
        if not self.cancel:
            self.commitdata()
        if self.noexit:
            self.setVisible(True)
            self.activateWindow()
            self.wordclasses()
        
    def commitdata(self):
        """ Commit the SQL command.
        """
        try:
            self.db.execute(self.sqlcommand)
            self.conn.commit()
        except Exception as e:
            self.setVisible(False)
            self.errormessage = "Error Data Commit\n" + "Error committing the data for: " + \
                self.enstr + " " + self.rustr + "\nError:  " + str(e) + "\nCommand: " + self.sqlcommand
            errorgui = ErrorDisplay(self)
            errorgui.activateWindow()
            errorgui.exec()
            self.setVisible(True)
            self.activateWindow()

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
            
    def checksql(self):
        """ Check the current state of the given SQL command.
            This can be done at any time from the main GUI.
        """
        self.setVisible(False)
        sql = SQLTest(self)
        sql.activateWindow()
        sql.exec()
        self.setVisible(True)
        self.activateWindow()
        
def main():  # Remember the Maine.
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        font = app.font()
        font.setPointSize(16)
        app.setFont(font)
        entry = DataEntry()
        entry.show()
        app.exec()
    elif sys.argv[1] == 'dummy':
        return 0
    else:
        print("\n\n\tUsage:  dataentry.py\n\n")
        return 1
    return 0

main()        
