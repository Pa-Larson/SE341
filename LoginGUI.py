from tkinter import *
import NoteListGUI
import CreateNote

global userPW                                 # The correct PW
userPW = "1234"

def loginNext(): # Removes the login screen and go to the next screen
  if inputPW.get() != userPW:                 # Verifies the input PW
      Label(screen, text = "Invalid username / password", fg = "red" ,font = ("calibri", 11)).pack()
  else:
    screen.destroy()                          # Destroys the current login screen
    NoteListGUI.scheduler(username.get())     # Goes to the Note List and brings the user name




def loginScreen(): # Displays the login screen
  # Variable for the Screen GUI
  global screen                             # Makes a screen
  screen = Tk()                             # Declares it as a Tk GUI
  screen.geometry("250x190")                # The dimensions

  # Variable for the inputed Username
  global username                           # Stores the user's name input
  global username_entry                     # Used to get input from tkinter textboxes
  username = StringVar()                    # Defines the variable as a string so we can use it
 
 # Variable for the inputed Password
  global inputPW                            # Stores user's password input
  inputPW = StringVar()                     # Defines the variable as a string so we can use it

 # A welcome prompt
  Label(screen, text = "Healthy Huskies Callback Notes \n").pack()
  
 # A request prompt for user name (Doesn't get verified)
  Label(screen, text = "Name (*)").pack()                 # Makes a input field for username          
  username_entry = Entry(screen, textvariable = username)
  username_entry.pack()

# A request prompt for user password
  Label(screen, text = "Password * ").pack()
  password_entry =  Entry(screen, textvariable = inputPW)
  password_entry.pack()

# Input text field for passward, which gets verified
  Label(screen, text = "").pack()
  Button(screen, text = "Login", width = 10, height = 1, command = loginNext).pack()


  screen.mainloop() # Loop / checks for user's update every frame.


loginScreen()                                               # Executes the login screen