from guizero import *
import sqlite3

# create an instance object called app from the App class/template
app = App(title="GUI Database", layout="grid", height=600, width=550)
app.bg = "#adeecf"


"subroutine to open/load add data and display data gui "


def addDataGui():
    dApp.show()
    app.hide()


def displayDataGui():
    cApp.show()
    app.hide()


dApp = Window(app, title="Add Data App", layout="grid")
dApp.bg = "#30316e"
dApp.hide()


cApp = Window(app, title="Display Data App", layout="auto")   # this could be grid too instead of auto!!!!
cApp.bg = "#ff4646"
cApp.hide()

btnAddDataApp = PushButton(
    dApp, text="Submit", width=15, grid=[1, 5]
)  #  command=AddDataToDB,
"Buttons on first main window"
btnLoadAdd = PushButton(app, command=addDataGui, text="Add Data", width=15, grid=[0, 0])
btnLoadDisplay = PushButton(
    app, command=displayDataGui, text="Display Data", width=15, grid=[0, 1]
)


#####################
# ask for user input

fnameT = Text(dApp, text="Enter firstname:", width=30, grid=[0, 2])
fnameT.text_color = "#fafafa"
fnameB = TextBox(dApp, text="", width=20, grid=[1, 2])
lnameT = Text(dApp, text="Enter Lastname:", width=30, grid=[0, 3])
lnameT.text_color = "#fafafa"
lnameB = TextBox(dApp, text="", width=20, grid=[1, 3])
emailT = Text(dApp, text="Enter Email:", width=30, grid=[0, 4])
emailT.text_color = "#fafafa"
emailB = TextBox(dApp, text="", width=20, grid=[1, 4])

conn = sqlite3.connect("Part13 GUI_DB/c10Sqlite.db")
cursor = conn.cursor()

"add data to database"

def addMember():

    # create empty list
    members = []
    # add data entered
    fname = fnameB.value
    lname = lnameB.value
    email = emailB.value

    # listName.append(dataCapyired)
    members.append(fname)
    members.append(lname)
    members.append(email)

    # insert data to members table
    cursor.execute("INSERT INTO members VALUES(NULL, ?,?,?)", members)
    conn.commit()
    print(f"{fname} added to members table")

btnAddDataApp = PushButton(
    dApp, text ="Submit", command=addMember, width=15, grid=[1, 5]

) # command=AddDatatoDB

# retrieve data from database

def displayRecords():
    myList = [] ## we will append to this list
    cursor.execute("SELECT * FROM members")
    row = cursor.fetchall()
    for record in row:
        myList.append(record)
        dataInList.append(record) # append the data from the members tbl to the ListBox

        print(record)
        #print(f"This is a List\n{myList}")


# button to call/invoke the displayRecords subroutine
btnDisplayData = PushButton(cApp, text="Read Members", command=displayRecords, align="right", width="fill", grid=[0, 1])
btnDisplayData.text_size = 40
btnDisplayData.text_color = "#f2f2f2"

# Display data from databse inside a list
dataInList = ListBox(cApp, items=[], align="right", height="fill", width="fill" )  ##grid=[2, 3] this list is to show data in DB
dataInList.text_size = 24
dataInList.text_color = "#f2f2f2"
app.display()

#   # time.sleep(3)

# cursor.execute("SELECT * FROM members")
#     row = cursor.fetchall()
#     for record in row:
#         print(record)

# def AddNums(pNum1,pNum2):
#     total = pNum1 + pNum2
#     return total

# AddNums()

# num1 = num1.value
# btnMyAdd = PushButton(cApp, text="Add", command=AddNums, args=)

# so we can pass arguments to btn s