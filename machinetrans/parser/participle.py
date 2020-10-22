"""
    Participle: A class to encapsulate a participial verb construct.
    and potentially an article an adjective and an adverb.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""
from machinetrans.data.engword import EngWord
from machinetrans.data.wordtype import WordType

class Participle:
    """ Creates a grammatical structure for the end of an English
        sentence of the form:
         [adverb] auxilliary verb participle [article] [adjective] subject.
    """
    english = EngWord()
    types = WordType()
    pronouns = list()
    art = None
    sub = None
    verb = None
    participle = None
    adj = None
    adv = None
    cap = False
    output = ""
    tense = ""
    conn = None
    db = None
    def __init__(self, conn, art, participle, adj=None, obj=None, adv=None, capitalize=False):
        self.conn = conn
        self.db = conn.cursor()
        self.art = art
        self.obj = obj
        self.participle = participle
        self.adj = adj
        self.adv = adv
        self.cap = capitalize
        

    def compose(self):
        wtype = "type error"
        verbstr = "verb error"
        person = "third"
        verbstr = None
        self.output = ""
        self.partstr = self.participle[0]
        self.tense = self.participle[1]
        if self.partstr.startswith("was "):
            self.partstr = self.partstr[4:]
            verbstr = self.english.tobepast[person]
        if self.partstr.startswith("were "):
            self.partstr = self.partstr[5:]
            verbstr = self.english.tobepast[person]
        elif self.partstr.startswith("to be "):
            self.partstr = self.partstr[6:]
            verbstr = self.english.tobe[person]
        elif self.partstr.startswith("to have "):
            self.partstr = self.partstr[8:]
            verbstr = self.english.tohave[person]
        if verbstr:
            self.partstr = verbstr + " " + self.partstr
        # Add an "n" to the indefinite article "a" if necessary.
        article = self.art
        if self.obj:
            article = "Error Value"
            if self.obj[0] == "noun": 
                if "plural" == self.obj[3]:
                    article = "the"
                else:
                    article = "a"
            if self.obj[0] == "pronoun":
                if "plural" == self.obj[2]:
                    article = "the"
                else:
                    article = "a"
            if self.adj:
                if article == "a" and self.adj[0][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    article += "n"
            else:
                if article == "a" and self.obj[1][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    article += "n"
        # Generate the construct.
        if self.cap:
            if self.adv:
                self.output = self.adv.capitalize() + " " + self.partstr
            else:
                self.output = self.partstr.capitalize()
        else:
            if self.adv:
                self.output = self.adv + " " + self.partstr
            else:
                self.output = self.partstr
            
        if self.obj:
            if self.adj:
                self.output += " " + article + " " + self.adj[0] + " " + self.obj[1]
            else:
                self.output += " "  + article + " " + self.obj[1]
        self.output = self.output.strip()
        return(self.output)

        
