"""
    Compare: A class to encapsulate a subject and a comparative verb.
    and optionally with an article, an adjective and an adverb.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""
from machinetrans.data.wordtype import WordType

class Compare:
    """ Creates a grammatical structure for an English
        sentence of the form:
        [article] subject [comparative adjective].
    """

    art = None
    sub = None
    verb = ""
    comp = None
    capit = True
    output = ""
    conn = None
    db = None
    tobe = dict({"first": "am", "second": "are", "third": "is", "plural first": "are", "plural second": "are", "plural third": "are"})

    def __init__(self, conn, art, sub, comp, capit=True):
        """ Initialize the class global variables.
        """
        self.art = art
        self.sub = sub
        self.comp = comp
        self.conn = conn
        self.capit = capit
        
    def compose(self):
        """ Compose the construct with the data provided.
        """
        verbstr = "verb error"
        pronstr = "pronoun error"
        self.output = ""
        tense = "simple present"
        # Check for a pronoun.
        # Get the necessary verb data.
        if self.sub[0] == "pronoun":
            person = self.sub[2]
            pronstr = self.sub[1]
            self.verb = self.tobe[person]
            collective = False
        elif self.sub[0] == "noun" and self.sub[2] == "proper":
            wtype = "pronoun"
            person = "third"
            self.verb = self.tobe[person]
            pronstr = self.sub[1]
            collective = False
        else:
            wtype = "noun"
            person = "third"
            pronstr = self.sub[1]
            collective = self.sub[2] == "collective"
            self.verb = self.tobe[person]
        article = self.art
        verbstr = self.verb
        if article == "a" and pronstr[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            article += "n"
        # Generate the construct.
        if self.capit:
            if person == "third" and not collective and "a" in article:
                self.output = article.capitalize() + " " + pronstr
            elif person == "third" and not "a" in article:
                self.output = article.capitalize() + " " + pronstr
            else:
                self.output = pronstr.capitalize()
            self.output += " " + verbstr + " " + self.comp
        else:
            if person == "third" and not collective and "a" in article:
                self.output = article + " " + pronstr
            elif person == "third" and not "a" in article:
                self.output = article + " " + pronstr
            else:
                self.output = pronstr
            self.output += " " + verbstr + " " + self.comp
        return(self.output)

    

        
