from sqliteConnect import *

# import readData
import time
def searchSong():
    # enter the field you would like to perform a search on
    searchField = input(
        "Which field would you like to search: (Title, Artist, Genre)? "
    ).title()
    searchValue = input(f"Enter the value for the {searchField} you want to search: ")
    print(f"The search value entered is {searchValue} ")

    # add single quotes
    searchValue = "'" + searchValue + "'"
    print(f"The amended search value entered is {searchValue}")
    """Method 1"""
    # search database
    #"SELECT * FROM songs WHERE Artist name = Michael Jackson "
   # cursor.execute("SELECT * FROM songs WHERE " + searchField + "=" + searchValue)


    "Method 2"
    cursor.execute(f"SELECT * FROM songs WHERE {searchField} = {searchValue}")

    conn.commit()
    time.sleep(3)

    row = cursor.fetchall()
    #conver/cast(row) to a string datatype
    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)
    else:
        print(f"The field {searchField} does not contain a {searchValue} in the database! ")
    
searchSong()
