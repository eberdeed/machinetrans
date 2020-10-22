"""
   WordMenu:  A class to encapsulate menu values
   for random sentence generation.
   Edward C. Eberle <eberdeed@eberdeed.net>
   July 2, 2016 San Diego, California USA
"""
import os, sys

class WordMenu:
    """ A class to encapsulate menu values
        for random sentence generation.
    """
    mainmenu = list(["Word Generation Menu", \
        "Verbs of Contemplation", \
        "Verbs of Motion", \
        "Participles",
        "Interrogatives",
        "Conditional Sentences",
        "Comparative Degree"])

    contemplation = list(["Verbs of Contemplation", \
        "A-S-V", \
        "A-S-V-A-O", \
        "A-S-V-A-ADJ-O", \
        "A-S-AV-V-A-ADJ-O", \
        "A-ADJ-S-AV-V-A-ADJ-O"])

    motion = list(["Verbs of Motion", \
        "A-S-V", \
        "A-S-V-A-O", \
        "A-S-V-A-ADJ-O", \
        "A-S-AV-V-A-ADJ-O", \
        "A-ADJ-S-AV-V-A-ADJ-O"])
    """
    Curently not being used.
    modal = list(["Modal Verbs", \
        "A-S-MV-V", \
        "A-S-MV-V-A-O", \
        "A-S-MV-V-A-ADJ-O", \
        "A-S-MV-AV-V-A-ADJ-O", \
        "A-ADJ-S-AV-MV-V-A-ADJ-O"])
    """
    participle = list(["Participles", \
        "A-S-V-AV-AXV-PRT-A-O", \
        "A-S-V-AXV-PRT-PR-A-O", \
        "A-ADJ-S-V-AXV-PRT-PR-A-ADJ-O", \
        "A-ADJ-S-V-AV-AXV-PRT-PR-A-ADJ-O",
        "A-ADJ-S-AV-V-AXV-PRT-PR-A-ADJ-O"])
    
    interrogative = list(["Interrogatives", \
        "I-V", \
        "I-V-O", \
        "I-V-ADJ-O", \
        "I-AV-V-O", \
        "I--AV-V-ADJ-O"])

    conditional = list(["Conditional Sentences", \
        "If A-S-V, then A-S-V", \
        "If A-S-V-A-O, then A-S-V-A-O", \
        "If A-S-V-A-ADJ-O, then A-S-V-A-ADJ-O", \
        "If A-S-AV-V-A-ADJ-O, then A-S-AV-V-A-ADJ-O", \
        "If A-ADJ-S-AV-V-A-ADJ-O, then A-ADJ-S-AV-V-A-ADJ-O"])

    comparative = list(["Comparative Degree", \
        "If A-S-V-Comp, then A-S-V", \
        "If A-S-V-Comp, then A-S-V-A-O", \
        "If A-S-V-Comp, then A-S-V-A-ADJ-O", \
        "If A-S-V-Comp, then A-S-AV-V-A-ADJ-O", \
        "If A-S-V-Comp, then A-ADJ-S-AV-V-A-ADJ-O"])
