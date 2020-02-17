from tkinter import *
import NoteListGUI

def loginNext():    
  screen.destroy()                          # Destroys the current login screen
  NoteListGUI.scheduler(username.get())     # Goes to the Note List and brings the user name

def loginScreen():
  global screen                             # Makes a screen
  screen = Tk()
  screen.geometry("300x250")

  global username                           # Stores the users input
  global username_entry                     # Used to get input from tkinter textboxes
  username = StringVar()                    # Defines the variable as a string so we can use it
 
  Label(screen, text = "Healthy Huskies Callback Notes \n").pack()         
  
  Label(screen, text = "What is your name?").pack()                 # Makes a input field for username          
  username_entry = Entry(screen, textvariable = username)
  username_entry.pack()

  Label(screen, text = "").pack()                                   #Makes a login button
  Button(screen, text = "Login", width = 10, height = 1, command = loginNext).pack()

  screen.mainloop()
 
loginScreen()                                               # Executes the login screen