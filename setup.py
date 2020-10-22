#!/usr/bin/python3
"""
    setup.py:  A setup utility to install the machinetrans program.
    Created By Edward Charles Eberle <eberdeed@eberdeed.net>
    August 28, 2017, San Diego California United States of America
"""

from distutils.core import setup
from distutils.util import execute
from glob import glob
import os, sys, pwd

# The class that instantiates and updates the PostgreSQL database.
from machinetrans.dataentry.langdatacreate import LangDataCreate

# Program file lists.
# Here we gather lists of files.
resfilelist = glob('machinetrans/resources/*')
uifilelist = glob('uifiles/*')
datafilelist = glob('data/*')
datapkg = glob('machinetrans/data/*')
parserpkg = glob('machinetrans/parser/*')
dataentrypkg = glob('machinetrans/dataentry/*.py')
dataentrydata = glob('machinetrans/dataentry/*.sql')
userinterfacepkg = glob('machinetrans/userinterfaces/*')
htmldata = glob("docs/*.html")

# if we are creating a distribution (not installing)
# remove the "__pycache__" directories from the tree.
if len(sys.argv) >= 2 and sys.argv[1] != "install":
    if "machinetrans/data/__pycache__" in datapkg:
        datapkg.remove("machinetrans/data/__pycache__")
    if "machinetrans/parser/__pycache__" in parserpkg:
        parserpkg.remove("machinetrans/parser/__pycache__")
    if "machinetrans/dataentry/__pycache__" in dataentrypkg:
        dataentrypkg.remove("machinetrans/dataentry/__pycache__")
    if "machinetrans/userinterfaces/__pycache__" in userinterfacepkg:
        userinterfacepkg.remove("machinetrans/userinterfaces/__pycache__")
    if (os.path.exists("machinetrans/dataentry/user.sql")):
        command = "rm machinetrans/dataentry/user.sql"
        os.system(command)
# Other files in the main directory.
progfilelist = list(['README.txt', 'uifiles.bsh', 
        'CHANGELOG', 'GrammaticalMachineTranslation.odt', 
        'GrammaticalMachineTranslation.pdf'])
# Program scripts.
execfilelist = list(['dataentry.py', 'worddatagen.py'])

# If we are making a distribution then generate the documentation
# and grab the database dump file.
if (len(sys.argv) >= 2) and (sys.argv[1] == "sdist"):
    os.chdir("docs")
    command = "./docgen.py"
    os.system(command)
    os.chdir("..")
    print("\n\n\tEnter the name of the user the database has been \n\n\tran under, I need the database dump.\n\n\t")
    username = input("***>>> ")
    # We create the user.sql file here so it already exists during install.
    datastr = "CREATE USER " + username + " WITH PASSWORD 'MachineTrans';\nCREATE DATABASE " + username + ";\n"
    textfile = open("machinetrans/dataentry/user.sql", "w", newline="\n", encoding="utf-8")
    textfile.write(datastr)
    textfile.close()
    userdir = os.path.join("/home", username)
    dbdir = os.path.join(userdir, ".config/machinetrans/worddata.sql")
    command = "cp -r " + dbdir + " data"
    os.system(command)

# Setup from the distutils module.
setup(name='machinetrans', 
    version='1.15', 
    description='Machine Translation Software', 
    author='Edward Charles Eberle', 
    author_email='eberdeed@eberdeed.net', 
    url='www.eberdeed.net', 
    packages=['machinetrans', 'machinetrans/data', 'machinetrans/parser', 'machinetrans/dataentry', 'machinetrans/userinterfaces'], 
    package_dir={'machinetrans' : 'machinetrans', 'machinetrans/data' : 'machinetrans/data', 'machinetrans/parser' : 'machinetrans/parser', 
        'machinetrans/dataentry' : 'machinetrans/dataentry', 'machinetrans/userinterfaces' : 'machinetrans/userinterfaces'}, 
    package_data={'machinetrans' : ['machinetrans/lineediten.py', 'machinetrans/lineeditru.py', 'machinetrans/helpview.py'], 
        'machinetrans/data' : datapkg, 'machinetrans/parser' : parserpkg, 'machinetrans/dataentry' : dataentrypkg, 
        'machinetrans/userinterfaces' : userinterfacepkg}, 
    data_files=([('/usr/share/machinetrans/resources', resfilelist),
        ('machinetrans-1.15/data', datafilelist), 
        ('/usr/share/doc/machinetrans-1.15-doc', htmldata), 
        ('/usr/bin', execfilelist), 
        ('machinetrans-1.15', progfilelist),
        ('machinetrans-1.15/uifiles', uifilelist),
        ('machinetrans-1.15/machinetrans/dataentry', dataentrydata)]) 
     )
""" Calls the setup method from distutils with the given parameters.
"""
    
# Check to see if this is an install, if so instantiate the database.
if (len(sys.argv) >= 2) and (sys.argv[1] == "install"):    
    langdata = LangDataCreate()
