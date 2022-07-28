import sqlite3 # import sqlite module/library

"Create a variable 'conn' and pass sqlite connect method to it"

conn = sqlite3.connect(r"PYTHON\Part11 DB Operations\SQLite\c10Sqlite.db")

"cursor method iterates thrugh database/tables"
cursor = conn.cursor()
