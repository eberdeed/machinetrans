
    To use this program a few things are needed.

    You must have postgresql installed along with
    python3, the python3 postgresql driver psycopg2 
    and PyQt5.
    
    To execute the program there must exist a machinetrans
    system user and the postgresql roles for the regular user and 
    machinetrans user as well as regular user and machinetrans 
    user named postgresql databases. Usually the machinetrans 
    user and database are provided by the setup program. The 
    user's database needs to be provided by you.
    try from the command line in the user's account:
    
    psql
    
    CREATE ROLE [user];
    CREATE DATABASE [user];
    
    That will satisfy postgresql's requirements for
    a user role and database.  Substitute your username
    for [user].
    
    To install the program, from root type:
    "./setup.py install"

    To run the vocabulary data entry program type:
    "dataentry.py"
    
    To run the random sentence generator type:
    "worddatagen.py"
    
    Enjoy!
    Questions? <eberdeed@eberdeed.net>
    Edward C. Eberle    
    October 22, 2020 San Diego, California USA
