from sqliteConnect import *

def readSongs():
    cursor.execute("SELECT * FROM songs") # select all songs records
    row = cursor.fetchall() # fetch all songs that was retrieved and pass it to the row variable
    for record in row: # iterate through the records(held in the row variable)
        print(record)

#readSongs()