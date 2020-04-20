from tkinter import *
import pymysql.cursors
import Note
import NoteList
from functools import partial
## login screen
#global username
#username = StringVar()



def loginScreen():
    # Variable for the Screen GUI
    userPW = "1234"

    #global screen  # Makes a screen
    screen = Tk()  # Declares it as a Tk GUI
    screen.geometry("300x300")  # The dimensions

    # Variable for the inputed Username
    global username  # Stores the user's name input
    global username_entry  # Used to get input from tkinter textboxes
    username = StringVar()  # Defines the variable as a string so we can use it

    # Variable for the inputed Password
    global inputPW  # Stores user's password input
    inputPW = StringVar()  # Defines the variable as a string so we can use it

    # A welcome prompt
    Label(screen, text="Healthy Huskies Callback Notes \n").pack()

    # A request prompt for user name (Doesn't get verified)
    Label(screen, text="Name").pack()  # Makes a input field for username
    username_entry = Entry(screen, textvariable=username)
    username_entry.pack()

    # A request prompt for user password
    Label(screen, text="Password").pack()
    password_entry = Entry(screen, textvariable=inputPW)
    password_entry.pack()
    pwEntry = password_entry.get()



    # Input text field for passward, which gets verified
    Label(screen, text="").pack()
    Button(screen, text="Login", width=10, height=1, command=partial(loginButtonClicked,password_entry,userPW,screen,username_entry)).pack()

    screen.mainloop()  # Loop / checks for user's update every frame.

def loginButtonClicked(PwEntryObject, userPW, screen,usernameEntryObject):
    if PwEntryObject.get() == userPW:
        #screen.destroy()
        #username = usernameEntryObject.get()
        mainMenu(screen)
    else:
        Label(screen, text="Invalid username / password", fg="red", font=("calibri", 11)).pack()
        return


## Main menu
def mainMenu(root):
    root.destroy()


    #notelist = NoteList.NoteList()
    notes = notelist.getAllNotes()



    screen = Tk()  # Declares it as a Tk GUI
    screen.geometry("600x500")  # The dimensions

    ##Create listbox add all note entries to it
    global listbox
    listbox = Listbox(screen, borderwidth=5,font = 'arial', relief = 'groove', selectbackground = 'lightgrey', height = 12  )

    firstline = formatText("STUDENT NAME", "STUDENT ID", "NOTE ID")
    #listbox.insert(END, firstline)
    for n in notes:
        theStudent = notelist.getStudentInfo(n.sID)
        studentName = theStudent.firstname
        textline = 'Student name: ' + str(studentName) +    '        Student ID: ' +   str(n.sID) + '              Note ID: ' + str(n.noteID)
        #textline = formatText(studentName, str(n.sID), str(n.noteID))
        listbox.insert(END, textline)

    Label(screen, text="Select the note you would like to view", fg="black", font=("calibri", 14)).pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="                 " + firstline, fg="black", font=("calibri", 12)).pack(anchor='n')
    listbox.pack(anchor='n')
    listbox.config(width=60)
    Label(screen, text=" ").pack(anchor='n')
    Label(screen, text=" ").pack(anchor='n')

    ##Button when pressed will fetch the anchor, retrieve Note ID stored in that line, and then go to view note screen
    Button(screen, text= "View selected note", width=20,height =1, pady=5,command = partial(getAnchor,screen)).pack(anchor='n')
    Label(screen, text=" ").pack(anchor='n')
    Button(screen, text="Create new note", width=20, height=1, pady=5,padx = 2, command=partial(createNote,screen)).pack(anchor='n')




    line = listbox.get(ANCHOR)
    print("The line contains: ",line)
    screen.update_idletasks()

    screen.mainloop()

def formatText(StudentName, sID, nID):
    s = "                                                                                                                   "
    s = s[:20] + StudentName + s[20:]
    s = s[:40] + sID + s[40:]
    s = s[:70] + nID + s[70:]
    print(s);

    name1 = "Bob Stein"
    name2 = "Noneya Business"
    date1 = "11/22/3333"
    date2 = "2/1/4444"
    comp1 = "Yes"
    comp2 = "No"
    return(s)
    format(name1, date1, comp1)
    format(name2, date2, comp2)

def getAnchor(root):

    line = listbox.get(ANCHOR)
    root.destroy()
    keyword = 'Note ID: '
    noteID = line.partition(keyword)[2]
    noteID = int(noteID)


    viewNote(noteID)

def createNote(root):
    global entries
    entries = []

    root.destroy()
    screen = Tk()  # Declares it as a Tk GUI
    screen.geometry("400x250")  # The dimensions
    fields = ('Student ID', 'For Who', 'Reason', 'Notes', 'Employee ID')
    for field in fields:
        row = Frame(screen)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)

    b2 = Button(screen, text=' Create Note', command=processEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(screen, text='    Clear    ', command = clearEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b1 = Button(screen, text='   Go Back   ', command = partial(mainMenu, screen)).pack(side=RIGHT, padx=5, pady=5)



    screen.mainloop()

# Retrieve the values contained in Tkinter entries and attempt to add them to DB
def processEntries():
    vals = []
    #clearEntries()
    for e in entries:
        vals.append(e.get())
    return notelist.addToDB(vals)

def clearEntries():
    for e in entries:
        e.delete(0,END)

## View note page
def viewNote(noteID):


    #root.destroy()
    screen = Tk()  # Declares it as a Tk GUI
    screen.geometry("500x500")  # The dimensions

    theNote = notelist.getNote(noteID)
    print("The note is: ", theNote.sID, " ", theNote.reason)
    theStudent = notelist.getStudentInfo(theNote.sID)

    Label(screen, font=('arial',14,'bold'), pady=30, text="Student note details").pack(anchor='n')

    listbox = Listbox(screen, borderwidth=5,fg = 'black', font='arial', relief='groove', selectbackground='lightgrey', height=12,width=45)
    listbox.insert(END, "Student first name: " + theStudent.firstname)
    listbox.insert(END, "Student last: " + theStudent.lastname)
    listbox.insert(END, "Student ID: " + str(theStudent.sID))
    listbox.insert(END, "Student phone: " + str(theStudent.phonenumber))
    listbox.insert(END, "Student address: " + theStudent.address)
    listbox.insert(END, "Note ID: " + theNote.noteID)
    listbox.insert(END, "Reason for note: " + theNote.reason)
    listbox.insert(END, "Additional notes: " + theNote.note)
    listbox.insert(END, "Note is for: " + theNote.forWho)
    listbox.insert(END, "Note made by: " )
    listbox.insert(END, "Employee ID: " + str(theNote.eID))
    listbox.insert(END, "Date created: ")
    listbox.insert(END, "Date completed: ")
    listbox.insert(END, "Status: ")

    listbox.pack(anchor='n')



    b1 = Button(screen, text='   Go Back   ',command = partial(mainMenu, screen))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(screen, text='    Mark as complete    ')
    b2.pack(side=LEFT, padx=5, pady=5)




##Create global variables
def createGlobals():
    global entries
    entries = []
    global username
    global notelist
    notelist = NoteList.NoteList()


createGlobals()
loginScreen()



