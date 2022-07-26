from mysqlConnect import *
import readMembers
import time

def searchMember():
    # enter the field you like to perform a search on
    searchField = input("Which field would you like to search: (firstname, lastname, email)? ").title()
    searchValue = input(f"Enter the value for the {searchField} you want to search: ")
    print(f"The search value entered is {searchValue} ")

    # add single quotes
    searchValue = "'" + searchValue + "'"
    print(f"The amended search value entered is {searchValue}")

    # search database
    #"SELECT * FROM members WHERE Firstname = Fatih Dulger "
    #cursor.execute("SELECT * FROM members WHERE " + searchField + "=" + searchValue)

    # Method 2
    cursor.execute(f"SELECT * FROM members WHERE {searchField} = {searchValue}")

    #conn.commit()
    time.sleep(3)

    row = cursor.fetchall()
    #convert/casting row to as tingring datatype
    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)
    else: 
        print(f"The field {searchField} does not contain a {searchValue} in the database! ")
    
    
searchMember()

"""from mysqlConnect import *

import time




def searchMember():

    # Enter the field you would like to perform a search on

    searchField = input(

        "Which field would you like to search: (Firstname, Lastname, Email)?  "

    ).title()

    searchValue = input(f"Enter the value for the {searchField} you want to search:  ")

    print(f"The search value entered is {searchValue} ")



    #  add single quotes

    searchValue = "'" + searchValue + "'"

    print(f"The amended search value entered is {searchValue} ")



    #  seacrch database

    "SELECT * FROM  songs WHERE Artist  = Michael Jackson "

    # cursor.execute("SELECT * FROM  songs WHERE " + searchField + "=" + searchValue)

    "Method 2"
    cursor.execute(f"SELECT * FROM  members WHERE {searchField} = {searchValue}")

    # conn.commit()

    time.sleep(3)
    row = cursor.fetchall()

    # convert/cast(row) to a string datatype

    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)

    else:

        print(

            f"The field {searchField} does not contain a {searchValue} in the database! "

        )

searchMember()"""











