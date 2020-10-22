#!/usr/bin/python3
"""
    SQLTest:  Machine Translation Data Entry -- SQL Command Checker.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    July 1, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.userinterfaces.ui_sqltest import Ui_SQLTest
from machinetrans.helpview import HelpView

class SQLTest(QDialog, Ui_SQLTest):
    """ A GUI to check SQL data while entering data.
        The program accumulates SQL commands as it 
        collects data, this GUI allows viewing of those commands
        before they are placed before the user to
        be committed to the database.
    """
    
    helpfile = "/usr/share/machinetrans/resources/sqltest.html"
    parent = None
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    
    def __init__(self, parent=None):
        """ Initialize the GUI and display the SQL commands.
        """
        super(SQLTest, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        tmpstr = self.titleLbl.text() + " "
        tmpstr +=  self.parent.enstr.capitalize()
        self.titleLbl.setText(tmpstr)
        self.sqlEdit.setText(self.parent.sqlcommand)
        self.cancelBttn.clicked.connect(self.cancel)
        self.acceptBttn.clicked.connect(self.accept)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.setGeometry(self.parent.geometry[0], self.parent.geometry[1], self.parent.geometry[2], self.parent.geometry[3])
        self.acceptBttn.setFocus()
        
    def resizeEvent(self, event):
        """ Resize the GUI and record GUI sizing information.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 20, tmpwidth, 25)
        tmpx = 10
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 140
        self.sqlEdit.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 65
        tmpint = (self.width1 - 300) / 2
        tmpx = (self.width1 - (tmpint + 130)) / 2
        self.cancelBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])

    def accept(self):
        """ Accept the command as displayed and close the form.
        """
        self.parent.sqlcommand = self.sqlEdit.toPlainText()
        self.parent.setVisible(True)
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
        self.parent.setVisible(True)
        self.parent.wordclasses()
        self.close()

    def closeEvent(self, event):
        """ Close the GUI and pass along GUI sizing information.
        """
        self.parent.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        event.accept()        