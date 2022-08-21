from filmflixConnect import *

"""
Note:
CRUD: Create Read Update Delete.
Only one table in the database with records, which is all you need for this project.
Database name filmflix.db
Table name tblfilms
filmID(integer), title(text), yearReleased(integer),rating(text),duration(integer),genre(text)

You have now been tasked with developing a python application to manipulate the FilmFlix database.
Perform CRUD operation on the database from the python command line
1.	Print all records in  tblfilms in database filmflix.db
2.	Allows users to add, update or delete records in the filmflix.db database (CRUD)
3.	Print a selection of reports, these functions demonstrate different techniques of writing sql commands and printing reports
"""
def readFilms():
    cursor.execute("SELECT * FROM tblfilms")
    row = cursor.fetchall()
    for record in row:
        print(record)

readFilms()
