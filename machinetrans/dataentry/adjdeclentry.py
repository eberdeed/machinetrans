#!/usr/bin/python3
'''
    AdjDeclEntry:  Machine Translation Data Entry -- Russian Adjectival Declension Entry.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 1, 2016, San Diego California United States of America
'''
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from machinetrans.userinterfaces.ui_adjdeclentry import Ui_AdjDeclEntry
from machinetrans.data.wordmorph import WordMorph
from machinetrans.dataentry.decltable import DeclTable
from machinetrans.helpview import HelpView
from machinetrans.dataentry.adjdeclsel import AdjDeclSel

class AdjDeclEntry(QDialog, Ui_AdjDeclEntry):
    ''' A GUI to enter Russian adjectival declensions and their English equivalents.
    '''
    # The current helpfile for adjectives.
    helpfile = '/usr/share/machinetrans/resources/adjdeclentry.html'
    parent = None
    labeltext = ''
    # Window geometry.
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()
    # Russian word morphology (declension and conjugations).
    morphs = None
    # Data for the declension ending table.
    tableobj = list()
    # Data for the selected declension.
    decllist = list()
    # Data for the final published declensions.
    sqldata = list()
    # The Russian stem.
    stem = ''
    # The type of adjective.
    adjtype = 0
    # The Russian word.
    rustr = ''
    # The English word.
    enstr = ''
    # The declined Russian word from the gui.
    cases = list()
    # The declension number.
    declnum = 0
    
    def __init__(self, parent=None):
        ''' Configure the GUI and decide where the given adjective fits in the overall scheme.
        '''
        super(AdjDeclEntry, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.parent.cancel = True
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.stem = self.rustr[:-2]
        self.stemEdit.setText(self.stem)
        ending = self.rustr[-2:]
        cons = self.rustr[-3]
        # Set up the endings.
        self.stemEdit.firereturn.triggered.connect(self.stemchg)
        self.stemEdit.firefocus.triggered.connect(self.stemchg)
        
        # Determine the adjectival ending.
        if ending == 'ый':
            self.adjtype = 0
        elif ending == 'ий' and cons in self.morphs.gkx:
            self.adjtype = 1
        elif ending == 'ий':
            self.adjtype = 2
        elif ending == 'ой':
            self.adjtype = 3
        elif ending == 'ье':
            self.adjtype = 4
        else:
            QMessageBox.warning(self, 'Error on Ending', 'You will be provided with the hard endings.')
            self.adjtype = 0
        # Set the declension to masculine animate.
        self.anim.setChecked(True)
        
        # Draw the table for masculine animate.
        if self.parent.adjpages[0]:
            self.sqldata.clear()
            self.sqldata = self.parent.sqldata.copy()
        else:
            self.createdecl()
        self.drawtable()
        self.declension1()
        # Connect the signals to their various methods.
        self.acceptBttn.clicked.connect(self.accept)
        self.rejectBttn.clicked.connect(self.cancel)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.nomEdit.firereturn.triggered.connect(self.addnom)
        self.nomEdit.firefocus.triggered.connect(self.addnom)
        self.accEdit.firereturn.triggered.connect(self.addacc)
        self.accEdit.firefocus.triggered.connect(self.addacc)
        self.genEdit.firereturn.triggered.connect(self.addgen)
        self.genEdit.firefocus.triggered.connect(self.addgen)
        self.datEdit.firereturn.triggered.connect(self.adddat)
        self.datEdit.firefocus.triggered.connect(self.adddat)
        self.insEdit.firereturn.triggered.connect(self.addins)
        self.insEdit.firefocus.triggered.connect(self.addins)
        self.prpEdit.firereturn.triggered.connect(self.addprp)
        self.prpEdit.firefocus.triggered.connect(self.addprp)
        self.anim.released.connect(self.declension1)
        self.inan.released.connect(self.declension2)
        self.nuet.released.connect(self.declension4)
        self.fem.released.connect(self.declension3)
        self.pluranim.released.connect(self.declension5)
        self.plurinan.released.connect(self.declension6)
        self.declBttn.clicked.connect(self.changedecl)
        self.stemEdit.firereturn.triggered.connect(self.stemchg)
        self.engEdit.setText(self.enstr)
        
    def getdecl(self):
        """ Gather the declension from the gui for the given
            declension number.
        """
        self.cases = list()
        tmptxt = self.nomEdit.text()
        if len(tmptxt) > 0:
            self.cases.append(self.nomEdit.text())
            self.cases.append(self.accEdit.text())
            self.cases.append(self.genEdit.text())
            self.cases.append(self.datEdit.text())
            self.cases.append(self.insEdit.text())
            self.cases.append(self.prpEdit.text())
            self.sqldata[self.declnum] = self.cases
            
        
            
    def createdecl(self):
        count1 = 0
        self.sqldata = None
        self.sqldata = list()
        for x in range(6):
            self.sqldata.append(list())
        for x in self.morphs.declension[self.adjtype]:
            for y in range(1, len(x)):
                self.sqldata[count1].append(self.stem + x[y])
            count1 += 1
                
                    
    def hardtitle(self):
        ''' Display a title for hard adjectival endings.
        '''
        tmpstr = self.rustr.capitalize() + ' Russian Adjectival Declension -- Hard Ending'
        self.titleLbl.setText(tmpstr)

    def softtitle(self):
        ''' Display a title for soft adjectival endings.
        '''
        tmpstr = self.rustr.capitalize() + ' Russian Adjectival Declension -- Soft Ending'
        self.titleLbl.setText(tmpstr)
                
    def gkxsofttitle(self):
        ''' Display a title for soft adjectival endings.
        '''
        tmpstr = self.rustr.capitalize() + ' Russian Adjectival Declension -- ГКХ with a Soft Ending'
        self.titleLbl.setText(tmpstr)

    def oytitle(self):
        ''' Display a title for other adjectival endings.
        '''
        tmpstr = self.rustr.capitalize() + ' Russian Adjectival Declension -- Ending in ой'
        self.titleLbl.setText(tmpstr)

    def myagkiytitle(self):
        ''' Display a title for other adjectival endings.
        '''
        tmpstr = self.rustr.capitalize() + ' Russian Adjectival Declension -- Ending in ье'
        self.titleLbl.setText(tmpstr)

    def changedecl(self):
        changer = AdjDeclSel(self)
        changer.exec()
        self.drawselection()
        

    def resizeEvent(self, event):
        ''' Resize the GUI.
        '''
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        hscale = self.height1 /600
        wscale = self.width1 / 800
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 30, tmpwidth, 30)
        tmpheight = hscale * 180
        self.tableView.setGeometry(10, 70, tmpwidth, tmpheight)
        tmpy = hscale * 260
        tmpx = (self.width1 / 2) - 385
        self.gender.setGeometry(tmpx, tmpy, 770, 50)
        tmpx = 20
        tmpy = 0
        self.anim.setGeometry(tmpx, tmpy, 120, 25)
        tmpx = 230
        self.inan.setGeometry(tmpx, tmpy, 140, 25)
        tmpx = 450
        self.fem.setGeometry(tmpx, tmpy, 130, 25)
        tmpx = 640
        self.nuet.setGeometry(tmpx, tmpy, 120, 25)
        tmpy = 30
        tmpx = 170
        self.pluranim.setGeometry(tmpx, tmpy, 190, 25)
        tmpx = 430
        tmpy = 30
        self.plurinan.setGeometry(tmpx, tmpy, 210, 25)
        tmpy = 320 * hscale
        tmpx = (self.width1 - 740) / 2
        self.engLbl.setGeometry(tmpx, tmpy, 80, 25)
        tmpx += 90
        self.engEdit.setGeometry(tmpx, tmpy, 240, 30)
        tmpx = (self.width1 / 2) + 20
        self.stemLbl.setGeometry(tmpx, tmpy, 70, 25)
        tmpx += 90
        self.stemEdit.setGeometry(tmpx, tmpy, 260, 30)
        tmpy = 350 * hscale
        tmpx = (self.width1 - 740) / 2
        self.nomLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.nomEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 350 * hscale
        tmpx = (self.width1 / 2) + 30        
        self.accLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.accEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 410 * hscale
        tmpx = (self.width1 - 740) / 2
        self.genLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.genEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 410 * hscale
        tmpx = (self.width1 / 2) + 30        
        self.datLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.datEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 470 * hscale
        tmpx = (self.width1 - 740) / 2
        self.insLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.insEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = 470 * hscale
        tmpx = (self.width1 / 2) + 30        
        self.prpLbl.setGeometry(tmpx, tmpy, 340, 25)
        tmpy += 30
        self.prpEdit.setGeometry(tmpx, tmpy, 340, 30)
        tmpy = self.height1 - 80
        tmpx = (self.width1 - 740) / 2
        self.rejectBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) - 75
        self.declBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx = (self.width1 / 2) + 220
        self.acceptBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def drawtable(self):
        ''' Draw an HTML table representing the given adjectival declension.
            Each table will have masculine, feminine and nueter.
        '''
        self.rustr = self.parent.rustr
        self.tableobj = list()
        tmpstr = self.rustr[-2:]
        if self.adjtype == 0:
            self.hardtitle()
            for x in self.morphs.adjectiveshard:
                self.tableobj.append(x)
        elif self.adjtype == 1:
            self.gkxsofttitle()
            self.tableobj = list()
            for x in self.morphs.adjectivesgkxsoft:
                self.tableobj.append(x)
        elif self.adjtype == 2:
            self.softtitle()
            self.tableobj = list()
            for x in self.morphs.adjectivessoft:
                self.tableobj.append(x)
        elif self.adjtype == 3:
            self.oytitle()
            self.tableobj = list()
            for x in self.morphs.adjectivesoy:
                self.tableobj.append(x)
        elif self.adjtype == 4:
            self.myagkiytitle()
            self.tableobj = list()
            for x in self.morphs.adjectivesmyagkiy:
                self.tableobj.append(x)
        self.createobj()
 
    def stemchg(self):
        ''' Propogates the stem change to the GUI.
        '''
        self.stem = self.stemEdit.text()
        self.createdecl()
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()
    
    def declension1(self):
        ''' Decline the adjective according to masculine animate rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 0
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()
        
    def declension2(self):
        ''' Decline the adjective according to masculine inanimate rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 1
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()
 
    def declension3(self):
        ''' Decline the adjective according to feminine rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 2
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()
 
    def declension4(self):
        ''' Decline the adjective according to nueter rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 3
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()
        
    def declension5(self):
        ''' Decline the adjective according to plural animate rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 4
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()

    def declension6(self):
        ''' Decline the adjective according to plural inanimate rules.
        '''
        self.getdecl()
        self.decllist = list()
        self.declnum = 5
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()

    def addnom(self):
        self.sqldata[self.declnum][0] = self.nomEdit.text()

    def addacc(self):
        self.sqldata[self.declnum][1] = self.accEdit.text()

    def addgen(self):
        self.sqldata[self.declnum][2] = self.genEdit.text()

    def adddat(self):
        self.sqldata[self.declnum][3] = self.datEdit.text()

    def addins(self):
        self.sqldata[self.declnum][4] = self.insEdit.text()

    def addprp(self):
        self.sqldata[self.declnum][5] = self.prpEdit.text()

    def drawselection(self):
        """ Open a declension selection page and get the "adjtype"
            value for the adjectival endings.
        """
        self.createdecl()
        self.drawtable()
        self.decllist = self.sqldata[self.declnum][:]
        self.drawdecl()

    def createobj(self):
        ''' Create an HTML table of adjectival declensions.
        '''
        self.tableView.clear()
        # A class to draw the HTML table.
        tmptable = DeclTable(self.rustr)
        for x in self.tableobj:
            tmptable.addrow(x)
        tmpstr = tmptable.table()
        # Put the table in the GUI.
        self.tableView.clear()
        self.tableView.setHtml(tmpstr)
        
    def drawdecl(self):
        ''' Fill the GUI with declensions.
        '''
        self.nomEdit.setText(self.decllist[0])
        self.accEdit.setText(self.decllist[1])
        self.genEdit.setText(self.decllist[2])
        self.datEdit.setText(self.decllist[3])
        self.insEdit.setText(self.decllist[4])
        self.prpEdit.setText(self.decllist[5])
        

    def accept(self):
        ''' Gather the data and create an SQL 
            command to insert the new data.
        '''
        self.getdecl()
        count1 = 0
        self.enstr = self.engEdit.text()
        basecommand = self.parent.sqlcommand
        self.parent.adjcommand = ""
        for x in self.sqldata:
            count2 = 0
            for y in x:
                cols = list()
                data = list()
                cols.append('name')
                x = self.enstr
                index = x.find('\'')
                while(index >= 0):
                    tmpstr1 = x[:index]
                    tmpstr1 += '\''
                    tmpstr1 += x[index:]
                    x = tmpstr1
                    tmpint = index + 2
                    index = x.find('\'', tmpint)
                data.append('\'' + x + '\'')
                cols.append('runame')
                data.append('\'' + self.sqldata[0][0] + '\'')
                cols.append('declension')
                data.append('\'' + y + '\'')
                cols.append('variety')
                data.append(self.parent.sqldict["variety"])
                if count1 == 0:
                    cols.append('gender')
                    data.append('\'masculine\'')
                    cols.append('animate')
                    data.append('\'animate\'')
                elif count1 == 1:
                    cols.append('gender')
                    data.append('\'masculine\'')
                    cols.append('animate')
                    data.append('\'inanimate\'')
                elif count1 == 2:
                    cols.append('gender')
                    data.append('\'feminine\'')
                    cols.append('animate')
                    data.append('\'animate\'')
                elif count1 == 3:
                    cols.append('gender')
                    data.append('\'nueter\'')
                    cols.append('animate')
                    data.append('\'inanimate\'')
                elif count1 == 4:
                    cols.append('gender')
                    data.append('\'plural\'')
                    cols.append('animate')
                    data.append('\'animate\'')
                elif count1 == 5:
                    cols.append('gender')
                    data.append('\'plural\'')
                    cols.append('animate')
                    data.append('\'inanimate\'')
                if count2 == 0:
                    cols.append('wordcase')
                    data.append('\'nominative\'')
                elif count2 == 1:
                    cols.append('wordcase')
                    data.append('\'accusative\'')
                elif count2 == 2:
                    cols.append('wordcase')
                    data.append('\'genitive\'')
                elif count2 == 3:
                    cols.append('wordcase')
                    data.append('\'dative\'')
                elif count2 == 4:
                    cols.append('wordcase')
                    data.append('\'instrumental\'')
                elif count2 == 5:
                    cols.append('wordcase')
                    data.append('\'prepositional\'')
                tokens = '('
                info = 'VALUES ('
                if (len(cols) != len(data)):
                    print("\n\nError:  Data types do not equal data present.\n\n")
                    limit = len(cols)
                    if limit > len(data):
                        limit = len(data)
                        coltest = True
                    elif limit < len(data):
                        coltest = False
                    if coltest:
                        final = len(cols)
                    else:
                        final = len(data)
                        for x in range(limit, final):
                            print(data[x], "\n")
                    exit(1)
                for y in range(len(cols)):
                    tokens += cols[y] + ', '
                    info += data[y] + ', '
                tokens = tokens[:-2]
                info = info[:-2]
                tokens += ')'
                info += ');\n'
                self.parent.adjcommand += basecommand + tokens + info
                count2 += 1
            count1 += 1
        self.parent.cancel = False
        self.parent.adjpages[0] = True
        self.parent.sqldata = self.sqldata.copy()
        self.close()
        
    def displayhelp(self):
        """ Display a help file in HTML format.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()
            
    def cancel(self):
        ''' Cancel this event.
        '''
        self.parent.cancel = True
        self.parent.declension = list()
        self.close()

    def closeEvent(self, event):
        ''' Close the GUI and pass along GUI sizing information.
        '''
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()  

        