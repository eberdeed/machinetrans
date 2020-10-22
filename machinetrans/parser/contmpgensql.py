"""
    ContmpGenSQL:  A class to generate English sentences
    with contemplative verbs (i.e. verbs that are not
    verbs of motion).
    Edward C. Eberle <eberdeed@eberdeed.net>
    July 4, 2016 San Diego California
"""

import sys, os
from machinetrans.parser.subverb import SubVerb
from machinetrans.parser.artobj import ArtObj
from machinetrans.parser.wordgensql import WordGenSQL

class ContmpGenSQL(WordGenSQL):
    """ A class to generate English sentences
        with contemplative verbs (i.e. verbs that are not
        verbs of motion).  This is a subclass of WordGenSQL
        which handles database management and data generation.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super(ContmpGenSQL, self).__init__()
        return
    
    def makesentences(self, choice):
        """ Generate sentences.
        """
        if choice == 0:
            """ Generates the following:  A-S-V
                where A = article, S = subject and V = verb.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"])    
            tmpstr = sub.compose() + ". "
            self.datastr += "\n" + tmpstr
        elif choice == 1:    
            """ Generates the following:  A-S-V-A-O
                where A = article, S = subject, V = verb and O = object.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 2:    
            """ Generates the following:  A-S-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object and ADJ = adjective.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 3:    
            """ Generates the following:  A-S-AV-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object, ADJ = adjective and AV = adverb.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 4:    
            """ Generates the following:  A-ADJ-S-AV-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object, ADJ = adjective and AV = adverb.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], self.sentence["adjectives"], self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
