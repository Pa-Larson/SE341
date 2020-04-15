from tkinter import *
import pymysql.cursors
import NoteClass
import CreateNote


def gotoCreateNote():
    screen.destroy()
    CreateNote.createNotePage()


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
            noteIDs = cursor.fetchall()
    finally:
        database.close()

    nextLB.insert(END, "Note ID")
    for row in noteIDs:
        nextLB.insert(END, row["Note_ID"])

    nextLB.pack()

    global rmvID
    global IDtoRemove
    rmvID = StringVar()

    ## Remove notes
    Label(screen,pady = 50, text="Enter ID to remove \n").pack()
    IDtoRemove = Entry(screen, textvariable=rmvID)
    IDtoRemove.pack()
    Button(screen, text="Remove from DB", width=20, height=2).pack()

    ##Button to go to create note page
    Label(screen, text="").pack()
    Button(screen, text="Create Note", width=10, height=1, command=gotoCreateNote).pack()


    #makeScrollBar(screen)

    screen.mainloop()


##This function is not usable right now. The GUI shows noteID rather than studentID, and this function uses studentID to query for which tuple to delete
## We will change this to a function that marks a note as complete rather than deleting it, or perhaps we can keep this in addition to a mark as complete functoin
def removeNoteFromDB():
    database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                               user="admin",
                               password="se3412020",
                               db="callbackDb",
                               charset="latin1",
                               cursorclass=pymysql.cursors.DictCursor)



    cursor = database.cursor()
    ##print("The id passed to function is ", rmvID.get())
    tempID = rmvID.get()
    try:
        cursor.execute("DELETE from studentNotes WHERE student_id =" + IDtoRemove.get())
        database.commit()
        print("Entry deleted")
        refreshList()

    except:
        print("Unable to delete the entry with the given student id")


## This needs to be fixed, the way it is right now it creates a new box underneath everything rather than clearing it
def refreshList():
    scrollbar = Scrollbar(screen, orient="vertical")  # Scroll bar initalization
    nextLB = Listbox(screen, width=50, height=10,
                     yscrollcommand=scrollbar.set)  # List box size + initalization w/ scroll bar
    processLB = Listbox(screen, width=50, height=10,
                        yscrollcommand=scrollbar.set)  # List box size + initalization w/ scroll bar
    scrollbar.config(command=nextLB.yview)  # Makes the list box scrollable
    scrollbar.pack(side="right", fill="y")  # tells where the scroll bar should go

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

    nextLB.insert(END, "Student ID")
    for row in notes:
        nextLB.insert(END, row["student_id"])

    nextLB.pack()

def addStudent():
    print("Enter Student ID")
    sID = int(input())
    print("Enter first name")
    fname = input()
    print("Enter last name")
    lname = input()
    print("Enter phone number")
    pnum = input()
    print("Enter address")
    address = input()

    database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                               user="admin",
                               password="se3412020",
                               db="callbackDb",
                               charset="latin1",
                               cursorclass=pymysql.cursors.DictCursor)

    cursor = database.cursor()

    ##try:
    formula = "INSERT INTO Student (Student_ID, First_Name, Last_Name, Address, Phone_Number) VALUES (%s, %s, %s, %s, %s)"
    values = (sID, fname, lname, pnum, address)
    cursor.execute(formula, values)
    database.commit()
    print("Student added")
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    for row in students:
        print("The students contained in DB are: ")
        print(row)





def addEmployee():
    print("Enter the ID of the employee to add")
    empID = input()

    print("Enter the first name of employee")
    empFname = input()

    print("Enter the last name of the employee")
    empLname = input()


    database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                               user="admin",
                               password="se3412020",
                               db="callbackDb",
                               charset="latin1",
                               cursorclass=pymysql.cursors.DictCursor)

    cursor = database.cursor()

    ##try:
    formula = "INSERT INTO Employee (Employee_ID, Employee_Lname, Employee_Fname) VALUES (%s, %s, %s)"
    values = (empID, empFname, empLname)
    cursor.execute(formula, values)
    database.commit()
    print("Employee added")
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()
    for row in employees:
        print("The employees contained in the DB: ")
        print(row)

## THESE FUNCTIONS CAN BE USED TO POPULATE THE STUDENT AND EMPLOYEE TABLES. For the purposes of this assignment, we don't need to add GUI for this functionality
## Just delete comments below for the functions and run NoteListGUI.py
#addStudent()
#addEmployee()