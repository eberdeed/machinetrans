"""
    LineEditEN:  A subclass for QLineEdit to catch the "Return" keypress
    and the loss of focus event. This line editor accepts only English.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 15, 2016, San Diego California United States of America
"""
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LineEditEN(QLineEdit):
    """ A subclass for QLineEdit to catch the "Return" keypress
        and the loss of focus event.
    """

    enall = ("a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "-"
    "_", "\"", "\'", "`", "~", "-", "+", "=", "?", ":", ";")
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    qtkeys = (0, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab, Qt.Key_Backspace, 
        Qt.Key_Return, Qt.Key_Enter, Qt.Key_Insert, Qt.Key_Delete, 
        Qt.Key_Clear, Qt.Key_Home, Qt.Key_End, Qt.Key_Left, Qt.Key_Up, 
        Qt.Key_Right, Qt.Key_Down, Qt.Key_Shift, Qt.Key_Control, 
        Qt.Key_Meta, Qt.Key_Alt, Qt.Key_AltGr, Qt.Key_CapsLock)
    returnval = Qt.Key_Return
    firereturn = None
    firefocus = None
    parent = None
    
    def __init__(self, parent=None):
        """ Initialize the class.
        """
        super(LineEditEN, self).__init__(parent)
        self.firereturn = QAction("Fire Return", self)
        self.firefocus = QAction("Out of Focus", self)
        return

    def keyPressEvent(self, event):
        """ Catch the <RETURN> key.
        """
        key = event.key()
        tmpchar = event.text()
        if (not tmpchar in self.enall and not tmpchar in self.numbers 
        and not key in self.qtkeys):
            (QMessageBox.warning(self, "Error in Charset", 
            "You entered a non-English character where a English character was required."))
            return
        if key == self.returnval:
            self.firereturn.trigger()
            return
        QLineEdit.keyPressEvent(self, event)
          
    def focusOutEvent(self, event):
        """ Catch the Focus Out event.
        """
        self.firefocus.trigger()
        QLineEdit.focusOutEvent(self, event)