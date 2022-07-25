from mysqlConnect import *

def readMembers():
    cursor.execute("SELECT * FROM members")
    row = cursor.fetchall()
    for record in row:
        print(record)

readMembers()