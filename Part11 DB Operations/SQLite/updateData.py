from sqliteConnect import *
import readData
import time

def updateSongs():
    #songsID to be updated
    idField = input("Enter the songID of the song to be updated: ")
    #enter the name of the field to be updated
    fieldName = input("which field would you like to update: (Title, Artist, Genre)? ").title()
    #enter the value of the field to be updated
    newFieldValue = input(f"Enter the new field value for {fieldName}")
    print(f"The new value entered is {newFieldValue} ")

    # add single quotes around the new field value entered by the user
    newFieldValue = " ' " + newFieldValue + " ' "
    print(f"The new value entered is {newFieldValue} ")
    #UPDATE songs SET {Title, Artist, Genre}

    cursor.execute(f"UPDATE songs SET {fieldName} = {newFieldValue} WHERE SongID = {idField} ")
    conn.commit()
    print(f" Record {idField} Updated form Songs table")

time.sleep(3)
readData.readSongs()  # invoke the readSongs subroutine from the readData python app
#updateSongs() >>>> we are commenting becuase we are calling them in another file.

