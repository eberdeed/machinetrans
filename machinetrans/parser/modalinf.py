"""
    Currently not being used.
    ModalInf: A class to encapsulate a modal verb + an infinitive
    and potentially an article an adjective and an adverb.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""

class ModalInf:
    """ Currently not being used.
        Creates a grammatical structure for an English
        sentence of the form:
        [article] [adjective] subject modal verb [adverb] verb.
    """

    art = None
    sub = None
    modal = None
    verb = None
    adj = None
    adv = None
    output = ""
    conn = None
    db = None
    sqlcommand = "SELECT conjugation FROM verbs WHERE name=\'{}\' AND variety=\'modal\' AND tense=\'{}\' AND person=\'{}\';\n"
    currcommand = ""

    def __init__(self, conn, art, sub, modal, verb, adj=None, adv=None):
        """ Initialize the class global variables.
        """
        self.art = art
        self.sub = sub
        self.modal = modal
        self.verb = verb
        self.adj = adj
        self.adv = adv
        self.conn = conn
        self.db = self.conn.cursor()
        
    def compose(self):
        """ Compose the construct with the data provided.
        """
        verbstr = "verb error"
        pronstr = "pronoun error"
        self.output = ""
        tense = self.modal[2]
        # Check for a pronoun (has length 4).
        if len(self.sub) >= 4:
            wtype = "pronoun"
            person = self.sub[1]
            pronstr = self.sub[0]
            self.currcommand = self.sqlcommand.format(self.modal[0], tense, person)
        else:
            wtype = "noun"
            person = "third"
            pronstr = self.sub[0]
            self.currcommand = self.sqlcommand.format(self.modal[0], tense, person)
        # Get the necessary verb data.
        self.db.execute(self.currcommand)
        datalist = self.db.fetchall()
        for x in datalist:
            for y in x:
                verbstr = y
        # Add an "n" to the indefinite article "a" if necessary.
        article = self.art
        if self.adj:
            if article == "a" and self.adj[0][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                article += "n"
            else:
                if article == "a" and pronstr[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    article += "n"
        # Compose the construct.
        if wtype == "noun":
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
            self.output += " " + self.adv[0] + " " + verbstr + " " + self.verb[0]
        else:
            self.output += " " + verbstr + " " + self.verb[0]
        return(self.output)

        
