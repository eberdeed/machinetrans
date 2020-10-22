#!/usr/bin/python3
"""
    WordParseSmall:  A class to parse Russian nouns
    in order to determine their gender.
    Edward C. Eberle <eberdeed@eberdeed.net>
    July 30, 2016 San Diego California
"""

import sys, os, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from machinetrans.data.wordmorph import WordMorph

class WordParseSmall:
    """ A class to parse Russian nouns
        in order to determine their gender.
    """
    singends = dict()
    endings = dict()
    morphs = None
    parent = None
    
    def __init__(self, parent):
        """ Initialize the class.  Create regular expressions and compile them.
        """
        self.parent = parent
        self.morphs = self.parent.morphs
        tmplist = list(self.morphs.feminounsing)
        end = None
        tmplist.append(self.morphs.adjfemideclhrd[1])
        tmplist.append(self.morphs.adjfemideclsft[1])
        tmplist.append(self.morphs.adjfemideclgkx[1])
        tmplist.append(self.morphs.adjfemio[1])
        tmplist.append(self.morphs.adjfemimyagkiy[1])
        tmpstr = self.createpattern(tmplist)
        end = re.compile(tmpstr, flags=re.IGNORECASE)
        self.singends["feminounsing"] = end
        tmplist = list(self.morphs.nuetnounsing)
        tmplist.append(self.morphs.adjnuetdeclhrd[1])
        tmplist.append(self.morphs.adjnuetdeclsft[1])
        tmplist.append(self.morphs.adjnuetdeclgkx[1])
        tmplist.append(self.morphs.adjnueto[1])
        tmplist.append(self.morphs.adjnuetmyagkiy[1])
        tmpstr = self.createpattern(tmplist)
        end = re.compile(tmpstr, flags=re.IGNORECASE)
        self.singends["nuetnounsing"] = end
        tmplist = list(self.morphs.mascnounsing)
        tmplist.append(self.morphs.adjmascdeclhrdanim[1])
        tmplist.append(self.morphs.adjmascdeclhrdinan[1])
        tmplist.append(self.morphs.adjmascdeclsftanim[1])
        tmplist.append(self.morphs.adjmascdeclsftinan[1])
        tmplist.append(self.morphs.adjmascdeclgkxanim[1])
        tmplist.append(self.morphs.adjmascdeclgkxinan[1])
        tmplist.append(self.morphs.adjmascoanim[1])
        tmplist.append(self.morphs.adjmascoinan[1])
        tmplist.append(self.morphs.adjmascmyagkiyanim[1])
        tmplist.append(self.morphs.adjmascmyagkiyinan[1])
        tmpstr = self.createpattern(tmplist)
        end = re.compile(tmpstr, flags=re.IGNORECASE)
        self.singends["mascnounsing"] = end
        tmplist = list(self.morphs.mascnounplur)
        tmplist.append(self.morphs.adjplurdeclhrdanim[1])
        tmplist.append(self.morphs.adjplurdeclhrdinan[1])
        tmplist.append(self.morphs.adjplurdeclsftanim[1])
        tmplist.append(self.morphs.adjplurdeclsftinan[1])
        tmplist.append(self.morphs.adjplurdeclgkxanim[1])
        tmplist.append(self.morphs.adjplurdeclgkxinan[1])
        tmplist.append(self.morphs.adjpluroanim[1])
        tmplist.append(self.morphs.adjpluroinan[1])
        tmplist.append(self.morphs.adjplurmyagkiyanim[1])
        tmplist.append(self.morphs.adjplurmyagkiyinan[1])
        tmpstr = self.createpattern(tmplist)
        end = re.compile(tmpstr, flags=re.IGNORECASE)
        self.singends["plurnoun"] = end
        
    def createpattern(self, pattset):
        """ Create a regular expression from the provided list of endings.
        """
        pattstr = ""
        if isinstance(pattset, list):
            pattstr = "(" + "|".join(pattset) + ")$"
            return pattstr
        else:
            print("\n\n\tError pattern set ", pattset, " not a tuple.\n\n")
            return None
    
    def parse(self, word):
        """ Parse a singular undeclined Russian noun.
        """
        foundlist = list()
        ongoing = True
        found = False
        matchobj = None
        endchar = word[-1]
        penul = word[-2]
        for regex in sorted(self.singends):
            matchobj = self.singends[regex].search(word)
            if matchobj:
                found = True
                tmplist = list()
                count = 0
                tmplist.append(regex)
                tmplist.append(word)
                tmplist.append(matchobj.group(0))
                tmplist.append(self.singends[regex].pattern)
                tmpint = len(matchobj.group(0))
                if (len(foundlist) > 0):
                    listfound = False
                    for x in range(len(foundlist)):
                        itemlist = foundlist[x]
                        tmpint1 = len(itemlist[2])
                        if tmpint >= tmpint1:
                            listfound = True
                            foundlist.insert(count, tmplist)
                        count += 1
                    if not listfound:
                        foundlist.append(tmplist) 
                else:
                    foundlist.append(tmplist)
        if not found:
            return "masculine"
        else:
            tmpstr = ""
            itemlist = foundlist[0]
            data = itemlist[0]
            if "masc" in data :
                return "masculine"
            elif "fem" in data:
                return "feminine"
            elif "nuet" in data: 
                return "nueter"
            elif "plur" in data:
                return "plural"
            else:
                return "masculine"
        
    def parsewords(self):
        """ Driver to allow entry of Russian words into the class as a standalone.
        """
        foundlist = list()
        ongoing = True
        found = False
        matchobj = None
        while ongoing:
            print("\n\n\tEnter a Russian word.\n\t")
            answer = input("***>>> ")
            foundlist = list()
            found = False
            if answer[0] == 'q' or answer[0] == '№':
                ongoing = False
            for regex in sorted(self.endings):
                matchobj = self.endings[regex].search(answer)
                if matchobj:
                    found = True
                    tmplist = list()
                    count = 0
                    tmplist.append(regex)
                    tmplist.append(answer)
                    tmplist.append(matchobj.group(0))
                    tmplist.append(self.endings[regex].pattern)
                    tmpint = len(matchobj.group(0))
                    if (len(foundlist) > 0):
                        listfound = False
                        for x in range(len(foundlist)):
                            itemlist = foundlist[x]
                            tmpint1 = len(itemlist[2])
                            if tmpint >= tmpint1:
                                listfound = True
                                foundlist.insert(count, tmplist)
                            count += 1
                        if not listfound:
                            foundlist.append(tmplist) 
                    else:
                        foundlist.append(tmplist)
            if not found:
                tmpstr = ""
                for x in answer:
                    tmpstr += str(ord(x)) + ", "
                tmpstr = tmpstr[:-2]
            else:
                tmpstr = ""
                itemlist = foundlist[0]
                for x in itemlist:
                    tmpstr += x + ", "
                tmpstr = tmpstr[:-2]
                    
