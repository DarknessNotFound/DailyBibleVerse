#main.py
import sqlite3
from CRUD import *

try:
    DbCon = sqlite3.connect('DailyBibleVerse.db')
    print('Connected to DailyBibleVerse.db')
    
    Table = GetTableName()

    TableCreation(DbCon)
    AddNewVerse(DbCon, "Grant -- Test5", "Jesus Wept -- Test Verse")
    AddNewVerse(DbCon, "Grant -- Test6", "Jesus Wept -- Test Verse")
    AddNewVerse(DbCon, "Grant -- Test7", "Jesus Wept -- Test Verse")
    AddNewVerse(DbCon, "Grant -- Test8", "Jesus Wept -- Test Verse")
    
    c = DbCon.execute("SELECT * from " + Table + ";")
    for row in c:
        print(row)
    
    c.close()

except sqlite3.Error as error:
    print('ERROR: main.py -- ', error)

finally:
    if DbCon:
        DbCon.close()
        print('Disconnected from DailyBibleVerse.db')
