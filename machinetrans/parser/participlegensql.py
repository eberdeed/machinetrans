"""
    ModalGen:  A class to generate English sentences
    with participles.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06-24-2016 San Diego California
"""

import sys, os
from machinetrans.parser.participle import Participle
from machinetrans.parser.artobj import ArtObj
from machinetrans.parser.wordgensql import WordGenSQL
from machinetrans.parser.subverb import SubVerb

class ParticipleGenSQL(WordGenSQL):
    """ A class to generate English sentences with participles.  
        This is a subclass of WordGenSQL which handles database 
        management and data generation.
    """
    def __init__(self):
        """ Initialize the class.
        """
        super(ParticipleGenSQL, self).__init__()
        return
    def makesentences(self, choice):
        """ Generate sentences.
        """
        if choice == 0:
            """ Generates the following:  A-S-V-AXV-PRT-O
                where A = article, S = subject, AXV = auxilliary verb and PRT = participle.
            """
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], capit=True)    
            tmpstr = sub.compose()
            self.datastr += "\n" + tmpstr
            sub = Participle( self.conn, self.sentence["articles"], self.sentence["participles"], obj=self.sentence["objects"])    
            tmpstr = sub.compose() + ". "
            self.datastr += " " + tmpstr
        elif choice == 1:    
            """ Generates the following:  A-S-V-AXV-PRT-PR-A-O
                where A = article, S = subject, AXV = auxilliary verb, Adj = Adjective, PR = Preposition and PRT = participle.
            """    
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], capit=True)    
            tmpstr = sub.compose()
            self.datastr += "\n" + tmpstr + " "
            sub = Participle( self.conn, self.sentence["articles"], self.sentence["participles"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], None, self.sentence["prepositions"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += " " + tmpstr
        elif choice == 2:    
            """ Generates the following:  A-ADJ-S-V-AXV-PRT-PR-A-ADJ-O
                where A = article, S = subject, TB = to be, AXV = auxilliary verb, PRT = participle, PR = Preposition, O = object and ADJ = adjective.
            """    
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], capit=True, adj=self.sentence["adjectives"])    
            tmpstr = sub.compose() + " "
            self.datastr += "\n" + tmpstr + " "
            sub = Participle( self.conn, self.sentence["articles"], self.sentence["participles"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"], self.sentence["prepositions"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += " " + tmpstr
        elif choice == 3:    
            """ Generates the following:  A-ADJ-S-V-AV-AXV-PRT-PR-A-ADJ-O
                where A = article, S = subject, TB = to be, PRT = participle, O = object, ADJ = adjective and AV = adverb.
            """    
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], capit=True, adj=self.sentence["adjectives"])    
            tmpstr = sub.compose() + " "
            sub = Participle( self.conn, self.sentence["articles"], self.sentence["participles"], adv=self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"], self.sentence["prepositions"])
            tmpstr += sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 4:    
            """ Generates the following:  A-ADJ-S-AV-V-AXV-PRT-PR-A-ADJ-O
                where A = article, S = subject, TB = to be, PRT = participle, O = object, ADJ = adjective and AV = adverb.
            """    
            sub = SubVerb( self.conn, self.sentence["articles"], self.sentence["subjects"], self.sentence["contemplatives"], capit=True, adj=self.sentence["adjectives"], adv=self.sentence["advsmanner"])    
            tmpstr = sub.compose() + " "
            sub = Participle( self.conn, self.sentence["articles"], self.sentence["participles"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"], self.sentence["prepositions"])
            tmpstr += sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

