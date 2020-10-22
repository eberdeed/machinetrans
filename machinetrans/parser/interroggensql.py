"""
    InterrogGenSQL:  A class to generate English sentences
    with interrogatives (i.e. verbs that are not
    verbs of motion.
    Edward C. Eberle <eberdeed@eberdeed.net>
    July 4, 2016 San Diego California
"""

import sys, os, time, random
from machinetrans.parser.interrog import Interrog
from machinetrans.parser.artobj import ArtObj
from machinetrans.parser.wordgensql import WordGenSQL

class InterrogGenSQL(WordGenSQL):
    """ A class to generate English sentences
        with interrogatives.  This is a subclass of WordGenSQL
        which handles database management and data generation.
    """

    def __init__(self):
        """ Initialize the class.
        """
        tmpint = time.time()
        tmpint %= 100000
        random.seed(tmpint)
        super(InterrogGenSQL, self).__init__()
        return
    
    def makesentences(self, choice):
        """ Generates sentences.
        """
        tmpint = random.randint(0, 1)
        if tmpint == 0:
            self.sentence["interrogatives"] = "who"
        else:
            self.sentence["interrogatives"] = "what"

        if choice == 0:
            """ Generates the following:  I-V
                where I = interrogative and V = verb.
            """
            sub = Interrog( self.conn, self.sentence["interrogatives"], self.sentence["verbs"])    
            tmpstr = sub.compose() + ". "
            self.datastr += "\n" + tmpstr
        elif choice == 1:    
            """ Generates the following:  I-V-O
                where I = interrogative, V = verb and O = object.
            """
            sub = Interrog( self.conn, self.sentence["interrogatives"], self.sentence["verbs"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 2:    
            """ Generates the following:  I-V-ADJ-O
                where I = interrogative, V = verb, O = object and ADJ = adjective.
            """
            sub = Interrog( self.conn, self.sentence["interrogatives"], self.sentence["verbs"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 3:    
            """ Generates the following:  I-AV-V-O
                where I = interrogative, V = verb, O = object and AV = adverb.
            """
            sub = Interrog( self.conn, self.sentence["interrogatives"], self.sentence["verbs"], self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr
        elif choice == 4:    
            """ Generates the following:  I--AV-V-ADJ-O
                where I = interrogative, V = verb, O = object, ADJ = adjective and AV = adverb.
            """
            sub = Interrog( self.conn, self.sentence["interrogatives"], self.sentence["verbs"], self.sentence["advsmanner"])    
            obj = ArtObj(self.sentence["articles"], self.sentence["objects"], self.sentence["adjectives"])
            tmpstr = sub.compose() + " "
            tmpstr += obj.compose() + "."
            self.datastr += "\n" + tmpstr

