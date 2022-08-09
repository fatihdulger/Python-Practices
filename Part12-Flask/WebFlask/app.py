from flask import Flask, render_template, request, url_for, redirect, abort, Response
import sqlite3 as sql

# create an instance object of the flask class

app = Flask(__name__)  # main class    # app will be our object

# create a function to handle db connection

def musicDBcon():
    #conn variable = sql.connectFunction(path/filename.ext)
    conn = sql.connect("PYTHON\Part12 Flask\webflask\c10Sqlite.db")
    #row_factory is used to manipulate/access the db
    conn.row_factory = sql.Row  # we are accesing class row
    return conn


# set the routes for the index.html/home
@app.route("/") # 192.168.0.6/
@app.route("/index") # 192.168.0.6/index.html
def index():
    #returns the index page in the browser on load
    return render_template("index.html", title="Home")




# set the routes for the songs.html
@app.route("/songs")
def songs():
    # read song data from the database
    songConn = musicDBcon()
    cursor = songConn.cursor()
    cursor.execute("SELECT * FROM songs")  # selecting evrything in db and then we will pass it to fetchall()
    getSongs = cursor.fetchall()
    #returns the songs page in the browser when the songs text/link is clicked on the menu
    return render_template("songs.html", title = "Songs", songsInDB = getSongs)

"Delete song by songID" # 192.168.0.9:23500/songID=21
@app.route("/<int:songID>/delete", methods=("POST",))  # we set up the route
def delete(songID): # we are passing songID above
    songConn = musicDBcon()
    cursor = songConn.cursor()
    cursor.execute("DELETE FROM songs WHERE songID =?", (songID,))
    songConn.commit()
    songConn.close()
    return redirect(url_for("songs")) # redirect to the songs page after delete

# now we need to get songID to pass it on above function to be able to do that we need another function  - because we cant delete before we get songID 
#Create a function to get a specific song"
def getSong(recordID):
    songConn = musicDBcon()
    cursor = songConn.cursor()
    #
    aSong = cursor.execute("SELECT * FROM songs WHERE songID =?", (recordID,)).fetchone()
    songConn.close()

    if aSong is None:
        abort(Response(f"No Record {aSong} was found in DB"))
    return aSong

"Update a Song"
@app.route("/<int:songID>/update", methods=("GET","POST"))
def update(songID):
    aSongRecord = getSong(songID)
    if request.method == "POST":
        title = request.form["Title"]
        artist = request.form["Artist"]
        genre = request.form["Genre"]

        songConn = musicDBcon()
        cursor = songConn.cursor()
        cursor.execute("UPDATE songs SET title = ?, artist = ?, genre = ?" "WHERE songID = ?", (title, artist, genre, songID))
        songConn.commit()
        songConn.close()
        return redirect(url_for("songs")) # redirect to the songs page
    return render_template("updatesongs.html", title="Update songs", SongRecord=aSongRecord)

##########################

"Add songs "

@app.route("/addsongs.html", methods=["GET", "POST"])
def addsongs():   # this is what we want to happen in case of adding songs
    if request.method == "POST":

        title = request.form["Title"]  ## we need to paste these to addsong input value with single quotes!!!!
        artist = request.form["Artist"]
        genre = request.form["Genre"]

        songConn = musicDBcon()
        cursor = songConn.cursor()
        songID = cursor.lastrowid

        cursor.execute("INSERT INTO songs VALUES(?,?,?,?)", (songID, title, artist, genre))
        songConn.commit()
        songConn.close()
        return redirect(url_for("songs")) # redirect back to the songs page after adding a song 

    return render_template("addsongs.html", title="Add Songs")



##########################
# set the routes for the contact.html
@app.route("/contact")
def contact():

 # returns the contact page in the browser when the Contact text/link is clicked on the menu
    return render_template("contact.html", title="Contact")

# set the routes for the about.html

@app.route("/about")
def about():

 # returns the about page in the browser when the about text/link is clicked on the menu
    return render_template("about.html", title="About")

# set the routes for the addsongs.html we added this up addSong and then delete this.
""" @app.route("/addsongs")
##def addsongs():

 # returns the addsongs page in the browser when the addsongs text/link is clicked on the menu
     return render_template("addsongs.html", title="Add Songs") """


# invoke / call the main class
if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=3500)   # this port will serve this host local host at the IP address of the computer