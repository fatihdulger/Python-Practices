from sqliteConnect import *
import time

# create a subroutine to add songs to table songs in c10sqlite.db

def addSongs():
    #create an empty list
    songs = []

    # capture data inputed by the user
    title = input("Enter song title: ")
    artist = input("Enter Artist: ")
    genre = input("Enter song Genre: ")

    #append captured data from the user to the song list []
    "songs.songID is set to auto increment and would be added automatically"
    #listName.append(variableName)
    songs.append(title)
    songs.append(artist)
    songs.append(genre)

    # insert data from the list into the songs table

    cursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)",songs)
    conn.commit() # commit/write changes to the songs table in the database
    print(f"{title} added to Songs table") # display the name of the song that was added
    time.sleep(3)

    cursor.execute("SELECT * FROM songs") # select all songs records  >>> this bit is about read data added or changed
    row = cursor.fetchall() # fetch all songs that was retrieved and pass it to the row variable
    for record in row: # iterate through the records(held in the row variable)
        print(record)
    
#addSongs() # call/invoke the subroutine
