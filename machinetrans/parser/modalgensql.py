"""
    Currently not being used.
    ModalGenSQL:  A class to generate English sentences
    with modal verbs.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06-24-2016 San Diego California
"""

import sys, os
from machinetrans.parser.modalinf import ModalInf
from machinetrans.parser.artobj import ArtObj
from machinetrans.parser.wordgensql import WordGenSQL

class ModalGenSQL(WordGenSQL):
    """ Currently not being used.
        A class to generate English sentences with modal verbs.  
        This is a subclass of WordGenSQL
        which handles database management and data generation.
    """
    def __init__(self):
        """ Initialize the class.
        """
        super(ModalGenSQL, self).__init__()
        return
    
    def makesentences(self, choice):
        """ Generate sentences.
        """
        if choice == 0:
            sub = ModalInf( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["modals"], self.sentence["verbs"])    
            tmpstr = sub.compose() + ". "
            self.datastr += "\n" + tmpstr
    
        elif choice == 1:    
            sub = ModalInf( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["modals"], self.sentence["verbs"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

        elif choice == 2:    
            sub = ModalInf( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["modals"], self.sentence["verbs"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

        elif choice == 3:    
            sub = ModalInf( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["modals"], self.sentence["verbs"], None, self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

        elif choice == 4:    
            sub = ModalInf( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["modals"], self.sentence["verbs"], self.sentence["adjectives"], self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

  
"""
article subject verb
article subject verb article object
article subject verb article adjective object
article subject adverb verb article object
article subject adverb verb article adjective object
article subject verb article object article object
"""
