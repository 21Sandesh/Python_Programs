# loading in modules
import sqlite3

# creating file path
dbfile = 'D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Sanket Project\database.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# here is you table list
print(table_list)

# Be sure to close the connection
con.close()