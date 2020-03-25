from tkinter import *
import pymysql.cursors


def listToString(list):
    str1 = ""
    for i in list:
        str1 += str(i)

    return str1


def viewNote(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))


def scheduler(username):
    # Makes the screen
    global screen                       # Makes the screen variable
    screen = Tk()                       # Declares it as a GUI
    screen.geometry("350x525")          # Declears the deminsion

    # Displays the user name (moreso for debugging)
    Label(screen, text = "welcome " + username, font = ("calibri", 11), height = 2).pack()
    
    #Makes the Listbox and it's scroll bar (Can't put this into a def)
    scrollbar = Scrollbar(screen, orient="vertical")                                    # Scroll bar initalization
    nextLB = Listbox(screen, width=50, height=10, yscrollcommand=scrollbar.set)         # List box size + initalization w/ scroll bar
    processLB = Listbox(screen, width=50, height=10, yscrollcommand=scrollbar.set)      # List box size + initalization w/ scroll bar
    scrollbar.config(command=nextLB.yview)                                              # Makes the list box scrollable
    scrollbar.pack(side="right", fill="y")                                              # tells where the scroll bar should go

    # Get /declare the Callback Notes from the Database
    database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                               user="admin",
                               password="se3412020",
                               db="callbackDb",
                               charset="latin1",
                               cursorclass=pymysql.cursors.DictCursor)

    try:
        with database.cursor() as cursor:
            cursor.execute("SELECT * FROM studentNotes")
            notes = cursor.fetchall()
    finally:
        database.close()

    nextLB.insert(END, "Student ID\tName\t\t\tStatus")
    for row in notes:
        status = str(row["status"])
        if status == "1":
            status = "Open"
        else:
            status = "Closed"

        rowList = [str(row["student_id"]), "   \t", str(row["first_name"]),
                   " ", str(row["last_name"]), " \t", status]
        rowString = listToString(rowList)
        nextLB.insert(END, rowString)

    nextLB.pack()
    nextLB.bind('<Double-Button>', viewNote)

    screen.mainloop()
