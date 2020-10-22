#!/usr/bin/python3
"""
    WordMorph:  A class encapsulate Russian word morphology.
    Edward C. Eberle <eberdeed@eberdeed.net>
    July 30, 2016 San Diego California
"""

import sys, os, re

class WordMorph:
    """ A class to encapsulate Russian word morphology.
        Here are found the declensions and conjugations of Russian.
        We use tuples because they are immutable.
    """
    # pronouns
    reflposs = list()
    variety = list()
    reflexivesam = list()
    possessive1a = list()
    possessive2a = list()
    possessive2b = list()
    possessive3a = list()
    interrog = list()
    demonstrative1 = list()
    demonstrative2 = list()
    inclusive = list()
    pronouns = dict()
    singlekeys = ()
    groupkeys = ()
    
    datalist = list()
    mascsing = list()
    nuetsing = list()
    femsing = list()
    mascplur = list()
    nuetplur = list()
    femplur = list()
    verblist = list()
    pluralonly = list()
    conjugations = list()
    adjectiveshard = list()
    adjectivessoft = list()
    adjectivesoy = list()
    adjectivesmyagkiy = list()
    declension = list()

    def __init__(self):
        """ I did the pronouns as one big lump.  The dictionary below allows for 
            a single input of all the pronouns and their declensions.
        """
        for x in self.pronouns:
            tmplist = list(self.pronouns[x]) + list([x])
            self.pronouns[x] = tmplist

        # Pronouns
        
        self.reflposs.append(self.reflpossmanim)
        self.reflposs.append(self.reflpossminan)
        self.reflposs.append(self.reflpossf)
        self.reflposs.append(self.reflpossn)
        self.reflposs.append(self.reflposspanim)
        self.reflposs.append(self.reflposspinan)
        self.reflposs.append("possessive")
        
        self.variety.append(self.varietymanim)
        self.variety.append(self.varietyminan)
        self.variety.append(self.varietyf)
        self.variety.append(self.varietyn)
        self.variety.append(self.varietypanim)
        self.variety.append(self.varietypinan)
        self.variety.append("variety")
        
        self.reflexivesam.append(self.reflexivesamadjmanim)
        self.reflexivesam.append(self.reflexivesamadjminan)
        self.reflexivesam.append(self.reflexivesamadjf)
        self.reflexivesam.append(self.reflexivesamadjn)
        self.reflexivesam.append(self.reflexivesamadjpanim)
        self.reflexivesam.append(self.reflexivesamadjpinan)
        self.reflexivesam.append("reflexive")
        
        self.possessive1a.append(self.possessive1amanim)
        self.possessive1a.append(self.possessive1aminan)
        self.possessive1a.append(self.possessive1af)
        self.possessive1a.append(self.possessive1an)
        self.possessive1a.append(self.possessive1apanim)
        self.possessive1a.append(self.possessive1apinan)
        self.possessive1a.append("possessive")

        self.possessive2a.append(self.possessive2amanim)
        self.possessive2a.append(self.possessive2aminan)
        self.possessive2a.append(self.possessive2af)
        self.possessive2a.append(self.possessive2an)
        self.possessive2a.append(self.possessive2apanim)
        self.possessive2a.append(self.possessive2apinan)
        self.possessive2a.append("possessive")

        self.possessive2b.append(self.possessive2bmanim)
        self.possessive2b.append(self.possessive2bminan)
        self.possessive2b.append(self.possessive2bf)
        self.possessive2b.append(self.possessive2bn)
        self.possessive2b.append(self.possessive2bpanim)
        self.possessive2b.append(self.possessive2bpinan)
        self.possessive2b.append("possessive")

        self.possessive3a.append(self.possessive3amanim)
        self.possessive3a.append(self.possessive3aminan)
        self.possessive3a.append(self.possessive3af)
        self.possessive3a.append(self.possessive3an)
        self.possessive3a.append(self.possessive3apanim)
        self.possessive3a.append(self.possessive3apinan)
        self.possessive3a.append("possessive")

        self.interrog.append(self.interrogmanim)
        self.interrog.append(self.interrogminan)
        self.interrog.append(self.interrogf)
        self.interrog.append(self.interrogn)
        self.interrog.append(self.interrogpanim)
        self.interrog.append(self.interrogpinan)
        self.interrog.append("interrogative")
        
        self.demonstrative1.append(self.demonstrative1manim)
        self.demonstrative1.append(self.demonstrative1minan)
        self.demonstrative1.append(self.demonstrative1f)
        self.demonstrative1.append(self.demonstrative1n)
        self.demonstrative1.append(self.demonstrative1panim)
        self.demonstrative1.append(self.demonstrative1pinan)
        self.demonstrative1.append("demonstrative")

        self.demonstrative2.append(self.demonstrative2manim)
        self.demonstrative2.append(self.demonstrative2minan)
        self.demonstrative2.append(self.demonstrative2f)
        self.demonstrative2.append(self.demonstrative2n)
        self.demonstrative2.append(self.demonstrative2panim)
        self.demonstrative2.append(self.demonstrative2pinan)
        self.demonstrative2.append("demonstrative")

        self.inclusive.append(self.inclusivemanim)
        self.inclusive.append(self.inclusiveminan)
        self.inclusive.append(self.inclusivef)
        self.inclusive.append(self.inclusiven)
        self.inclusive.append(self.inclusivepanim)
        self.inclusive.append(self.inclusivepinan)
        self.inclusive.append("inclusive")
        
        self.pronouns["a"] = self.personal1a
        self.pronouns["b"] = self.personal2a
        self.pronouns["c"] = self.personal3a
        self.pronouns["d"] = self.personal3b
        self.pronouns["e"] = self.personal3c
        self.pronouns["f"] = self.personal1b
        self.pronouns["g"] = self.personal2b
        self.pronouns["h"] = self.personal3c
        self.pronouns["i"] = self.reflexive
        self.pronouns["j"] = self.interrog1
        self.pronouns["k"] = self.interrog2
        self.pronouns["l"] = self.neginterrog1
        self.pronouns["m"] = self.neginterrog2
        
        self.singlekeys = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
        
        self.pronouns["1"] = self.reflposs
        self.pronouns["2"] = self.variety
        self.pronouns["3"] = self.reflexivesam
        self.pronouns["4"] = self.possessive1a
        self.pronouns["5"] = self.possessive2a
        self.pronouns["6"] = self.possessive2b
        self.pronouns["7"] = self.possessive3a
        self.pronouns["8"] = self.interrog
        self.pronouns["9"] = self.demonstrative1
        self.pronouns["10"] = self.demonstrative2
        self.pronouns["11"] = self.inclusive
        
        self.groupkeys = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
        
        # Noun data structure.
        self.mascsing.append(self.mascdeclanimhrd)
        self.mascsing.append(self.mascdeclinanhrd)
        self.mascsing.append(self.mascdeclanimsft)
        self.mascsing.append(self.mascdeclinansft)
        self.mascsing.append(self.mascdeclanimsft1)
        self.mascsing.append(self.mascdeclinansft1)
        self.mascsing.append(self.mascdeclanimsft2)
        self.mascsing.append(self.mascdeclinansft2)
        self.mascsing.append(self.mascdeclinanhrd1)
        self.mascsing.append(self.mascdeclinansft1a)
        self.mascsing.append(self.mascdeclanimsft3)
        self.mascsing.append(self.mascdeclinansft3)
        self.mascsing.append(self.declblank)
        self.mascsing.append(self.adjmascdeclhrdanim) # 13
        self.mascsing.append(self.adjmascdeclhrdinan)
        self.mascsing.append(self.adjmascdeclsftanim)
        self.mascsing.append(self.adjmascdeclsftinan)
        self.mascsing.append(self.adjmascdeclgkxanim)
        self.mascsing.append(self.adjmascdeclgkxinan)
        self.mascsing.append(self.adjmascoanim)
        self.mascsing.append(self.adjmascoinan)
        self.mascsing.append(self.adjmascmyagkiyanim)
        self.mascsing.append(self.adjmascmyagkiyinan)
        
        self.nuetsing.append(self.nuetdeclhrd)
        self.nuetsing.append(self.nuetdeclsft)
        self.nuetsing.append(self.nuetdeclsft1)
        self.nuetsing.append(self.nuetdeclmya)
        self.nuetsing.append(self.declblank)
        self.nuetsing.append(self.adjnuetdeclhrd) # 5
        self.nuetsing.append(self.adjnuetdeclsft)
        self.nuetsing.append(self.adjnuetdeclgkx)
        self.nuetsing.append(self.adjnueto)
        self.nuetsing.append(self.adjnuetmyagkiy)

        self.femsing.append(self.femideclhrd)
        self.femsing.append(self.femideclsft)
        self.femsing.append(self.femideclhrdgkx)
        self.femsing.append(self.femideclsftgkx)
        self.femsing.append(self.femideclsft1)
        self.femsing.append(self.femideclsft2)
        self.femsing.append(self.femideclsftcons)
        self.femsing.append(self.declblank)
        self.femsing.append(self.adjfemideclhrd) # 8
        self.femsing.append(self.adjfemideclsft)
        self.femsing.append(self.adjfemideclgkx)
        self.femsing.append(self.adjfemio)
        self.femsing.append(self.adjfemimyagkiy)

        self.mascplur.append(self.mascdeclanimplur)
        self.mascplur.append(self.mascdeclinanplur)
        self.mascplur.append(self.mascdeclanimplur1)
        self.mascplur.append(self.mascdeclinanplur1)
        self.mascplur.append(self.mascdeclanimplur2)
        self.mascplur.append(self.mascdeclinanplur2)
        self.mascplur.append(self.mascdeclanimplur3)
        self.mascplur.append(self.mascdeclinanplur3)
        self.mascplur.append(self.mascdeclanimplur4)
        self.mascplur.append(self.mascdeclinanplur4)
        self.mascplur.append(self.mascdeclanimplur5)
        self.mascplur.append(self.mascdeclinanplur5)
        self.mascplur.append(self.mascdeclanimplur6)
        self.mascplur.append(self.mascdeclinanplur6)
        self.mascplur.append(self.mascdeclatayataplur)
        self.mascplur.append(self.mascdeclaninyaninplur)
        self.mascplur.append(self.mascdeclnumericplur)
        self.mascplur.append(self.mascdeclhundredplur)
        self.mascplur.append(self.declblank)
        self.mascplur.append(self.adjplurdeclhrdanim) # 17
        self.mascplur.append(self.adjplurdeclhrdinan)
        self.mascplur.append(self.adjplurdeclsftanim)
        self.mascplur.append(self.adjplurdeclsftinan)
        self.mascplur.append(self.adjplurdeclgkxanim)
        self.mascplur.append(self.adjplurdeclgkxinan)
        self.mascplur.append(self.adjpluroanim)
        self.mascplur.append(self.adjpluroinan)
        self.mascplur.append(self.adjplurmyagkiyanim)
        self.mascplur.append(self.adjplurmyagkiyinan)
                             
        self.nuetplur.append(self.nuetdeclhrdplur)
        self.nuetplur.append(self.nuetdeclsftplur)
        self.nuetplur.append(self.nuetdeclsftplur1)
        self.nuetplur.append(self.nuetdeclmyaplur)
        self.nuetplur.append(self.declblank)
        self.nuetplur.append(self.adjplurdeclhrdinan) # 5
        self.nuetplur.append(self.adjplurdeclsftinan)
        self.nuetplur.append(self.adjplurdeclgkxinan)
        self.nuetplur.append(self.adjpluroinan)
        self.nuetplur.append(self.adjplurmyagkiyinan)
        
        self.femplur.append(self.femideclanimhrdplur)
        self.femplur.append(self.femideclinanhrdplur)
        self.femplur.append(self.femideclanimhrdplur1)
        self.femplur.append(self.femideclinanhrdplur1)
        self.femplur.append(self.femideclanimsftplur)
        self.femplur.append(self.femideclinansftplur)
        self.femplur.append(self.femideclanimsftplur1)
        self.femplur.append(self.femideclinansftplur1)
        self.femplur.append(self.femideclanimsftplur2)
        self.femplur.append(self.femideclinansftplur2)
        self.femplur.append(self.femideclanimsftplur3)
        self.femplur.append(self.femideclinansftplur3)
        self.femplur.append(self.femideclnumericplur)
        self.femplur.append(self.declblank)
        self.femplur.append(self.adjplurdeclhrdanim) # 14
        self.femplur.append(self.adjplurdeclhrdinan)
        self.femplur.append(self.adjplurdeclsftanim)
        self.femplur.append(self.adjplurdeclsftinan)
        self.femplur.append(self.adjplurdeclgkxanim)
        self.femplur.append(self.adjplurdeclgkxinan)
        self.femplur.append(self.adjpluroanim)
        self.femplur.append(self.adjpluroinan)
        self.femplur.append(self.adjplurmyagkiyanim)
        self.femplur.append(self.adjplurmyagkiyinan)
        
        self.pluralonly.append(self.plural)
        
        self.datalist = (self.mascsing, self.nuetsing, self.femsing, self.mascplur, self.nuetplur, self.femplur, self.pluralonly)

        comma = ", "

        self.conjugations.append(self.vrbprstat)
        self.conjugations.append(self.vrbprstyat)
        self.conjugations.append(self.vrbprstat1)
        self.conjugations.append(self.vrbprstat2)
        self.conjugations.append(self.vrbprstat3)
        self.conjugations.append(self.vrbprstgat)
        self.conjugations.append(self.vrbprstyt1)
        self.conjugations.append(self.vrbprstyt2)
        self.conjugations.append(self.vrbprstyt3)
        self.conjugations.append(self.vrbprstet)
        self.conjugations.append(self.vrbprsty)
        self.conjugations.append(self.vrbprststy)
        self.conjugations.append(self.vrbprstzty)
        self.conjugations.append(self.vrbprstt)
        self.conjugations.append(self.vrbprstt1)
        self.conjugations.append(self.vrbprstt2)
        self.conjugations.append(self.vrbprstovat)
        self.conjugations.append(self.vrbprstit)
 
        # Define adjectives
        
        self.adjectiveshard = list([self.adjmascdeclhrdanim, self.adjmascdeclhrdinan, self.adjfemideclhrd, self.adjnuetdeclhrd,
        self.adjplurdeclhrdanim, self.adjplurdeclhrdinan])
        self.adjectivesgkxsoft = list([self.adjmascdeclgkxanim, self.adjmascdeclgkxinan, self.adjfemideclgkx, self.adjnuetdeclgkx,
        self.adjplurdeclgkxanim, self.adjplurdeclgkxinan])
        self.adjectivessoft = list([self.adjmascdeclsftanim, self.adjmascdeclsftinan, self.adjfemideclsft, self.adjnuetdeclsft,
        self.adjplurdeclsftanim, self.adjplurdeclsftinan])
        self.adjectivesoy = list([self.adjmascoanim, self.adjmascoinan, self.adjfemio, self.adjnueto,
        self.adjpluroanim, self.adjpluroinan])
        self.adjectivesmyagkiy = list([self.adjmascmyagkiyanim, self.adjmascmyagkiyinan, self.adjfemimyagkiy, self.adjnuetmyagkiy,
        self.adjplurmyagkiyanim, self.adjplurmyagkiyinan])
        self.declension.append(self.adjectiveshard)
        self.declension.append(self.adjectivesgkxsoft)
        self.declension.append(self.adjectivessoft)
        self.declension.append(self.adjectivesoy)
        self.declension.append(self.adjectivesmyagkiy)
        return

    # Russian alphabet lowercase and upper case.
    rualphlower = ("а", "б", "в", "г", "д", "е", "ё", "ж", \
        "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", \
        "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")
    rualphupper = ("А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", \
        "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", \
        "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я")
    ruall = rualphlower + rualphupper
    # English latin alphabet.
    enall = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", \
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
        "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", \
        "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", \
        "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    # Letter Types.
    # Hard and soft Russian consonants.
    # Hard consonants.
    ruconshrd = ("ц", "ш", "ж", "к", "г", "х", "т", "д", \
        "с", "з", "п", "б", "ф", "в", "л", "р", "м", "н")
    # Soft consonants.
    ruconssft = ("ть", "дь", "сь", "зь", "пь", "бь", \
        "фь", "вь", "ль", "рь", "мь", "нь", "ч", "щ", "й")
    # Soft only consonants.
    ruconssoftonly = ("ч", "щ", "й")
    # Sybillants are a sound group in Russian.
    sybillants = ("ч", "щ", "ш")
    # Russian vowels.
    vowels = ("а", "е", "ё", "о", "у", "э", "ю", "я")
    # A complete list of Russian consonants.
    consonants = ("б", "в", "г", "д", "ж", "з", "и", "й", \
        "к", "л", "м", "н", "р", "с", "т", "ф", "х", "ц", \
        "ч", "ш", "щ", "ъ")
    """
        Word Identifiers by position in the variable name:
        0 - 3 gender
        4 - 7 wordtype (noun, adjective, verb, etc.)
        8 - 11 number (singular/plural)
    """
    feminounsing = ("а", "я", "жь", "чь", "шь", "щь", "ия")
    nuetnounsing = ("о", "е", "ё", "мя")
    mascnounsing = ruconshrd + ("ч", "щ", "й", "ь")
    mascnounplur = ("ы", "и")
    gkx = ("г", "к", "х")
    reqi = ("г", "к", "х", "ж", "ч", "ш", "щ")
    mascnounplur1 = ("а", "я")
    mascnounplur2 = ("ане", "яне")
    mascnounplur3 = ("ата", "ята")
    mascnounplur4 = ("ья")
    nuetnounplur = ("а", "я", "емена", "емёна")
    nuetnounplur1 = ("еса")
    """
        Declension by position in the list:
        1) Nominative
        2) Accusative
        3) Genitive
        4) Dative
        5) Instrumental
        6) Prepositional
        
        Declension Names by position in the variable name:
        0 - 3  gender
        4 - 7  declension
        [8 - 11 animate/inanimate]
        12 - 14 hard/soft
        [15     Declension Number (1, 2, 3)]
        [16     Sub-Category (a, b, c)]
    """
    declblank = ("Blank", "", "", "", "", "", "")
    
    mascdeclanimhrd = ("Animate Hard", "", "а", "а", "у", "ом", "е")
    mascdeclinanhrd = ("Inanimate Hard", "", "", "а", "у", "ом", "е")
    mascdeclanimsft = ("Animate Soft", "ь", "я", "я", "ю", "ём", "е")
    mascdeclinansft = ("Inanimate Soft", "ь", "ь", "я", "ю", "ём", "е")
    mascdeclanimsft1 = ("Animate Soft 1", "", "я", "я", "у", "ем", "е")
    mascdeclinansft1 = ("Inanimate Soft 1", "", "", "я", "у", "ем", "е")
    mascdeclanimsft2 = ("Animate Soft Ends in й", "й", "я", "я", "ю", "ем", "е")
    mascdeclinansft2 = ("Inanimate Soft Ends in й", "й", "й", "я", "ю", "ем", "е")
    mascdeclinanhrd1 = ("y in Prep.", "", "", "а", "у", "ом", "у") # y in prepositional.
    mascdeclinansft1a = ("ю in Prep.", "й", "й", "я", "ю", "ем", "ю") # ю in prepositional.
    mascdeclanimsft3 = ("Animate Soft","ий", "ия", "ия", "ию", "ием", "ии")
    mascdeclinansft3 = ("Inanimate Soft", "ий", "ий", "ия", "ию", "ием", "ии")
    # Pivotal Russian letter combinations for determining declension type.
    myagkiyznak = "ь"
    tmyagkiyznak = "ть"
    ykratkoye = "й"
    yykratkoye = "ий"
    
    nuetdeclhrd = ("Hard", "о", "о", "а", "у", "ом", "е")
    nuetdeclsft = ("Soft", "е", "е", "я", "ю", "ем", "е")
    nuetdeclsft1 = ("Soft", "ие", "ие", "ия", "ию", "ием", "ии")
    nuetdeclmya = ("Ends in мя", "мя", "мя", "мени", "мени", "менем", "мени")
    
    femideclhrd = ("Hard", "а", "у", "ы", "е", "ой", "е")
    femideclsft = ("Soft", "я", "ю", "ы", "е", "ой", "е")
    femideclhrdgkx = ("Hard гкх", "а", "у", "и", "е", "ой", "е")
    femideclsftgkx = ("Soft гкх", "я", "ю", "и", "е", "ой", "е")
    femideclsft1 = ("Soft", "ия", "ию", "ии", "ии", "ией", "ии")
    femideclsft2 = ("Soft", "ь", "ь", "и", "и", "ью", "и")
    femideclsftcons = ("Soft Consonant Ending", "я", "ю", "и", "е", "ей", "е")
    
    # Only masculine and plural keep the animate-inanimate distinction.
    mascdeclanimplur = ("Hard Animate", "ы", "ов", "ов", "ам", "ами", "ах")
    mascdeclinanplur = ("Hard Inanimate", "ы", "ы", "ов", "ам", "ами", "ах")
    mascdeclanimplur1 = ("Soft Animate", "ы", "ев", "ев", "ам", "ами", "ах")
    mascdeclinanplur1 = ("Soft Inanimate", "ы", "ы", "ев", "ам", "ами", "ах")
    mascdeclanimplur2 = ("Soft Animate 1", "и", "ев", "ев", "ям", "ями", "ях")
    mascdeclinanplur2 = ("Soft Inanimate 1", "и", "и", "ев", "ям", "ями", "ях")
    mascdeclanimplur3 = ("Soft Animate 2", "и", "ов", "ов", "ам", "ами", "ах")
    mascdeclinanplur3 = ("Soft Inanimate 2", "и", "и", "ов", "ам", "ами", "ах")
    mascdeclanimplur4 = ("Animate Ends in гкхщш", "и", "ей", "ей", "ам", "ами", "ах")
    mascdeclinanplur4 = ("Inanimate Ends in гкхщш", "и", "и", "ей", "ам", "ами", "ах")
    mascdeclanimplur5 = ("Animate Singular Ends in ь", "и", "ей", "ей", "ям", "ями", "ях")
    mascdeclinanplur5 = ("Inanimate Singular Ends in ь", "и", "и", "ей", "ям", "ями", "ях")
    mascdeclanimplur6 = ("Soft Animate ья", "ья", "ьев", "ьев", "ьям", "ьями", "ьях")
    mascdeclinanplur6 = ("Soft Inanimate ья", "ья", "ья", "ьев", "ьям", "ьями", "ьях")
    mascdeclatayataplur = ("Plural Ends in ата ята", "та", "т", "т", "там", "тами", "тах")
    mascdeclaninyaninplur = ("Singular Ends in анин янин", "не", "н", "н", "нам", "нами", "нах")
    mascdeclnumericplur = ("Numeric", "", "", "а", "а", "а", "а")
    mascdeclhundredplur = ("Hundreds", "", "", "сот", "стам", "стами", "стах")
    
    nuetdeclhrdplur = ("Hard", "а", "а", "", "ам", "ами", "ах") 
    nuetdeclsftplur = ("Soft", "я", "я", "ей", "ям", "ями", "ях") 
    nuetdeclsftplur1 = ("Soft", "ия", "ия", "ий", "иям", "иями", "иях")
    nuetdeclmyaplur = ("Ends in мя", "мена", "мена", "мён", "менам", "менами", "менах")
    
    femideclanimhrdplur = ("Hard Animate", "ы", "", "", "ам", "ами", "ах")
    femideclinanhrdplur = ("Hard Inanimate", "ы", "ы", "", "ам", "ами", "ах")
    femideclanimhrdplur1 = ("Hard Animate гкх", "и", "", "", "ам", "ами", "ах")
    femideclinanhrdplur1 = ("Hard Inanimate гкх", "и", "и", "", "ам", "ами", "ах")
    femideclanimsftplur = ("Soft Animate", "и", "", "", "ям", "ями", "ях")
    femideclinansftplur = ("Soft Inanimate", "и", "и", "", "ям", "ями", "ях")
    femideclanimsftplur1 = ("Hard Animate Singular Ends in ь", "и", "ей", "ей", "ам", "ами", "ах")
    femideclinansftplur1 = ("Hard Inanimate Singular Ends in ь", "и", "и", "ей", "ам", "ами", "ах")
    femideclanimsftplur2 = ("Soft Animate Singular Ends in ь", "и", "ей", "ей", "ям", "ями", "ях")
    femideclinansftplur2 = ("Soft Inanimate Singular Ends in ь", "и", "и", "ей", "ям", "ями", "ях")
    femideclanimsftplur3 = ("Soft Animate", "ии", "ий", "ий", "иям", "иями", "иях")
    femideclinansftplur3 = ("Soft Inanimate", "ии", "ии", "ий", "иям", "иями", "иях")
    femideclnumericplur = ("Numeric", "", "", "и", "и", "ью", "и")
    
    plural = ("Plural Only", "", "", "", "", "", "")
    
    child = ("Archaic Usage Singular", "дитя", "дитя", "дитяти", "дитяти", "дитятей", "дитяти")
    matdoch = ("мать дочь Singular", "ь", "ь", "ери", "ери", "ерью", "ери")
    muzh = ("муж Singular", "", "а", "а", "у", "ем", "е")
    childplur = ("Current Usage Plural", "дети", "детей", "детей", "детям", "детьми", "детях")
    matdochplur = ("мать дочь Plural", "ери", "ерей", "ерей", "ерям", "ерями", "ерях")
    muzhplur = ("муж Plural", "ья", "ей", "ей", "ьям", "ьями", "ьях")
    
    adjmascdeclhrdanim = ("Masc Anim", "ый", "ого", "ого", "ому", "ым", "ом")
    adjmascdeclhrdinan = ("Masc Inan", "ый", "ый", "ого", "ому", "ым", "ом")
    adjnuetdeclhrd = ("Nueter", "ое", "ое", "ого", "ому", "ым", "ом")
    adjfemideclhrd = ("Feminine", "ая", "ую", "ой", "ой", "ой", "ой")
    adjplurdeclhrdanim = ("Plur Anim", "ые", "ых", "ых", "ым", "ыми", "ых")
    adjplurdeclhrdinan = ("Plur Inan", "ые", "ые", "ых", "ым", "ыми", "ых")
    
    adjmascdeclgkxanim = ("Masc Anim ГКХ", "ий", "ого", "ого", "ому", "им", "ом")
    adjmascdeclgkxinan = ("Masc Inan ГКХ", "ий", "ий", "ого", "ому", "им", "ом")
    adjnuetdeclgkx = ("Nueter ГКХ", "ое", "ое", "ого", "ому", "им", "ом")
    adjfemideclgkx = ("Feminine ГКХ", "ая", "ую", "ой", "ой", "ой", "ой")
    adjplurdeclgkxanim = ("Plur Anim ГКХ", "ие", "их", "их", "им", "ими", "их")
    adjplurdeclgkxinan = ("Plur Inan ГКХ", "ие", "ие", "их", "им", "ими", "их")
    
    adjmascdeclsftanim = ("Masc Anim", "ий", "его", "его", "ему", "им", "ем")
    adjmascdeclsftinan = ("Masc Inan", "ий", "ий", "его", "ему", "им", "ем")
    adjnuetdeclsft = ("Nueter", "ее", "ее", "его", "ему", "им", "ем")
    adjfemideclsft = ("Feminine", "яя", "юю", "ей", "ей", "ей", "ей")
    adjplurdeclsftanim = ("Plur Anim", "ие", "их", "их", "им", "ими", "их")
    adjplurdeclsftinan = ("Plur Inan", "ие", "ие", "их", "им", "ими", "их")
    
    adjmascoanim = ("Masc Anim", "ой", "ого", "ого", "ому", "ым", "ом")
    adjmascoinan = ("Masc Inan", "ой", "ой", "ого", "ому", "ым", "ом")
    adjnueto = ("Nueter", "ое", "ое", "ого", "ому", "ым", "ом")
    adjfemio = ("Feminine", "ая", "ую", "ой", "ой", "ой", "ой")
    adjpluroanim = ("Plur Anim", "ие", "их", "их", "им", "ими", "их")
    adjpluroinan = ("Plur Inan", "ие", "ие", "их", "им", "ими", "их")
    
    adjmascmyagkiyanim = ("Masc Anim", "ий", "ьего", "ьего", "ьему", "ьим", "ьем")
    adjmascmyagkiyinan = ("Masc Inan", "ий", "ий", "ьего", "ьему", "ьим", "ьем")
    adjnuetmyagkiy = ("Nueter", "ье", "ье", "ьего", "ьему", "ьим", "ьем")
    adjfemimyagkiy = ("Feminine", "ья", "ью", "ьей", "ьей", "ьей", "ьей")
    adjplurmyagkiyanim = ("Plur Anim", "ьи", "ьих", "ьих", "ьим", "ьими", "ьих")
    adjplurmyagkiyinan = ("Plur Inan", "ьи", "ьи", "ьих", "ьим", "ьими", "ьих")
    
    adjshorthard = ("Hard Short Adjective", "", "а", "о", "ы")
    adjshortsoft = ("Soft Short Adjective", "", "а", "о", "и")
    
    """
        Person for verb conjugation -- order in list:
        1) I
        2) You (informal)
        3) He, She, It
        4) We
        5) You (formal, can be plural)
        6) They
        
        Verbs by position in the variable name:
        1 - 3  verb
        4 - 7  tense
        8 -    ending
    """
    vrbprstat = ("Present ать", "аю", "аешь", "ает", "аем", "аете", "ают")
    vrbprstyat = ("Present ять", "яю", "яешь", "яет", "яем", "яете", "яют")
    vrbprstat1 = ("Present ать 1", "аю", "аёшь", "аёт", "аём", "аёте", "ают")
    vrbprstat2 = ("Present ать 2", "у", "ишь", "ит", "им", "ите", "ат")
    vrbprstat3 = ("Present еть", "у", "ишь", "ит", "им", "ите", "ят")
    vrbprstgat = ("Present гать", "гу", "жишь", "жит", "жим", "жите", "гут")
    vrbprstyt1 = ("Present ить 1", "ю", "ишь", "ит", "им", "ите", "ют")
    vrbprstyt2 = ("Present ить 2", "ю", "ишь", "ит", "им", "ите", "ят")
    vrbprstyt3 = ("Present ить 3", "ю", "ешь", "ет", "ем", "ете", "ют")
    vrbprstet = ("Present еть", "у", "ешь", "ет", "ем", "ете", "ут")
    vrbprsty = ("Present и", "у", "ёшь", "ёт", "ём", "ёте", "ут")
    vrbprststy = ("Present сти", "су", "сёшь", "сёт", "сём", "сёте", "сут")
    vrbprstzty = ("Present зти", "зу", "зёшь", "зёт", "зём", "зёте", "зут")
    vrbprstt = ("Present ть", "у", "ишь", "ит", "дим", "дите", "дут")
    vrbprstt1 = ("Present ть 1", "у", "ишь", "ит", "дим", "дите", "дят")
    vrbprstt2 = ("Present ть 2", "м", "шь", "ст", "дим", "дите", "дут")
    vrbprstovat = ("Present овать", "ую", "уешь", "ует", "уем", "уете", "уют")
    vrbprstit = ("Present ыть", "ою", "оешь", "оет", "оем", "оете", "оют")
    
    # Past Tense: Masculine, Feminine, Nueter, Plural
    vrbpast = ("past", "л", "ла", "ло", "ли")
    vrbpast1 = ("past", "", "ла", "ло", "ли")
    # Imperative Informal and Formal
    vrbimp = ("Imperative", "й", "йте")
    pppart = ("Short Past Passive", "", "а", "о", "и")
    vrbadvb = ("Verbal Adverb", "а", "я", "в", "ши", "вши")
    """
        Participles:
        1) Present Active
        2) Present Passive (not all forms)
        3) Past Active
        4) Past Passive
        6) Present Adverbial
        7) Past Adverbial
        The past is included as a participle because it conjugates like one.
        Participles conjugate like adjectives and the adjective endings are used.
    """
    vrbprtcp = ("Participles", "щий", "мый", "вший", "нный", "я", "в")
    # Past Passive Participle Short Form: Masculine, Feminine, Nueter, Plural
    vrbshrtpp = ("Short Past Passive", "н", "на", "но", "ны")        
    # Pronouns
    personal1a = ("I", "я", "меня", "меня", "мне", "мной", "мне", "personal")
    personal2a = ("you", "ты", "тебя", "тебя", "тебе", "тобой", "тебе", "personal")
    personal3a = ("he", "он", "его", "его", "ему", "им", "нём", "personal")
    personal3b = ("she", "она", "её", "её", "ей", "ею", "ней", "personal")
    personal3c = ("it", "оно", "оно", "его", "ему", "им", "нём", "personal")
    personal1b = ("we", "мы", "нас", "нас", "нам", "нами", "нас", "personal")
    personal2b = ("you", "вы", "вас", "вас", "вам", "вами", "вас", "personal")
    personal3c = ("they", "они", "их", "их", "им", "ими", "них", "personal")
    reflexive =  ("oneself", "себя", "себя", "себя", "себе", "собой", "себе", "reflexive")
    interrog1 = ("who", "кто", "кого", "кого", "кому", "кем", "ком", "interrogative")
    interrog2 = ("what", "что", "что", "чего", "чему", "чем", "чём", "interrogative")
    neginterrog1 = ("no one", "никто", "никого", "никого", "никому", "никем", "ни о ком", "interrogative")
    neginterrog2 = ("nothing", "ничто", "ничто", "ничего", "ничему", "ничем", "ни о чём", "interrogative")
    
    reflpossmanim =  ("one's own", "свой", "своего", "своего", "своему", "своим", "своём")
    reflpossminan =  ("one's own", "свой", "свой", "своего", "своему", "своим", "своём")
    reflpossf =  ("one's own", "своя", "свою", "своей", "своей", "своей", "своей")
    reflpossn =  ("one's own", "своё", "своё",  "своего", "своему", "своим", "своём")
    reflposspanim =  ("one's own", "свои", "своих", "своих", "своим", "своими", "своих")
    reflposspinan =  ("one's own", "свои", "свои", "своих", "своим", "своими", "своих")
    
    varietymanim =  ("which", "какой", "какого", "какого", "какому", "каким", "каком")
    varietyminan =  ("which", "какой", "какой", "какого", "какому", "каким", "каком")
    varietyf =  ("which", "какая", "какую", "какой", "какой", "какой", "какой")
    varietyn =  ("which", "какоё", "какоё",  "какого", "какому", "каким", "каком")
    varietypanim =  ("which", "какие", "каких", "каких", "каким", "какими", "каких")
    varietypinan =  ("which", "какие", "какие", "каких", "каким", "какими", "каких")
    
    reflexivesamadjmanim =  ("oneself", "самый", "самого", "самого", "самому", "самим", "самом")
    reflexivesamadjminan =  ("oneself", "самый", "самый", "самого", "самому", "самим", "самом")
    reflexivesamadjf =  ("oneself", "самая", "самую", "самой", "самой", "самой", "самой")
    reflexivesamadjn =  ("oneself", "самое", "самое", "самого", "самому", "самим", "самом")
    reflexivesamadjpanim =  ("oneself", "самые", "самих", "самих", "самим", "самими", "самих")
    reflexivesamadjpinan =  ("oneself", "самые", "самые", "самих", "самим", "самими", "самих")
    
    possessive1amanim = ("mine", "мой", "моего", "моего", "моему", "моим", "моём")
    possessive1aminan = ("mine", "мой", "мой", "моего", "моему", "моим", "моём")
    possessive1af = ("mine", "моя", "мою", "моей", "моей", "моей", "моей")
    possessive1an = ("mine", "моё", "моё", "моего", "моему", "моим", "моём")
    possessive1apanim = ("mine", "мои", "моих", "моих", "моим", "моими", "моих")
    possessive1apinan = ("mine", "мои", "мои", "моих", "моим", "моими", "моих")
    
    possessive2amanim = ("your", "твой", "твоего", "твоего", "твоему", "твоим", "твоем")
    possessive2aminan = ("your", "твой", "твой", "твоего", "твоему", "твоим", "твоем")
    possessive2af = ("your", "твоя", "твою", "твоей", "твоей", "твоей", "твоей")
    possessive2an = ("your", "твоё", "твоё", "твоего", "твоему", "твоим", "твоем")
    possessive2apanim = ("your", "твои", "твоих", "твоих", "твоим", "твоими", "твоих")
    possessive2apinan = ("your", "твои", "твои", "твоих", "твоим", "твоими", "твоих")
    
    possessive2bmanim = ("your", "ваш", "вашего", "вашего", "вашему", "вашим", "вашем")
    possessive2bminan = ("your", "ваш", "ваш", "вашего", "вашему", "вашим", "вашем")
    possessive2bf = ("your", "ваша", "вашу", "вашей", "вашей", "вашей", "вашей")
    possessive2bn = ("your", "ваше", "ваше", "вашего", "вашему", "вашим", "вашем")
    possessive2bpanim = ("your", "ваши", "ваших", "ваших", "вашим", "вашими", "ваших")
    possessive2bpinan = ("your", "ваши", "ваши", "ваших", "вашим", "вашими", "ваших")
    
    possessive3amanim = ("our", "наш", "нашего", "нашего", "нашему", "нашим", "нашем")
    possessive3aminan = ("our", "наш", "наш", "нашего", "нашему", "нашим", "нашем")
    possessive3af = ("our", "наша", "нашу", "нашей", "нашей", "нашей", "нашей")
    possessive3an = ("our", "наше", "наше", "нашего", "нашему", "нашим", "нашем")
    possessive3apanim = ("our", "наши", "наших", "наших", "нашим", "нашими", "наших")
    possessive3apinan = ("our", "наши", "наши", "наших", "нашим", "нашими", "наших")
    
    interrogmanim = ("whose", "чей", "чьего", "чьего", "чьему", "чьим", "чьём")
    interrogminan = ("whose", "чей", "чей", "чьего", "чьему", "чьим", "чьём")
    interrogf = ("whose", "чья", "чью", "чьей", "чьей", "чьей", "чьей")
    interrogn = ("whose", "чьё", "чьё", "чьего", "чьему", "чьим", "чьём")
    interrogpanim = ("whose", "чьи", "чьих", "чьих", "чьим", "чьими", "чьих")
    interrogpinan = ("whose", "чьи", "чьих", "чьих", "чьим", "чьими", "чьих")
    
    demonstrative1manim = ("this", "этот", "этого", "этого", "этому", "этим", "этом")
    demonstrative1minan = ("this", "этот", "этот", "этого", "этому", "этим", "этом")
    demonstrative1f = ("this", "эта", "эту", "этой", "этой", "этой", "этой")
    demonstrative1n = ("this", "это", "это", "этого", "этому", "этим", "этом")
    demonstrative1panim = ("this", "эти", "этих", "этих", "этим", "этими", "этих")
    demonstrative1pinan = ("this", "эти", "эти", "этих", "этим", "этими", "этих")
    
    demonstrative2manim = ("this", "тот", "того", "того", "тому", "тем", "том")
    demonstrative2minan = ("this", "тот", "тот", "того", "тому", "тем", "том")
    demonstrative2f = ("this", "та", "ту", "той", "той", "той", "той")
    demonstrative2n = ("this", "то", "то", "того", "тому", "тем", "том")
    demonstrative2panim = ("this", "те", "тех", "тех", "тем", "теми", "тех")
    demonstrative2pinan = ("this", "те", "те", "тех", "тем", "теми", "тех")
    
    inclusivemanim = ("all", "весь", "всего", "всего", "всему", "всем", "всём")
    inclusiveminan = ("all", "весь", "весь", "всего", "всему", "всем", "всём")
    inclusivef = ("all",  "вся", "всей", "всю", "всей", "всей", "всей")
    inclusiven = ("all", "всё", "всё", "всего", "всему", "всем", "всём")
    inclusivepanim = ("all",  "все", "всех", "всех", "всем", "всеми", "всех")
    inclusivepinan = ("all",  "все", "все", "всех", "всем", "всеми", "всех")
    
    