"""
    WordGenSQL:  A base class to generate English sentences.
    This base class contains the database management and 
    random word selection routines.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06-24-2016 San Diego California
"""

import sys, os, time, random
import psycopg2 as pg_driver
from machinetrans.data.wordtype import WordType
from machinetrans.parser.subverb import SubVerb
from machinetrans.parser.artobj import ArtObj
class WordGenSQL:
    """ A base class to generate English sentences.
        This base class contains the database management and 
        random word selection routines.
    """
    wordinfo = WordType()
    itemvals = dict()
    classlist = list()
    namelist = list()
    tmpstr = ""
    datastr = ""
    subject = True
    conn = None
    db = None
    sentence = dict()
    sqlcommand = "SELECT DISTINCT name FROM {};\n"
    sqlcommandpron = "SELECT DISTINCT (name, gender) FROM pronouns WHERE variety=\'personal\'" \
        + " AND wordcase=\'nominative\';\n"
    sqlcommandnoun = "SELECT DISTINCT (name, variety, gender) FROM nouns;\n"
    sqlcommandverb = "SELECT DISTINCT (name, variety, tense) FROM verbs WHERE tense=\'simple present\';\n"
    sqlcommandadv = "SELECT DISTINCT name FROM adverbs WHERE variety=\'manner\';\n"
    sqlcommandpart = "SELECT DISTINCT (enval, variety) FROM participles WHERE gender=\'masculine\'" \
        + " AND wordcase=\'nominative\';\n"
    sqlcommandadj = "SELECT DISTINCT (name, variety) FROM adjectives WHERE (variety=\'descriptive\' OR " \
        + "variety=\'comparative\') AND wordcase=\'nominative\';\n"
    sqlcommandpart = "SELECT DISTINCT (enval, variety) FROM participles WHERE (variety=\'present active\' OR " \
        + "variety=\'present passive\' OR variety=\'past active\' OR variety=\'past passive\') AND " \
        + "gender=\'masculine\' AND wordcase=\'nominative\';\n"
    sqlcurrent = ""
    genclass = frozenset(["subjects", "objects", "adjectives", "contemplatives", \
        "advsmanner", "interjections", "prepositions", "symbols", "articles",\
        "conjunctions", "interrogatives", "motions", "participles", \
        "verbs", "comparatives"])
    articles = list(["a", "the"])
    
    def __init__(self):
        """ Initialize the class, connect to the database and get the data to randomize.
        """
        tmpint = time.time()
        tmpint %= 100000000
        random.seed(tmpint)
        self.conn = pg_driver.connect( \
            user = 'machinetrans', \
            password = 'MachineTrans', \
            dbname = 'machinetrans', \
            host = 'localhost', \
            port = 5432 \
            )
        self.db = self.conn.cursor()
        self.readdata()
        return
    
    def readdata(self):
        """ Here the data is read.  A token representing the word, and sometimes the entire entry, are
            read and then added to a list, which is then added to a dictionary for each class.
        """
        # In this for loop all the data used by the word generator is processed.
        for x in self.wordinfo.wordclass:
            if x == "past tense verb":
                continue
            self.tmpstr = x + "s"
            # The exceptions.
            if self.tmpstr != "pronouns" and self.tmpstr != "verbs" and \
                self.tmpstr != "adverbs" and self.tmpstr != "participles" and \
                self.tmpstr != "adjectives" and self.tmpstr != "nouns":
                self.sqlcurrent = self.sqlcommand.format(self.tmpstr)
                self.db.execute(self.sqlcurrent)
                datalist = self.db.fetchall()
            elif ((self.tmpstr == "pronouns") or 
                (self.tmpstr == "verbs") or
                (self.tmpstr == "participles") or
                (self.tmpstr == "nouns") or 
                (self.tmpstr == "adjectives")):
                self.db.execute(self.sqlcurrent)
                datalist = self.db.fetchall()
            elif self.tmpstr == "adverbs":
                self.tmpstr = "advsmanner"
                self.db.execute(self.sqlcurrent)
                datalist = self.db.fetchall()
            self.namelist = list()
            for z in datalist:
                y = z[0]
                self.namelist.append(y)    
            self.itemvals[self.tmpstr] = self.namelist
        # Process the exceptions.
        subjlist = list()
        objlist = list()
        for x in self.itemvals["pronouns"]:
            entry = list()
            entry.append("pronoun")
            for y in x:
                entry.append(y)
            if self.subject:
                subjlist.append(entry)
                self.subject = False
            else:
                objlist.append(entry)
                self.subject = True
        for x in self.itemvals["nouns"]:
            entry = list()
            entry.append("noun")
            for y in x:
                if len(y) > 0:
                    entry.append(y)
            if self.subject:
                subjlist.append(entry)
                self.subject = False
            else:
                objlist.append(entry)
                self.subject = True
        del(self.itemvals["pronouns"])
        del(self.itemvals["nouns"])
        self.itemvals["subjects"] = subjlist
        self.itemvals["objects"] = objlist
        partlist = list()
        for x in self.itemvals["participles"]:
            entry = list()
            for y in x:
                entry.append(y)
            partlist.append(entry)
        del(self.itemvals["participles"])
        self.itemvals["participles"] = partlist
        contmp = list()
        modal = list()
        motion = list()
        adverbs = list()
        for x in self.itemvals["verbs"]:
            if x[1] == "other":
                contmp.append(list([x[0], x[2]]))
            else:
                motion.append(list([x[0], x[2]]))
        comp = list()
        for x in self.itemvals["adjectives"]:
            if x[1] == "comparative":
                comp.append(x[0])
                self.itemvals["adjectives"].remove(x)
        self.itemvals["contemplatives"] = contmp
        self.itemvals["motions"] = motion
        self.itemvals["comparatives"] = comp
        self.itemvals["articles"] = self.articles
        
            
    def newitem(self, wtype):
        """ Take the tokenized data and choose a random entry.
        """
        lim = 0
        tmpint = 0
        itemlist = list()
        wordval = ""
        lim = len(self.itemvals[wtype])
        if lim == 0:
            print("Error no values for " + wtype + ".")
            return (wtype.capitalize() + " error.")
        lim -= 1
        tmpint = round(random.random() * lim)
        tmplist =  self.itemvals[wtype][tmpint][:]
        return tmplist

    def wordgen(self, choice):
        """ Choose random data and call makesentence to put 
            it in a sentence.  makesentence is defined in a subclass.
        """
        for e in range(100):
            self.sentence.clear()
            for x in self.genclass:
                self.sentence[x] = self.newitem(x)
            self.makesentences(choice)
                
    def newvocab(self):
        """ Reinitialize the randomly generated sentence vocabulary.
        """
        for x in self.genclass:
            self.sentence[x] = self.newitem(x)

    def makesentences(self, choice):
        """ Provide sentence generation code here.
        """
        return

    def data(self):
        """ Return the generated sentence data.
        """
        return self.datastr
  
