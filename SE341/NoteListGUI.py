from tkinter import *
import NoteClass


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
    
    # Populates the Listbox with Callback Notes
    for i in range(len(listSJF)):                                               #Initializes the listbox
        nextLB.insert("end", getOrder(i, listSJF))


    makeScrollBar(screen)

    screen.mainloop() 