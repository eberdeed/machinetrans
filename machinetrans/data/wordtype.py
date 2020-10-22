"""
    WordType:  A class to encapsulate English word types.
    I am indebted to the website www.englishclub.com 
    for the categorization lists.
    Edward C. Eberle <eberdeed@eberdeed.net>
    06-24-2016 San Diego California
"""
class WordType:
    """ A class to encapsulate English word types.
        This varies a bit from the Russian grammar.
    """
    
    # First Level Categorizations
    
    wordclass = ("noun", "adjective", "verb", "past tense verb",\
        "adverb", "interjection", "pronoun", \
        "preposition", "symbol", "conjunction", \
        "interrogative", "participle", "invariant")
            
    # Class Types Second Level
    
    nouns = ("abstract", "proper", "concrete", \
        "collective", "compound")
    verbs = ("motion", "other")
    adjectives = ("descriptive", "comparative", "superlative", "short adjective")
    adverbs = ("state", "manner", "place", "time", "degree", "other")
    pronouns = ("personal", "demonstrative", "possessive", \
        "interrogative", "reflexive", "reciprocal", "indefinite", \
        "relative")
    participles = ("present active", "present passive", \
        "past active", "past passive", "verbal adverb", "short past passive")
    prepositions = ("place", "time", "other")
    conjunctions = ("coordinating", "subordinating")
    symbols = ("glyph", "number", "other")
    interrogs = ("person", "place", "time", "method", "reason", "ownership", "quantity")
    invariant = ("foreign", "subjunctive", "acronym", "other")

    # Level Three Categorizations

    # Verb Tense.
    tense = ("imperative", "simple present", "simple past", \
        "perfect simple past", "perfect continuous past", \
        "continuous past", "continuous present", "perfect simple present", \
        "perfect continous present", "simple future", "continuous future", \
        "perfect simple future", "perfect continuous future")   
    
    # Subject / Object -- Prounoun
    status = ("subject", "object")

    # Location / Thing -- Noun
    nountype = ("location", "thing")

    # Person -- Pronoun Verb
    person = ("first", "second", "third", "plural first", "plural second", "plural third")
    pronoun = list(["I", "you", "he", "she", "it", "we", "they"])
    # Declension
    declension = ("none", "nominative", "accusative", "genitive", "dative", "instrumental", "prepositional")
    
    # Object case.
    objcase = ('nominative', 'accusative', 'genitive', 'dative', 'instrumental', 'prepositional', 'none')
     
    # Gender
    gender = ("masculine", "feminine", "nueter", "plural")
    
    # Life
    animate = ("animate", "inanimate")
    
    # Repetition
    imperfective = ("perfective", "imperfective")
    
    nounkeys = ("name", "runame", "variety", "gender", "type", "declension", "wordcase", "animate")
    interjectionkeys = ("name", "runame")
    verbkeys = ("name", "runame", "variety", "tense", "person", "objcase", "conjugationru", \
        "conjugation", "imperfective")
    pastverbkeys = ("name", "runame", "tense", "gender", "conjugation", "conjugationru", \
        "objcase", "imperfective")
    adjectivekeys = ("name", "runame", "variety", "gender", "declension", "wordcase", "animate")
    adverbkeys = ("name", "runame", "variety")
    invariantkeys = ("name", "runame", "wordcase", "variety")
    pronounkeys = ("name", "runame", "variety", "gender","declension", "wordcase", "animate")
    participlekeys = ("name", "runame", "variety", "gender", "objcase", "animate", "declension", \
        "enval", "wordcase")
    prepositionkeys = ("name", "runame", "variety", "objcase")
    conjunctionkeys = ("name", "runame", "variety")
    symbolkeys = ("name", "runame", "variety")
    interrogativekeys = ("name", "runame", "variety")

    wordkeys = {"noun":nounkeys, "interjection":interjectionkeys, "verb":verbkeys, "pastverb":pastverbkeys, \
        "adjective":adjectivekeys, "adverb":adverbkeys, "invariant":invariantkeys, "pronoun":pronounkeys, \
        "participle":participlekeys, "preposition":prepositionkeys, "conjunction":conjunctionkeys, \
        "symbol":symbolkeys, "interrogative":interrogativekeys}