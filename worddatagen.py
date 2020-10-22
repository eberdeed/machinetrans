#!/usr/bin/python3
"""
    WordDataGen:  Machine Translation English Sentence Generator.
    Here the user selects a given sentence pattern, the class
    supporting that sentence is called and the data retrieved and displayed.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    July 4, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# Supporting classes.
from machinetrans.userinterfaces.ui_worddatagen import Ui_WordDataGen
from machinetrans.parser.wordmenu import WordMenu
from machinetrans.parser.modalgensql import ModalGenSQL
from machinetrans.parser.contmpgensql import ContmpGenSQL
from machinetrans.parser.movegensql import MoveGenSQL
from machinetrans.parser.datadisplay import DataDisplay
from machinetrans.parser.participlegensql import ParticipleGenSQL
from machinetrans.parser.interroggensql import InterrogGenSQL
from machinetrans.parser.conditionalgensql import ConditionalGenSQL
from machinetrans.parser.condcompgensql import CondCompGenSQL
from machinetrans.helpview import HelpView

class WordDataGen(QDialog, Ui_WordDataGen):
    """ A GUI to display English sentences.
    """
    helpfile = "/usr/share/machinetrans/resources/worddatagen.html"
    datatype = ""
    datastr = ""
    # Contains all the sentence pattern data
    # in form of strings for display in a menu.
    menudata = WordMenu()
    tmplist = list()
    tmpstr = ""
    tmpint = 0
    winx = 0
    winy = 0
    width1 = 0
    height1 = 0
    geometry = list()    
    usrdir = ""
    # Configuration directory
    confdir = ".config"
    progdir = ""
    # Configuration file.
    progconf = "machinetrans.conf"
    
    def __init__(self, parent=None):
        """ Initialize a QDialog. and call the main menu.
        """
        super(WordDataGen, self).__init__(parent)
        self.setupUi(self)
        # The user's home directory.
        self.usrdir = os.environ["HOME"]
        self.confdir = os.path.join(self.usrdir, self.confdir)
        if not os.path.exists(self.confdir):
            try:
                os.mkdir(self.confdir)
            except Exception as e:
                QMessageBox.critical(self, "Fatal Error", "Could not create the directory " \
                    + self.confdir + "\n" +  str(e), QMessageBox.Ok, QMessageBox.NoButton)
                sys.exit(1)
        else:
            self.progdir = os.path.join(self.confdir, "machinetrans")
            # if the programs configure directory does not exist, create it.
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
        # If the data is present, set the window geometry.
        if (self.winx >= 0 and self.winy >= 0 and self.width1 > 0 and self.height1 > 0):
            self.setGeometry(self.winx, self.winy, self.width1, self.height1)
        # Connect the signals to the methods.
        self.listDisplay.itemClicked.connect(self.accept)
        self.quitBttn.clicked.connect(self.quit)
        self.acceptBttn.clicked.connect(self.accept)
        self.backBttn.clicked.connect(self.mainmenu)
        self.helpBttn.clicked.connect(self.displayhelp)
        self.mainmenu()

    def resizeEvent(self, event):
        """ A method to resize the GUI.
        """
        dim = event.size()
        self.height1 = dim.height()
        self.width1 = dim.width()
        tmpy = 10
        tmpx = self.width1 - 160
        self.helpBttn.setGeometry(tmpx, tmpy, 150, 50)
        tmpwidth = self.width1 - 20
        self.titleLbl.setGeometry(10, 10, tmpwidth, 40)
        tmpx = 10
        tmpy = 60
        tmpwidth = self.width1 - 20
        tmpheight = self.height1 - 160
        self.listDisplay.setGeometry(tmpx, tmpy, tmpwidth, tmpheight)
        tmpy = self.height1 - 80
        tmpint = (self.width1 - 300) / 3
        tmpx = (self.width1 - ((tmpint * 2) + 130)) / 2
        self.quitBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.backBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpx += tmpint
        self.acceptBttn.setGeometry(tmpx, tmpy, 130, 50)
        tmpos = self.pos()
        self.winx = tmpos.x()
        self.winy = tmpos.y()
        self.geometry = list([self.winx, self.winy, self.width1, self.height1])
        
    def mainmenu(self):
        """ Display a list of the main English
            sentence structures.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.mainmenu)
        self.tmpstr = self.tmplist.pop(0)
        self.titleLbl.setText(self.tmpstr)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.titleLbl.setText(self.tmpstr)
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.accept)
        self.acceptBttn.clicked.connect(self.accept)
        
    def accept(self):
        """ Direct the program to the desired method.
        """
        self.tmpint = self.listDisplay.currentRow()
        if self.tmpint == 0:
            self.contemplation()
        elif self.tmpint == 1:
            self.motion()
        elif self.tmpint == 2:
            self.participle()
        elif self.tmpint == 3:
            self.interrogative()
        elif self.tmpint == 4:
            self.conditional()
        elif self.tmpint == 5:
            self.comparative()

    def contemplation(self):
        """ Display the contemplative verb menu.
            I use "contemplative" to distinguish
            these verbs from verbs of motion.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.contemplation)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosecontmp)
        self.acceptBttn.clicked.connect(self.choosecontmp)
        
    def motion(self):
        """ Display the menu for verbs of motion.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.motion)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosemotion)
        self.acceptBttn.clicked.connect(self.choosemotion)
    """
    def modal(self):
    """
    """
            Display the modal verb menu.
    """
    """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.modal)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosemodal)
        self.acceptBttn.clicked.connect(self.choosemodal)
    """
    def participle(self):
        """ Display the participial verb menu.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.participle)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosepart)
        self.acceptBttn.clicked.connect(self.choosepart)

    def interrogative(self):
        """ Display the interrogative sentence menu.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.interrogative)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.chooseinterrog)
        self.acceptBttn.clicked.connect(self.chooseinterrog)

    def conditional(self):
        """ Display the conditional sentence menu.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.conditional)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosecondit)
        self.acceptBttn.clicked.connect(self.choosecondit)

    def comparative(self):
        """ Display the comparative sentence menu.
        """
        self.listDisplay.clear()
        self.tmplist = list(self.menudata.comparative)
        self.datatype = self.tmplist.pop(0)
        self.titleLbl.setText(self.datatype)
        for x in self.tmplist:
            item = QListWidgetItem(x)
            self.listDisplay.addItem(item)            
        self.listDisplay.itemClicked.disconnect()
        self.acceptBttn.clicked.disconnect()
        self.listDisplay.itemClicked.connect(self.choosecompare)
        self.acceptBttn.clicked.connect(self.choosecompare)

    def choosecontmp(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = ContmpGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()
        
    def choosemotion(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = MoveGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()
    """    
    def choosemodal(self):
         Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = ModalGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()
    """    
    def choosepart(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = ParticipleGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()
        
    def chooseinterrog(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = InterrogGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()

    def choosecondit(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = ConditionalGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()

    def choosecompare(self):
        """ Choose a sentence type. Instantiate the desired class,
            call the makesentence method for that class and 
            collect and display the data.
        """
        self.tmpint = self.listDisplay.currentRow()
        listitem = self.listDisplay.selectedItems()
        self.datatype += " " + listitem[0].text()
        sengen = CondCompGenSQL()
        sengen.wordgen(self.tmpint)
        self.datastr = sengen.data()
        self.datastr = self.datastr[1:]
        self.mainmenu()
        display = DataDisplay(self)
        self.setVisible(False)
        display.show()

    def displayhelp(self):
        """ Display a help file in HTML format.
        """
        helper = HelpView(self)
        helper.activateWindow()
        helper.exec()
        self.activateWindow()

    def quit(self):
        """ Close the GUI.
        """
        self.close()
        
    def closeEvent(self, event):
        """ The last method called by the GUI before
            it disappears.
        """
        fname = os.path.join(self.progdir, self.progconf)
        try:
            textfile = open(fname, "w", newline="\n", encoding="utf-8")
            for x in self.geometry:
                textfile.write(str(x) + "\n")
            textfile.close()
        except Exception as e:
            print("\n\nUnable to save program window geometry.\n\n")
        event.accept()
        
def main():  # Remember the Maine.
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        font = app.font()
        font.setPointSize(16)
        app.setFont(font)
        entry = WordDataGen()
        entry.show()
        app.exec()
    return 0

main()         