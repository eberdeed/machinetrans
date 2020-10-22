"""
    ArtObj: A class to encapsulate the object part of an English sentence,
    with an optional article and adjective.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""

class ArtObj:
    """ Creates a grammatical structure for an English
        sentence of the form:
        [preposition] [article] [adjective] object.
    """   
    art = list()
    adj = list()
    obj = list()
    prep = list()
    output = ""
    
    def __init__(self, art, obj, adj = None, prep = None):
        """ Initialize the class global variables.
        """
        self.art = art
        self.obj = obj
        self.adj = adj
        self.prep = prep
            
    def compose(self):
        """ Compose the construct.
        """
        self.output = ""
        article = self.art
        object1 = self.obj[1]
        # Check to see if an "n" is necessary for the indefinite article "a."
        if self.adj:
            if article == "a" and self.adj[0][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                article += "n"
        else:
            if article == "a" and object1[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                article += "n"
        # Compose the construct.
        if self.prep:
            self.output = self.prep + " "
        # a pronoun is present.
        if self.obj[0] == "pronoun":
            if self.prep:
                self.output += article + " "
            if self.adj:
                self.output += self.adj[0] + " "
        elif self.obj[0] == "noun" and self.obj[2] == "proper":
            if self.prep:
                self.output += article + " "
            if self.adj:
                self.output += self.adj[0] + " "
        elif self.obj[0] == "noun" and self.obj[2] != "collective" and "a" in article:
            self.output += article + " "
            if self.adj:
                self.output += self.adj[0] + " "
        elif self.obj[0] == "noun" and not "a" in article:
            self.output += article + " "
            if self.adj:
                self.output += self.adj[0] + " "
        self.output += object1.strip()
        return(self.output)
        