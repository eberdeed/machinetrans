#!/usr/bin/python3
"""
      DeclTable.py  A program to generate an HTML table
      containing a given Russian declension list.
      Distributed under the GNU Public License with no 
      guarentees expressed or implied and not intended to be
      suitable for any use.
      by Edward Charles Eberle <eberdeed@eberdeed.net>
      August 1, 2016, San Diego, CA, USA
"""

import os, sys, math

class DeclTable:
    """ A program to generate an HTML table
        containing a given Russian declension list.
    """
    # HTML table data.
    header = \
        """
        <html>
        <head>
            <meta charset="UTF-8">
        <style>
            BODY   {      font-family: Serif;
                    background: white;
                    color: black;
                    line-height: 100%;
                }
            TABLE  { 
                    font-size:  16pt;
                    font-weight: bold;
                    color: black;
                    font-family: sans;
                }
            TD   {
                    width: 80px; 
                    height: 15px; 
                    vertical-align: top; 
                    text-align: center;
                    border: inset 1px;
                    border-color: #DBA244; 
                    border-width: 1px; 
                    background-color: yellow; 
                }
            H1      {     font-size: 16.0pt;
                    font-family: Serif;
                    line-height: 100%;
                }
        </style>
        </head>
        <body>
        """
    nameheader = '<center>{}</center><BR>\n' \
        + '<center>\n<table>\n' \
        + '<tr>\n<td>Declension</td>\n' \
        + '<td>Desc</td><td>Nom</td>\n' \
        + '<td>Acc</td>\n<td>Gen</td>\n'\
        + '<td>Dat</td>\n<td>Instr</td>\n' \
        + '<td>Prep</td>\n</tr>\n'
    footer = '</tr>\n</table>\n</center><BR><BR>\n</body>\n</html>\n'
    datumtag = '<td>'
    rowtag =  '<tr>'
    closedatum = '</td>'
    closerow = '</tr>'
    caltable = ''
    newline = '\n'
    count = 0
    rustr = ""

    def __init__(self, rustr, begin = 0):
        """ Initialize the class and create a title for the table.
        """
        self.rustr = rustr
        self.caltable = ""
        self.count = begin
        tmpstr = "Russian Declension for " + self.rustr
        self.nameheader = self.nameheader.format(tmpstr)
        return

    def addrow(self, rowlist):
        """ Add a row to the HTML table.
        """
        self.count += 1
        self.caltable += self.rowtag + self.newline
        self.caltable += self.datumtag + str(self.count) + self.closedatum + self.newline
        for x in rowlist:
            self.caltable += self.datumtag + x + " " + self.closedatum + self.newline
        self.caltable += self.closerow + self.newline
        return
 
    def table(self):
        """ Generate the completed table and return it to the calling class.
        """
        tmptext = list()
        tmptext = self.header + self.nameheader + self.caltable + self.footer
        return tmptext