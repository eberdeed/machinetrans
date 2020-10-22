#!/usr/bin/python3
"""
    SQLData:  Machine Translation Data Entry -- SQL Data Editor.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    July 2, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_sqldata import Ui_SQLData
from machinetrans.dataentry.editdata import EditData
from machinetrans.dataentry.sortedkeys import SortedKeys
from machinetrans.helpview import HelpView

class SQLData(QDialog, Ui_SQLData):
    """ A GUI to display an SQL command with data for editing.
    """

    helpfile = "/usr/share/machinetrans/resources/sqldata.html"
    parent = None
    wclass = ""
    types = None
    sortlist = list()
    columns = list()
    conn = None
    db = None
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    findstr = ""
    data = ""
    comma = ", "
    
    def __init__(self, parent=None):
        """ Initialize and display the data.
        """
        super(SQLData, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.conn = self.parent.conn
        self.db = self.conn.cursor()
        self.types = self.parent.types
        self.wclass = self.parent.wclass
        tmpstr = self.titleLbl.text()
        tmpstr += " -- " + self.parent.wclass.capitalize()
        self.titleLbl.setText(tmpstr)
        self.listDisplay.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.findBttn.clicked.connect(self.find)
        self.quitBttn.clicked.connect(self.close)
        self.delBttn.clicked.connect(self.delete)
        self.editBttn.clicked.connect(self.edit)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.sortBttn.clicked.connect(self.sortitems)
        self.showdata()
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.quitBttn.setFocus()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        wscale = self.width1 / 800
        self.titleLbl.setGeometry(10, 20, tmpwidth, 40)
        tmpx = 10
        tmpy = 70
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 160
        self.listDisplay.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpint = self.width1 / 5
        tmpx = (self.width1 - ((tmpint * 4) + 150)) / 2
        self.editBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.delBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.sortBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.findBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpx += tmpint
        self.quitBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def showdata(self):
        """ Draw the data on a QListWidget.  This makes each line of 
            data selectable.
        """
        tmpstr = ""
        self.sqlcommand = "TABLE " + self.parent.wclass + "s ORDER BY name;\n"
        self.listDisplay.clear()
        self.db.execute(self.sqlcommand)
        dataobj = self.db.fetchall()
        self.columns = list()
        names = self.db.description
        for x in names:
            self.columns.append(x.name)
        for x in dataobj:
            tmpstr = ""
            if len(x) > 0:
                for y in x:
                    tmpstr += str(y) + ", "
                tmpstr = tmpstr[:-2]
                item = QListWidgetItem(tmpstr)
                self.listDisplay.addItem(item)            
        
        
    def find(self):
        """ Find a given piece of data in the QListWidget.
        """
        curr = 0
        lim = 0
        tmpstr = ""
        found = False
        self.findstr, accept = QInputDialog.getText(self, "Please enter the text to find.", "Text Value:", \
            QLineEdit.Normal, self.findstr)
        if accept:
            curr = self.listDisplay.currentRow()
            if curr < 0:
                curr = 0
            else:
                curr += 1
            lim = self.listDisplay.count()
            for x in range(curr, lim, 1):
                item = self.listDisplay.item(x)
                tmpstr = item.text()
                index = tmpstr.find(self.findstr)
                if index >= 0:
                   curr = x
                   self.listDisplay.setCurrentRow(curr)
                   found = True
                   break
            if not found and curr > 0:
                lim = curr
                curr = 0
                for x in range(curr, lim, 1):
                    item = self.listDisplay.item(x)
                    tmpstr = item.text()
                    index = tmpstr.find(self.findstr)
                    if index >= 0:
                        curr = x
                        self.listDisplay.setCurrentRow(curr)
                        found = True
                        break
            if not found:
                QMessageBox.warning(self, "Item Not Found", "The item " + self.findstr + " was not found.", \
                    QMessageBox.Ok, QMessageBox.NoButton)
    
    def delete(self):
        """ Delete the selected lines. Multiple lines can be deleted at once.
        """
        itemlist = list()
        tagtext = list()
        basecommand = "DELETE FROM " + self.parent.wclass + "s WHERE "
        accumulator = ""
        lim = 0
        tagval = self.listDisplay.selectedItems()
        if not tagval:
            QMessageBox.warning(self, "No Item Selected", "Please select an item for deleting.")
            return
        for x in tagval:
            tagtext.append(x.text())
        else:
            for tagitem in tagtext:
                itemlist = tagitem.split(", ")
                if len(self.columns) == len(itemlist):
                    lim = len(self.columns)
                    tmpstr = ""
                    for x in range(lim):
                        if (itemlist[x] == 'None'):
                            continue
                        else:
                            index = itemlist[x].find('\'')
                            while(index >= 0):
                                tmpstr1 = itemlist[x][:index]
                                tmpstr1 += '\''
                                tmpstr1 += itemlist[x][index:]
                                itemlist[x] = tmpstr1
                                tmpint = index + 2
                                index = itemlist[x].find('\'', tmpint)
                            tmpstr += self.columns[x] + "=\'" + itemlist[x] + "\' AND "
                    tmpcommand = tmpstr[:-6]
                    tmpcommand += "\';\n"
                    tmpcommand = basecommand + tmpcommand
                    accumulator += tmpcommand
                else:
                    QMessageBox.warning(self, "Unmatched Data", "There is more data than columns to put it in.")
            self.db.execute(accumulator)
            self.conn.commit()
            self.showdata()
        return

    def edit(self):
        """ Edit the SQL data using the EditData class.  Put the edited
            data back into the database.
        """
        tagtext = list()
        itemlist = list()
        self.data = ""
        delcommand = "DELETE FROM " + self.parent.wclass + "s WHERE "
        inscommand = "INSERT INTO " + self.parent.wclass + "s "
        accumulator = ""
        tagval = self.listDisplay.selectedItems()
        if not tagval:
            QMessageBox.warning(self, "No Item Selected", "Please select an item for editing.")
            return
        for x in tagval:
            self.data += x.text() + "\n"
            itemlist.append(x.text())
        editor = EditData(self)
        editor.activateWindow()
        editor.exec()
        self.activateWindow()
        for tagitem in itemlist:
            tmplist = tagitem.split(", ")
            if len(self.columns) == len(tmplist):
                lim = len(self.columns)
                tmpstr = ""
                for x in range(lim):
                    if tmplist[x] == 'None':
                        continue
                    else:
                        index = tmplist[x].find('\'')
                        while(index >= 0):
                            tmpstr1 = tmplist[x][:index]
                            tmpstr1 += '\''
                            tmpstr1 += tmplist[x][index:]
                            tmplist[x] = tmpstr1
                            tmpint = index + 2
                            index = tmplist[x].find('\'', tmpint)
                        tmpstr += self.columns[x] + "=\'" + tmplist[x] + "\' AND "
                lim = len(tmpstr)
                lim -= 6
                tmpstr = tmpstr[:lim]
                tmpstr += "\';\n"
                tmpstr = delcommand + tmpstr
                accumulator += tmpstr
        self.db.execute(accumulator)
        self.conn.commit()
        tagval = self.data.split("\n")
        for tagitem in tagval:
            itemlist = tagitem.split(", ")
            if len(self.columns) == len(itemlist):
                tmpstr = "("
                for x in self.columns:
                    tmpstr += x + ", "
                tmpstr = tmpstr[:-2] + ") VALUES("
                for x in itemlist:
                    index = x.find('\'')
                    while(index >= 0):
                        tmpstr1 = x[:index]
                        tmpstr1 += '\''
                        tmpstr1 += x[index:]
                        x = tmpstr1
                        tmpint = index + 2
                        index = x.find('\'', tmpint)
                    tmpstr += "\'" + x + "\', "
                tmpstr = tmpstr[:-2] + ");\n"
                tmpstr = inscommand + tmpstr
                accumulator += tmpstr
        self.db.execute(accumulator)
        self.conn.commit()
        self.showdata()
        
    def sortitems(self):
        self.sortlist = list()
        sorter = SortedKeys(self)
        sorter.exec()
        if len(self.sortlist) > 1:
            tmpstr = self.comma.join(self.sortlist)
        else:
            self.sortlist.append("name")
            self.sortlist.append("runame")
            tmpstr = self.comma.join(self.sortlist)
        self.sqlcommand = "TABLE " + self.parent.wclass + "s ORDER BY " + tmpstr + ";\n"
        self.listDisplay.clear()
        self.db.execute(self.sqlcommand)
        dataobj = self.db.fetchall()
        self.columns = list()
        names = self.db.description
        for x in names:
            self.columns.append(x.name)
        for x in dataobj:
            tmpstr = ""
            if len(x) > 0:
                for y in x:
                    tmpstr += str(y) + ", "
                tmpstr = tmpstr[:-2]
                item = QListWidgetItem(tmpstr)
                self.listDisplay.addItem(item)            
        
    def displayhelp(self):
        """ Display an HTML help page for this GUI.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def closeEvent(self, event):
        """ Close the GUI and pass along sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        
