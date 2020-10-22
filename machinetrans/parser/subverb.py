"""
    SubVerb: A class to encapsulate a subject and a verb
    and potentially an article an adjective and an adverb.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""
from machinetrans.data.wordtype import WordType

class SubVerb:
    """ Creates a grammatical structure for an English
        sentence of the form:
        [article] [adjective] subject [adverb] verb.
    """

    art = None
    sub = None
    verb = None
    adj = None
    adv = None
    capit = True
    output = ""
    conn = None
    db = None
    sqlcommand = "SELECT DISTINCT conjugation FROM verbs WHERE name=\'{}\' AND tense=\'{}\' AND person=\'{}\';\n"
    currcommand = ""
    types = WordType()

    def __init__(self, conn, art, sub, verb, adj=None, adv=None, capit=True):
        """ Initialize the class global variables.
        """
        self.art = art
        self.sub = sub
        self.verb = verb
        self.adj = adj
        self.adv = adv
        self.conn = conn
        self.db = conn.cursor()
        self.capit = capit
        
    def compose(self):
        """ Compose the construct with the data provided.
        """
        verbstr = "verb error"
        pronstr = "pronoun error"
        tense = "\'simple present\'"
        wtype = ""
        self.output = ""
        tense = self.verb[1]
        article = "Error Value"
        if self.sub[0] == "noun": 
            if "plural" == self.sub[3]:
                article = "the"
            else:
                article = "a"
        if self.sub[0] == "pronoun":
            if "plural" == self.sub[2]:
                article = "the"
            else:
                article = "a"
        # Check for a pronoun (has length 4).
        if self.sub[0] == "pronoun":
            pronstr = self.sub[1]
            index = self.types.pronoun.index(pronstr)
            if index > 2 and index < 4:
                index = 2
            if index > 3:
                index -= 1
            person = self.types.person[index]
            if "plural" in person or "second" in person:
                person = "plural third"
            else:
                person = "third"
            wtype = "pronoun"
            self.currcommand = self.sqlcommand.format(self.verb[0], tense, person)
        elif self.sub[0] == "pronoun":
            pronstr = self.sub[1]
            index = self.types.pronouns.index(pronstr)
            if index > 2 and index < 4:
                index = 2
            if index > 3:
                index -= 1
            person = self.types.person[index]
            self.currcommand = self.sqlcommand.format(self.verb[0], tense, person)
        elif self.sub[0] == "noun" and self.sub[2] == "proper":
            wtype = "pronoun"
            person = "third"
            pronstr = self.sub[1]
            self.currcommand = self.sqlcommand.format(self.verb[0], tense, person)
        else:
            wtype = "noun"
            person = "third"
            pronstr = self.sub[1]
            collective = self.sub[2] == "collective"
            self.currcommand = self.sqlcommand.format(self.verb[0], tense, person)
        # Get the necessary verb data.
        self.db.execute(self.currcommand)
        dataobj = self.db.fetchall()
        for x in dataobj:
            for y in x:
                verbstr = y
        # Add an "n" to the indefinite article "a" if necessary.
        if self.adj:
            if article == "a" and self.adj[0][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                article += "n"
        else:
            if article == "a" and pronstr[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                article += "n"
        # Generate the construct.
        if self.capit:
            if wtype == "noun" and not collective and "a" in article:
                if self.adj:
                    self.output = article.capitalize() + " " + self.adj[0] + " " + pronstr
                else:
                    self.output = article.capitalize() + " " + pronstr
            elif wtype == "noun" and not "a" in article:
                if self.adj:
                    self.output = article.capitalize() + " " + self.adj[0] + " " + pronstr
                else:
                    self.output = article.capitalize() + " " + pronstr
            else:
                if self.adj:
                    self.output = self.adj[0].capitalize() + " " + pronstr
                else:
                    self.output = pronstr.capitalize()
            if self.adv:
                index = verbstr.find(' ')
                if index > 0:
                    self.output += " " + verbstr[:index] + " " + self.adv + verbstr[index:]
                else:
                    self.output += " " + self.adv + " " + verbstr
            else:
                self.output += " " + verbstr
        else:
            if wtype == "noun" and not collective and "a" in article:
                if self.adj:
                    self.output = article + " " + self.adj[0] + " " + pronstr
                else:
                    self.output = article + " " + pronstr
            if wtype == "noun" and not "a" in article:
                if self.adj:
                    self.output = article + " " + self.adj[0] + " " + pronstr
                else:
                    self.output = article + " " + pronstr
            else:
                if self.adj:
                    self.output = self.adj[0] + " " + pronstr
                else:
                    self.output = pronstr
            if self.adv:
                self.output += " " + self.adv + " " + verbstr
            else:
                self.output += " " + verbstr
        return (self.output)

    

        
