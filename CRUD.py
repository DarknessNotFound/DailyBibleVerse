#CRUD.py
import sqlite3

Table = "BibleVerses"

def GetTableName():
    return Table

def TableCreation(DbConnection):
    try:
        c = DbConnection.cursor()
        c.execute("""
            SELECT count(name) FROM sqlite_master
            WHERE type='table'
            AND name='{0}'""".format(Table))

        if c.fetchone()[0]==1:
            print(Table + ' table already exists')
        else:
            print(Table + ' table does not exist')
            print('Creating ' + Table + 'table')
            c.execute('''CREATE TABLE BibleVerses(
                            Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Verse TEXT,
                            DateLastUsed INTEGER,
                            CalledBy TEXT);''')
            print('Created BibleVerses')
    except sqlite3.Error as error:
        print('ERROR: CRUD.py -- TableCreation -- ', error)

def AddNewVerse(DbConnection, UserSubmitted, Text):
    try:
        DbConnection.execute("""
            INSERT INTO {0} (Verse, DateLastUsed, CalledBy)
            VALUES ('{1}', date('now'), '{2}');
        """.format(Table, Text, UserSubmitted))

        DbConnection.commit()
    except sqlite3.Error as error:
        print('ERROR: CRUD.py -- AddNewVerse -- ', error)
