from sqliteConnect import *
import readData
import time

def deleteSongs():
    #songsID to be deleted
    idField = input("enter the songID of the song to be deleted: ")
    "Method1"
    cursor.execute(f"DELETE FROM songs WHERE SongID= {idField}") # if you type  WHERE SongID > 30 it will delete songs with songsID greater than 30
    "Method 2"
    #cursor.execute(f"DELETE FROM songs WHERE SongID=" + idField")

    conn.commit()
    print(f"Record {idField} deleted from Songs table")

    time.sleep(3)
    readData.readSongs() # invoke the readSongs subroutine from the readData python app

#deleteSongs()  # invoke deleteSongs 
