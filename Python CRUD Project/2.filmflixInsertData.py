from filmflixConnect import *
import time

# create a subroutine to add films to tbale films in filmflix.db

def addFilms():
    # create an empty list
    films = []

    title = input("Enter film title: ")
    yearReleased = input("Enter year released:  ")
    rating = input("Enter rating: ")
    duration = input("Enter duration: ")
    genre = input("Enter film genre: ")

    # append captured data from the user to the film list []
    "films.filmID is set to auto increment and would be added automatically"
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?,?,?,?,?)", tblFilms)
    conn.commit() # commit/write changes to the songs table in the database
    print(f"{title} added to Films table ") # display the name of the song that was added
    time.sleep(3)







