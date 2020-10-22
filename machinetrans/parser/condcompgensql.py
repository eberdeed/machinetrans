"""
    ContmpGen:  A class to generate English sentences
    with comparative adjectives.
    Edward C. Eberle <eberdeed@eberdeed.net>
    July 4, 2016 San Diego California
"""

import sys, os
from machinetrans.parser.subverb import SubVerb
from machinetrans.parser.artobj import ArtObj
from machinetrans.parser.wordgensql import WordGenSQL
from machinetrans.parser.compare import Compare

class CondCompGenSQL(WordGenSQL):
    """ A class to generate English sentences
        with comparative adjectives.  This is 
        a subclass of WordGenSQL which handles 
        database management and data generation.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super(CondCompGenSQL, self).__init__()
        return
    
    def makesentences(self, choice):
        """ Generate sentences.
        """
        if choice == 0:
            """ Generates the following:  If A-S-V-Comp, then A-S-V
                where A = article, S = subject, V = verb and Comp = compartive adjective.
            """
            sub = Compare( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["comparatives"], False)    
            tmpstr = sub.compose()
            self.datastr += "\nIf " + tmpstr
            self.newvocab()
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, None, False)    
            tmpstr = sub.compose()
            self.datastr += ", then " + tmpstr + "."
        elif choice == 1:    
            """ Generates the following:  If A-S-V-Comp, then A-S-V-A-O
                where A = article, S = subject, V = verb, O = object and Comp = compartive adjective.
            """
            sub = Compare( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["comparatives"], False)    
            tmpstr = sub.compose()
            self.datastr += "\nIf " + tmpstr
            self.newvocab()
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, None, False)    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += ", then " + tmpstr
        elif choice == 2:    
            """
                Generates the following:  If A-S-V-Comp, then A-S-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object, ADJ = adjective and Comp = compartive adjective.
            """
            sub = Compare( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["comparatives"], False)    
            tmpstr = sub.compose()
            self.datastr += "\nIf " + tmpstr
            self.newvocab()
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, None, False)    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += ", then " + tmpstr
        elif choice == 3:    
            """ Generates the following:  If A-S-V-Comp, then A-S-AV-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object, ADJ = adjective, AV = adverb and Comp = compartive adjective.
            """
            sub = Compare( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["comparatives"], False)    
            tmpstr = sub.compose()
            self.datastr += "\nIf " + tmpstr
            self.newvocab()
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, None, False)    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += ", then " + tmpstr
        elif choice == 4:    
            """ Generates the following:  If A-S-V-Comp, then A-ADJ-S-AV-V-A-ADJ-O
                where A = article, S = subject, V = verb, O = object, ADJ = adjective, AV = adverb and Comp = compartive adjective.
            """
            sub = Compare( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["comparatives"], False)    
            tmpstr = sub.compose()
            self.datastr += "\nIf " + tmpstr
            self.newvocab()
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], None, None, False)    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += ", then " + tmpstr

  
