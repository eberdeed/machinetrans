#!/usr/bin/python3
"""
    DocGen:  Documentation Generator.
    Edward Charles Eberle <eberdeed@eberdeed.net>
    September 5, 2016, San Diego California USA
"""
import os, sys
from glob import glob

class DocGen:
    
    datapkg = glob('../machinetrans/data/*')
    datalen = len('../machinetrans/data/')
    parserpkg = glob('../machinetrans/parser/*')
    parserlen = len('../machinetrans/parser/')
    entrypkg = glob('../machinetrans/dataentry/*')
    entrylen = len('../machinetrans/dataentry/')
    utilpkg = glob('../machinetrans/*.py')
    utillen = len('../machinetrans/')
    command = list()
    index = "index.html"
    header = \
        """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>MachineTrans Documentation</title>
        <style>
            BODY   {      font-family: Serif;
                    background: white;
                    color: black;
                    line-height: 100%;
                }
           
            H1      {     font-size: 16.0pt;
                    font-family: Serif;
                    line-height: 100%;
                }
        </style>
        </head>
        <body>
        <br><br>
        <center><H1>MachineTrans Documentation</H1></center>
        <br><br>
        """    
    footer = '\n</body>\n</html>\n'
    
    def __init__(self):
        command = "rm *.html"
        os.system(command)
        self.createtopcommand()
        self.createhtml()
        self.createdatacommand()
        self.createhtml()
        self.createparsercommand()
        self.createhtml()
        self.createentrycommand()
        self.createhtml()
        self.createutilcommand()
        self.createhtml()
        self.createindex()
        print("\n\n\tDocumentation Successfully Generated\n\n")
        return

    def createtopcommand(self):
        self.command = list()
        self.command.append("pydoc3 -w ../dataentry.py dummy")
        self.command.append("pydoc3 -w ../worddatagen.py dummy")
                
    def createdatacommand(self):
        self.command = list()
        for x in self.datapkg:
            if not "pycache" in x:
                self.command.append("pydoc3 -w " + x)

    def createparsercommand(self):
        self.command = list()
        for x in self.parserpkg:
            if not "pycache" in x:
                self.command.append("pydoc3 -w " + x)

    def createutilcommand(self):
        self.command = list()
        for x in self.utilpkg:
            if not "pycache" in x:
                self.command.append("pydoc3 -w " + x)

    def createentrycommand(self):
        self.command = list()
        for x in self.entrypkg:
            if not "pycache" in x and not ".sql" in x:
                self.command.append("pydoc3 -w " + x)
                
    def createhtml(self):
        for x in self.command:
            os.system(x)
    
        
    def createindex(self):
        htmllines = ""
        htmllines += "<center><H1>MachineTrans Programs</H1></center><BR>"
        htmllines += "<center><A href=\"dataentry.html\">dataentry.html</A></center><BR>\n"
        htmllines += "<center><A href=\"worddatagen.html\">worddatagen.html</A></center><BR>\n"
        htmllines += "<BR><center><H1>Data Package</H1></center><BR>"
        for x in self.datapkg:
            if not "pycache" in x:
                x = x[self.datalen:]
                x = x.replace(".py", ".html")
                htmllines += "<center><A href=\"" + x + "\">" + x + "</A></center><BR>\n"
        htmllines += "<BR><BR><center><H1>Parser Package</H1></center><BR>"
        for x in self.parserpkg:
            if not "pycache" in x:
                x = x[self.parserlen:]
                x = x.replace(".py", ".html")
                htmllines += "<center><A href=\"" + x + "\">" + x + "</A></center><BR>\n"                
        htmllines += "<BR><BR><center><H1>Data Entry Package</H1></center><BR>"
        for x in self.entrypkg:
            if not "pycache" in x:
                x = x[self.entrylen:]
                x = x.replace(".py", ".html")
                htmllines += "<center><A href=\"" + x + "\">" + x + "</A></center><BR>\n"                
        htmllines += "<BR><BR><center><H1>Utility Classes</H1></center><BR>"
        for x in self.utilpkg:
            if not "pycache" in x:
                x = x[self.utillen:]
                x = x.replace(".py", ".html")
                htmllines += "<center><A href=\"" + x + "\">" + x + "</A></center><BR>\n"                
        htmllines = self.header + htmllines + self.footer
        htmlfile = open(self.index, "w", newline="\n", encoding="utf-8")
        htmlfile.write(htmllines)
        htmlfile.close()
        
def main():
    docs = DocGen()
    return(0)

main()