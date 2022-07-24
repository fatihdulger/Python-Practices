from mysqlConnect import *
import readMembers
import time

def deleteMembers():
    #songsID to be deleted
    idField = input("enter the MemberID of the member to be deleted: ")
    "Method1"
    cursor.execute(f"DELETE FROM members WHERE MemberID= {idField}") # if you type  WHERE SongID > 30 it will delete songs with songsID greater than 30
    "Method 2"
    #cursor.execute(f"DELETE FROM members WHERE MemberID=" + idField")

    conn.commit()
    print(f"Record {idField} deleted from Members table")

    time.sleep(3)
    readMembers.readMembers() # invoke the readSongs subroutine from the readData python app

deleteMembers()  # invoke  deleteMember()


"""from mysqlConnect import *
import readMembers
import time


def deleteMember():
    # songsID to be deleted
    idField = input("Enter the MemberID of the member to be deleted: ")
    "Method 1"
    cursor.execute(f"DELETE FROM members WHERE MemberID= {idField}")
    "Method 2"
    # cursor.execute("DELETE FROM members WHERE MemberID=" + idField)

    conn.commit()
    print(f" Record {idField} deleted form members table")

    time.sleep(3)
    readMembers.readMembers()  # invoke the readSongs subroutine from the readData python app

deleteMember()  # invoke  deleteMember()
"""