from mysqlConnect import *
import time

# create subroutine
def addMember():
    # create empty list
    members = []
    # add data entered
    fname = input("Enter firstname: ")
    lname = input("Enter lastname: ")
    email = input("Enter email: ")

    # listName.append(dataCaptured)
    members.append(fname)
    members.append(lname)
    members.append(email)

    #insert data to members table
    # cursor.execute("INSERT INTO members MemberID, Firstname, Lastname, Email VALUES($ .... ") >>>> this is othe method
    cursor.execute("INSERT INTO members VALUES(NULL, %s,%s,%s)", members)   # %s = placeholders
    conn.commit()
    print(f"{fname} added to members table")
    time.sleep(3)

    cursor.execute("SELECT * FROM members")
    row = cursor.fetchall()
    for record in row:
        print(record)

addMember()