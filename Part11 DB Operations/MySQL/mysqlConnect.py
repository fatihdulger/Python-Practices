import mysql.connector    # import the mysql connector

#connect to MySqlserver

#conn = mysql.connector.connect(host ="localhost", user="root", password="M31!h!mo4o415") #>>>> this connects to mysql with no specifying database name
conn = mysql.connector.connect(host ="localhost", database="c10musicapp", user="root", password="M31!h!mo4o415") # this connects to certain database




if conn.is_connected():
    print("connected to MySQL")
else:
    print("Connection failed!")

cursor = conn.cursor(prepared = True)

#create a database

# cursor.execute("CREATE DATABASE c10musicApp")  
# we used this command without mysql workbench we created database then commented this out!!!
# we used this along with above database connection then switch to new database we created thru commit and execution.