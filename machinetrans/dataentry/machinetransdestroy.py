#!/usr/bin/python3
"""
    MachineTransDestroy:  Removes the PostgreSQL database and user machinetrans.
    Created by Edward Charles Eberle <eberdeed@eberdeed.net>
    October 25, 2016 San Diego California United States of America
"""    
import os, sys, pwd

class MachineTransDestroy:
    """ Removes the PostgreSQL database and role machinetrans.
    """
    db = None
    curruid = 0
    def __init__(self):
        """ Do nothing well.
        """
        return
    
    def removedb(self):
        """ Check to see if the user is root. If not 
            prompt with an error message.
        """
        datalist = list()
        datalist = pwd.getpwnam("root")
        self.curruid = os.getuid()
        uid = datalist[2]
        if self.curruid != uid:
            print("\n\nUser must be root. Try again as root.")
            print("This program will totally remove the machinetrans database.\n\n")
            return
        else:
            datalist = list()

    def deletemachine(self):
        """ Drop the database using the SQL commands provided in the
            "droptrans.sql" file.  If the process fails inform the user.
        """
        try:
            datalist = list()
            datalist = pwd.getpwnam("postgres")
            uid = datalist[2]
            os.setuid(uid)
            print("\n\nDeleting database and user \"machinetrans\".\n\n")
            command = "psql < machinetrans/dataentry/droptrans.sql"
            os.system(command)
        except Exception as e:
            print("\n\nThe user and/or database \"machinetrans\"")
            print("was not removed from the PostgreSQL database.")
            print("in order to be completely removed this user and")
            print("database needs to be deleted.")
            print("Error:  ", e, "\n\n")
            sys.exit(1)
        print("\n\nSuccessfuly removed machintrans from the system.\n\n")

        
