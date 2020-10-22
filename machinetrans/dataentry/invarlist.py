#!/usr/bin/python3
"""
    InvarList:  Machine Translation Data Entry -- Russian Invariant List.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    October 25, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_invarlist import Ui_InvarList
from machinetrans.data.wordmorph import WordMorph
from machinetrans.data.wordtype import WordType
from machinetrans.dataentry.errordisplay import ErrorDisplay
from machinetrans.helpview import HelpView

class InvarList(QDialog, Ui_InvarList):
    """ Russian invariant word list.  
        Allows for editing and addition
        of Russian invariant words.
        Invariant means no declension or
        conjugation.  This class has no
        dictionary for SQL it works directly
        on the database.
    """

    helpfile = "/usr/share/machinetrans/resources/invarlist.html"
    parent = None
    sqlcommand = ""
    dblist = list()
    conn = None
    rustr = ''
    enstr = ''
    typstr = ''
    quote = "\'"
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    # Contains the data from the database.
    checkdict = dict()
    # Contains the data from the QListWidget.
    finaldict = dict()
    morphs = None
    types = None
    comma = ", "
    errormessage = ""
    findstr = ""
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the pronouns and their declensions.
        """
        super(InvarList, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.morphs = self.parent.morphs
        self.types = self.parent.types
        self.types = self.parent.types
        self.conn = self.parent.conn
        self.db = self.conn.cursor
        self.rustr = self.parent.rustr
        self.enstr = self.parent.enstr
        self.typestr = self.parent.sqldict["variety"]
        self.typestr = self.typestr.strip("\'")
        declstr = self.parent.sqldict["wordcase"]
        declstr = declstr.strip("\'")
        self.parent.sqlcommand = ""
        self.geometry = self.parent.geometry[:]
        self.parent.cancel = False
        self.itemList.setSelectionMode(QAbstractItemView.SingleSelection)
        for x in sorted(self.types.invariant):
            self.typeBox.addItem(x)
        self.itemList.itemClicked.connect(self.pdecl)
        self.findBttn.clicked.connect(self.finditem)
        self.deleteBttn.clicked.connect(self.delete)
        self.quitBttn.clicked.connect(self.cancel)
        self.newBttn.clicked.connect(self.clear)
        self.addBttn.clicked.connect(self.additem)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.enEdit.firereturn.triggered.connect(self.additem)
        self.ruEdit.firereturn.triggered.connect(self.additem)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        tmpstr = self.quote + self.apostrophe(self.enstr) + self.quote + ", " + self.quote + self.rustr + self.quote + ", " \
            + self.quote + declstr + self.quote + ", " + self.quote + self.typestr + self.quote
        self.sqlcommand = "INSERT INTO invariants (name, runame, wordcase, variety) VALUES(" + tmpstr + ");\n"
        self.db.execute(self.sqlcommand)
        self.conn.commit()
        entries = sorted(self.types.invariant)
        index = entries.index(self.typestr)
        self.typeBox.setCurrentIndex(index)
        self.declBox.addItems(self.types.declension)
        index = self.types.declension.index(declstr)
        self.declBox.setCurrentIndex(index)
        self.createlist()
        self.showdata()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record sizing information.
        """
        newitem = list()
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        hscale = self.height1 / 600
        wscale = self.width1 / 800
        self.titleLbl.setGeometry(10, 20, tmpwidth, 40)
        tmpx = 10
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = 270 * hscale
        self.itemList.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpx = (self.width1 - 720) / 2
        tmpy = hscale * 350
        self.engLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx =  (self.width1 / 2) + 30
        self.ruLbl.setGeometry(tmpx, tmpy, 330, 25)
        tmpx = (self.width1 - 720) / 2
        tmpy = hscale * 390 
        tmpstr = self.parent.sqldict["name"].strip("\'")
        tmpstr.strip("\'")
        newitem.append(tmpstr)
        tmpstr = self.parent.sqldict["runame"].strip("\'")
        tmpstr.strip("\'")
        newitem.append(tmpstr)
        tmpstr = self.parent.sqldict["variety"].strip("\'")
        newitem.append(tmpstr)
        self.finaldict[newitem[0]] = newitem
        self.enEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx =  (self.width1 / 2) + 30
        self.ruEdit.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 720) / 2
        tmpy = hscale * 440
        self.typeLbl.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 / 2) + 30
        self.declLbl.setGeometry(tmpx, tmpy, 330, 30)
        tmpx = (self.width1 - 720) / 2
        tmpy = hscale * 480
        self.typeBox.setGeometry(tmpx, tmpy, 330, 35)
        tmpx = (self.width1 / 2) + 30
        self.declBox.setGeometry(tmpx, tmpy, 330, 35)
        tmpy = self.height1 - 70
        tmpx = (self.width1 - 720) / 2
        tmpint = 720 / 5
        self.quitBttn.setGeometry(tmpx, tmpy, 110, 50)
        tmpx += tmpint
        self.findBttn.setGeometry(tmpx, tmpy, 110, 50)
        tmpx += tmpint
        self.deleteBttn.setGeometry(tmpx, tmpy, 110, 50)
        tmpx += tmpint
        self.newBttn.setGeometry(tmpx, tmpy, 110, 50)
        tmpx += tmpint
        self.addBttn.setGeometry(tmpx, tmpy, 110, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def createlist(self):
        """ Create a list of invariants from the database.
        """
        sqlcommand = "TABLE invariants ORDER BY name;\n"
        tmplist = list()
        newitem = list()
        self.dblist = list()
        self.finaldict = dict()
        tmpstr = self.apostrophe(self.parent.sqldict["name"].strip("\'"))
        newitem.append(tmpstr)
        tmpstr = self.parent.sqldict["runame"].strip("\'")
        newitem.append(tmpstr)
        tmpstr = self.parent.sqldict["wordcase"].strip("\'")
        newitem.append(tmpstr)
        tmpstr = self.parent.sqldict["variety"].strip("\'")
        newitem.append(tmpstr)
        self.finaldict[newitem[0]] = newitem
        try:
            sqldata = self.db.execute(sqlcommand)
        except Exception as e:
            errormessage =  "Unable to access variants in database: " + str(e)
            errorgui = ErrorDisplay(self)
            errorgui.exec()
            self.setVisible(True)
            self.activateWindow()
            self.cancel()
        datarows = self.parent.db.fetchall()
        self.columns = list()
        names = self.parent.db.description
        for x in names:
            self.columns.append(x.name)
        for x in datarows:
            if len(x) > 0:
                tmplist = list()
                for y in x:
                    tmplist.append(y)
                self.dblist.append(tmplist)

    def delete(self):
        """ Delete the selected lines. Multiple lines can be deleted at once.
        """
        tagtext = list()
        dellist = list()
        delitems = self.itemList.selectedItems()
        if not delitems:
            QMessageBox.warning(self, "No Item Selected", "An item must be selected to be deleted.", 
            QMessageBox.Ok, QMessageBox.NoButton)
            return
        for x in delitems:
            tmpstr = x.text()
            tmplist = tmpstr.split(sep=', ')
            dellist.append(tmplist)
        accumulator = ""
        lim = 0
        for x in dellist:
            tmpstr = "DELETE FROM invariants WHERE "
            tmpstr += "name=\'" + self.apostrophe(x[0]) + "\' AND "
            tmpstr += "runame=\'" + x[1] + "\' AND "
            tmpstr += "wordcase=\'" + x[2] + "\' AND "
            tmpstr += "variety=\'" + x[3] + "\'"
            tmpstr += ";\n"
            accumulator += tmpstr
        self.sqlcommand = accumulator
        try:
            self.db.execute(self.sqlcommand)
            self.conn.commit()
        except Exception as e:
            errormessage = "Error on database delelete row: " + str(e)
            self.setVisible(False)
            errorgui = ErrorDisplay(self)
            errorgui.activateWindow()
            errorgui.exec()
            self.setVisible(True)
            self.activateWindow()
            return
        self.showdata()
        return

    def showdata(self):
        """ Display the invariant list.
        """
        self.createlist()
        tmplist = list()
        newitem = list()
        self.itemList.clear()
        for x in self.dblist:
            tmpstr = self.comma.join(x)
            item = QListWidgetItem(tmpstr)
            self.itemList.addItem(item)            
        
    def pdecl(self):
        """ Collect the current item displayed 
            and place it in the line editors for editing.
            This occurs when the QListWidget is clicked.
        """
        found = False
        tmplist = list()
        newitem = list()
        item = self.itemList.currentItem()
        tmpstr = item.text()
        tmplist = tmpstr.split(self.comma)
        self.enEdit.setText(tmplist[0])
        self.ruEdit.setText(tmplist[1])
        index = self.types.declension.index(tmplist[2])
        self.declBox.setCurrentIndex(index)
        entries1 = sorted(self.types.invariant)
        index = entries1.index(tmplist[3])
        self.typeBox.setCurrentIndex(index)
        
    def clear(self):
        """ Clear the editors.
        """
        self.enEdit.setText("")
        self.ruEdit.setText("")

    def cancel(self):
        """ Cancel the event.
        """
        self.close()
    
    def finditem(self):
        """ Find a given piece of data in the QListWidget.
        """
        curr = 0
        lim = 0
        tmpstr = ""
        found = False
        self.findstr, accept = QInputDialog.getText(self, "Enter Data", "Enter data to find.", \
            QLineEdit.Normal, self.findstr)
        if accept:
            lim = self.itemList.count()
            for x in range(lim):
                item = self.itemList.item(x)
                tmpstr = item.text()
                index = tmpstr.find(self.findstr)
                if index >= 0:
                   curr = x
                   self.itemList.setCurrentRow(curr)
                   found = True
                   break
            if not found:
                QMessageBox.warning(self, "Item Not Found", "The item " + self.findstr + " was not found.", \
                    QMessageBox.Ok, QMessageBox.NoButton)
                
    def displayhelp(self):
        """ Display help for this GUI as an HTML page.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

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

    def additem(self):
        """ Get the item from the Line Editors and insert
            it into the database.
        """
        enteststr = self.enEdit.text()
        ruteststr = self.ruEdit.text()
        if len(enteststr) == 0 or len(ruteststr) == 0:
            QMessageBox.warning(self, "Missing Data", "There must be an English word and a Russian word present.")
            return
        tmpstr = self.quote + self.apostrophe(self.enEdit.text()) + self.quote + ", " + self.quote + self.ruEdit.text() + self.quote + ", " \
        + self.quote + self.declBox.currentText() + self.quote + ", " + self.quote + self.typeBox.currentText() + self.quote 
        self.sqlcommand = "INSERT INTO invariants (name, runame, wordcase, variety) VALUES(" + tmpstr + ");\n"
        self.db.execute(self.sqlcommand)
        self.conn.commit()
        self.showdata()
        self.enEdit.clear()
        self.ruEdit.clear()
        return

    def closeEvent(self, event):
        """ Close the form and pass along sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        
