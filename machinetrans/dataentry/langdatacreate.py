#!/usr/bin/python3
""" 
    LangDataCreate:  A class to instantiate a PostgreSQL
    database containing Russian-English data.
"""
import os, sys, pwd, subprocess
import psycopg2 as pg_driver
from machinetrans.dataentry.machinetransdestroy import MachineTransDestroy


class LangDataCreate:
    """ A class to instantiate a PostgreSQL
        database containing Russian-English data.
    """
    def __init__(self):
        """ Run the entire class.  Check to see if the user
            is root, if not generate an error and exit.
            Check to see if there is an existing installation,
            if so, prompt for replacement. If the answer is
            "yes" Instantiate the MachineTransDestroy class
            to erase the current database. 
            Create the database template.  
        """
        # Check for root.
        datalist = list()
        datalist = pwd.getpwnam("root")
        curruid = os.getuid()
        uid = datalist[2]
        if curruid != uid:
            print("\n\nUser must be root. Try again as root.\n\n")
            return
        else:
            datalist = list()
        try:
            # Check for an existing database.
            db = pg_driver.connect( \
                user = 'machinetrans', \
                dbname = 'machinetrans', \
                password = 'MachineTrans', \
                host = 'localhost', \
                port = 5432 \
                )
            db.close()
            print("\n\n\tThe program has found an existing installation,")
            print("Do you wish to have it re-created? (y or n)\n")
            answer = input("***>>> ")
            answer = answer.lower()
            if (answer[0] == 'y'):
                machdata = MachineTransDestroy()
                machdata.removedb()
                machdata.deletemachine()
            else:
                print("\n\n\tSuccessfully installed.\n\n")
                sys.exit(0)
        except Exception as e:
            # If there is no database, Create the necessary user.
            print("\n\nBeginning installation.\n\n")
            try:
                print("\n\nCreating user machinetrans.\n\n")
                command = "useradd -M -p MachineTrans machinetrans"
                os.system(command)
            except Exception as e:
                print("\n\nUnable to create the system user machinetrans.")
                print("This user is needed for the program to work properly.\n\n")
        try:
            # Create the database and PostgreSQL role.
            datalist = pwd.getpwnam("postgres")
            uid = datalist[2]
            os.seteuid(uid)
            try:
                command = "psql < machinetrans/dataentry/machinetrans.sql"
                os.system(command)
            except:
                print("\n\tDatabase machinetrans already exists, creating tables.\n")
            db = pg_driver.connect( \
            user = 'machinetrans', \
            dbname = 'machinetrans', \
            password = 'MachineTrans', \
            host = 'localhost', \
            port = 5432 \
            )
            print("\n\tDatabase connection to machinetrans established.\n")
        except Exception as e:
            print("\n\nThe program has failed to create and/or")
            print("log into the PostgreSQL user MachineTrans.")
            print("This user must be created along with the ")
            print("database \"machinetrans\" in order for the ")
            print("program to work properly.")
            print("Error:  ", e ,"\n\n")
            return
        try:
            ##################################################################################################
            # What you see below is the template for the database.
            ##################################################################################################
            cur = db.cursor()
            cur.execute( \
                """
                CREATE TYPE noun_var AS ENUM ('abstract', 'proper', 'concrete', 
                    'collective', 'compound');
                CREATE TYPE verb_var AS ENUM ('motion', 'other');
                CREATE TYPE adj_var AS ENUM ('descriptive', 'comparative', 'superlative', 'short adjective');
                CREATE TYPE adv_var AS ENUM ('state', 'manner', 'place', 'time', 'degree', 'other');
                CREATE TYPE pron_var AS ENUM ('personal', 'demonstrative', 'possessive', 
                    'interrogative', 'reflexive', 'reciprocal', 'indefinite', 
                    'relative', 'inclusive', 'variety');
                CREATE TYPE prtcpl_var AS ENUM ('present active', 'present passive', 
                    'past active', 'past passive', 'present verbal adverb', 'past verbal adverb 1', 'past verbal adverb 2',
                    'short past passive', 'formal imperative', 'informal imperative');
                CREATE TYPE prep_var AS ENUM ('place', 'time', 'other');
                CREATE TYPE conj_var AS ENUM ('coordinating', 'subordinating');
                CREATE TYPE symb_var AS ENUM ('glyph', 'number', 'other');
                CREATE TYPE intrgs_var AS ENUM ('person', 'place', 'time', 'method', 'reason', 'ownership', 'quantity');
                CREATE TYPE tense_var AS ENUM ('imperative', 'simple present', 'simple past', 
                    'perfect simple past', 'perfect continuous past', 
                    'continuous past', 'continuous present', 'perfect simple present', 
                    'perfect continous present', 'simple future', 'continuous future', 
                    'perfect simple future', 'perfect continuous future');
                CREATE TYPE ntype_var AS ENUM ('location', 'thing');
                CREATE TYPE prsn_var AS ENUM ('first', 'second', 'third', 'plural first', 'plural second', 'plural third');
                CREATE TYPE case_var AS ENUM ('nominative', 'accusative', 'genitive', 'dative', 'instrumental', 'prepositional');
                CREATE TYPE obj_var AS ENUM ('nominative', 'accusative', 'genitive', 'dative', 'instrumental', 'prepositional', 'none');
                CREATE TYPE gender_var AS ENUM ('masculine', 'feminine', 'nueter', 'plural');
                CREATE TYPE animate_var as ENUM ('animate', 'inanimate');
                CREATE TYPE imperfective_var as ENUM ('imperfective', 'perfective');
                CREATE TYPE invar_var as ENUM ('foreign', 'subjunctive', 'acronym', 'other');
                CREATE TABLE nouns( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety noun_var DEFAULT 'concrete', 
                    gender gender_var DEFAULT 'masculine',
                    type ntype_var DEFAULT 'thing',
                    declension text DEFAULT '',
                    wordcase case_var DEFAULT 'nominative',
                    animate animate_var DEFAULT 'animate'
                    );
                CREATE TABLE interjections( 
                    name text DEFAULT '', 
                    runame text DEFAULT ''
                    );
                CREATE TABLE verbs( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety verb_var DEFAULT 'other', 
                    tense tense_var DEFAULT 'simple present', 
                    person prsn_var DEFAULT 'third', 
                    objcase obj_var DEFAULT 'accusative',
                    conjugationru text DEFAULT '',
                    conjugation text DEFAULT '',
                    imperfective imperfective_var DEFAULT 'imperfective'
                    );
                CREATE TABLE pastverbs(
                    name text DEFAULT '',
                    runame text DEFAULT '',
                    tense tense_var DEFAULT 'simple past', 
                    gender gender_var DEFAULT 'masculine',
                    conjugation text DEFAULT '',
                    conjugationru text DEFAULT '',
                    objcase obj_var DEFAULT 'accusative',
                    imperfective imperfective_var DEFAULT 'imperfective'
                    );
                CREATE TABLE adjectives( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety adj_var DEFAULT 'descriptive', 
                    gender gender_var DEFAULT 'masculine',
                    declension text DEFAULT '',
                    wordcase case_var DEFAULT 'nominative',
                    animate animate_var DEFAULT 'animate'
                    );
                CREATE TABLE adverbs( 
                    name text DEFAULT ' ', 
                    runame text DEFAULT '',
                    variety adv_var DEFAULT 'manner' 
                    );
                CREATE TABLE invariants( 
                    name text DEFAULT ' ', 
                    runame text DEFAULT '',
                    wordcase obj_var DEFAULT 'nominative',
                    variety invar_var DEFAULT 'foreign'
                    );
                CREATE TABLE pronouns( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety pron_var DEFAULT 'personal',
                    gender gender_var DEFAULT 'masculine',
                    declension text DEFAULT '',
                    wordcase case_var DEFAULT 'nominative',
                    animate animate_var DEFAULT 'animate'
                    );
                CREATE TABLE participles( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety prtcpl_var DEFAULT 'past passive' ,
                    gender gender_var DEFAULT 'masculine',
                    objcase obj_var DEFAULT 'accusative',
                    animate animate_var DEFAULT 'animate',
                    declension text DEFAULT '',
                    enval text DEFAULT '',
                    wordcase case_var DEFAULT 'nominative'
                    );
                CREATE TABLE prepositions( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety prep_var DEFAULT 'place', 
                    objcase obj_var DEFAULT 'accusative'
                    );
                CREATE TABLE conjunctions( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety conj_var DEFAULT 'coordinating' 
                    );
                CREATE TABLE symbols( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety symb_var DEFAULT 'number' 
                    );
                CREATE TABLE interrogatives( 
                    name text DEFAULT '', 
                    runame text DEFAULT '',
                    variety intrgs_var DEFAULT 'person'
                    );
                """ \
            )
            ##########################################################################################
            ##########################################################################################
            db.commit()
            db.close()
            # Success!
            print("\n\nDatabase successfully created.\n\n")
        except Exception as e:
            print("\n\nError creating type or table:  " + str(e))
            print("The database structures were not created.")
            print("In order to use the program these structures")
            print("must exist in the database \"machinetrans\".\n\n")
            print("Error:  ", e)
            sys.exit(1)
        try:
            command = "psql machinetrans < data/worddata.sql"
            os.system(command)
            print("\n\tSuccessfully added the data to machinetrans.\n")
        except Exception as e:
            print("\n\tError:  Unable to add the data to the machinetrans database.  ", e)

    
    
