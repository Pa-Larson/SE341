import tkinter as tk
import NoteListGUI
import pymysql.cursors

def createGlobals():

    ##entries will keep track of Tkinter entry objects. Can use entry.get() to fetch text held in an entry box
    global entries
    entries = []

    ##fields will be referenced to create the form
    global fields
    fields = ('Student ID', 'For Who', 'Reason', 'Notes', 'Employee ID')

## returns database connection object
def getDatabaseConnection():
    database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                               user="admin",
                               password="se3412020",
                               db="callbackDb",
                               charset="latin1",
                               cursorclass=pymysql.cursors.DictCursor)
    return database


def addNoteToDB():
    database = getDatabaseConnection()
    cursor = database.cursor()

    #use getNoteID() and add it to entries list to be used to add to database. The order of the entries in sqlFormula is important because it lines up with the order of tkinter entries
    entries.append(getNoteID())

    sqlFormula = "INSERT INTO studentNotes (student_id, for_who, reason, note, Employee_ID,Note_ID) VALUES(%s, %s, %s, %s, %s, %s)"
    noteValues = (entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5])


    # Use loop below for debugging
    #for n in noteValues:
    #    print("The value in notevalues is ", n)

    emp_exists = checkEmployeeID(entries[4].get())
    student_exists = checkStudentID(entries[0].get())

    #Use print statements for debugging
    #print("Student exists: ", student_exists)
    #print("Employee exists: ", emp_exists)

    if(student_exists & emp_exists):
        try:
            cursor.execute(sqlFormula, noteValues)
            database.commit()
            print("Note added successfully")
        except:
            print("Unable to add note")


        finally:
            database.close()

    if(not student_exists):
        print("Unable to add note, student doesn't exist")
    if(not emp_exists):
        print("Unable to add note, employee doesn't exist")


def makeform(root):
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        input = ent
        entries.append(input)


def getEntriesList():
    entryList = []
    for entry in entries:
        entryList.append(entry)
    return entryList


def createNotePage():
    root = tk.Tk()                              # Makes the screen
    root.title("Create Callback Note")          # Changes the title of window
    root.geometry("300x300")                    # Default screen size
    makeform(root)                              # Makes the entry forms

    entries = getEntriesList()

    # Use loop below for debugging
    #for e in entries:
    #   print("The value of the entry is ", e)

    b1 = tk.Button(root, text='   Go Back   ')
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='    Clear    ')
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text=' Create Note', command=(addNoteToDB))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

# Returns the noteID to be used in creating a new note and adding it to database
def getNoteID():
    database = getDatabaseConnection()
    cursor = database.cursor()
    id=1

    try:

        cursor.execute("SELECT Note_ID FROM studentNotes")
        noteIDs = cursor.fetchall()
    except:
        print("Exception: Unable to fetch note ids")
    finally:
        database.close()


    for i in noteIDs:
        if int(i['Note_ID']) > id:
            id = int(i['Note_ID'])
    return id + 1

#Checks if student exists in database
def checkStudentID(s_id):
    exists = False
    database = getDatabaseConnection()
    cursor = database.cursor()

    try:
        with database.cursor() as cursor:
            cursor.execute("SELECT student_id FROM studentNotes")
            studentIDs = cursor.fetchall()
    except:
        print("Unable to fetch studentIDs")
    finally:
        database.close()


    for s in studentIDs:
        if int(s['student_id']) == int(s_id):
            exists = True
    return exists

#Checks if employee exists in database
def checkEmployeeID(e_id):
    exists = False
    database = getDatabaseConnection()
    cursor = database.cursor()

    try:
        with database.cursor() as cursor:
            cursor.execute("SELECT Employee_ID FROM Employee")
            empIDs = cursor.fetchall()
    except:
        print("Unable to fetch employee IDs")
    finally:
        database.close()


    for e in empIDs:
        if int(e['Employee_ID']) == int(e_id):
            exists = True
            break
    return exists



createGlobals()
#createNotePage()

