"""
    Interrog: A class to encapsulate an interrogative + verb construct.
    and potentially an adverb.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06/25/2016 San Diego, California USA
"""

class Interrog:
    """ Creates a grammatical structure for an English
        sentence of the form:
        interrog [adverb] verb.
    """
    interrog = None
    verb = None
    adv = None
    output = ""
    conn = None
    db = None
    sqlcommand = "SELECT conjugation FROM verbs WHERE name=\'{}\' AND tense=\'{}\' AND person=\'third\';\n"
    currcommand = ""

    def __init__(self, conn, interrog, verb, adv=None):
        """ Initialize the data.
        """
        self.conn = conn
        self.db = conn.cursor()
        self.interrog =interrog
        self.verb = verb
        self.adv = adv

    def compose(self):
        """ Compose the construct.
        """
        verbstr = "verb error"
        pronstr = "pronoun error"
        self.output = ""
        tense = self.verb[2]
        # Get the verb.
        person = "third"
        self.currcommand = self.sqlcommand.format(self.verb[0], tense)
        # Get the necessary verb data.
        self.db.execute(self.currcommand)
        dataobj = self.db.fetchall()
        for x in dataobj:
            for y in x:
                verbstr = y        

        # Generate the construct.
        index = verbstr.find(" ")
        if index > 0:
            if self.adv:
                self.output += self.interrog.capitalize() + " " + verbstr[:index] + " " + self.adv + verbstr[index:]
            else:
                self.output += self.interrog.capitalize() + " " + verbstr
        else:
            if self.adv:
                self.output += self.interrog.capitalize() + " " + self.adv + " " + verbstr
            else:
                self.output += self.interrog.capitalize() + " " + verbstr
        return(self.output)

        
