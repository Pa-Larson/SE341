from tkinter import *

def scheduler(username):
    global screen
    screen = Tk() 
    screen.geometry("350x525")

    Label(screen, text = username, font = ("calibri", 11), height = 2).pack()
 
    screen.mainloop() 