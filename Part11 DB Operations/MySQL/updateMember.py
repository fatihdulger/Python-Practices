from mysqlConnect import *
import readMembers
import time

def updateMembers():
    # MemberID to be updated
    idField = input("Enter the MemberID of the member to be updated: ")
    # enter the name of the field to be updated
    fieldName = input("Which field would you like to update: (Firstname, Lastname, Email)?: ")
    #enter the value of the field to be updated
    newFieldValue = input(f"Enter the new field value for {fieldName} ")
    print(f"The new value entered is {newFieldValue} ")

    # add single quotes around the new field value entered by the user

    newFieldValue = "'" + newFieldValue +  "'"
    print(f"The new value entered is {newFieldValue} ")

    #UPDATE members SET {Firstname, Lastname, Email}
    cursor.execute(f"UPDATE members SET {fieldName} = {newFieldValue} WHERE MemberID = {idField} ")
    conn.commit()
    print(f"Record {idField} Updated from members table")

time.sleep(3)
readMembers.readMembers()
updateMembers() # invoke the readMembers subroutine from the readMembers python app


