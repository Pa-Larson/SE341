from tkinter import *

def main():
    print("yes")

class callNote:
  def __init__(self, Fname, Lname, sID, pNum, addr, reason, notes, forWho):
        self.Fname = Fname          # Required *
        self.LName = Lname          # Required *
        self.sID = sID              # Required *
        self.pNum = pNum            # Required *
        self.addr = addr            # Optional
        self.reason = reason        # Optional
        self.notes = notes          # Optional
        self.forWho = forWho        # Optional
        self.dateMade = "Get from device"       # Required Now / Automated / Get from device
        self.dateComp = "Get from device"       # Required later / Automated / Get from device
        self.madeWho = "Get from login"         # Required Now / Automated / Get from login
        self.compWho = "Get from login"         # Required later / Automated / Get from login

#============================================================================================  
#Add Shortest Job First: adds an order to the list of orders in ascending order of burst times
#Preconditions: A valid order (Order), and a list of orders (listSJF)
#Post: A new order has been added to the list of orders in ascending total burst time.
#============================================================================================  
def addCallNote(CallNote, listCallNote = []):
    listCallNote.insert(CallNote)                 

#============================================================================================  
#Display Shortest Job First: Displays all the orders in queue.
#Preconditions: list of orders (listSJF)
#Post: Displays the Orders in their respective sequence and their attributes
#============================================================================================  
def displayNotes(listCallNote = []):
    i = 0
    while i < len(listCallNote):                             #Goes through the whole list
        print(i+1, 
        " Fname:", listCallNote[i].Fname,      
        "\t Lname:", listCallNote[i].Lname,
        "\t Star ID:", listCallNote[i].sID,
        "\t Phone:", listCallNote[i].pNum,
        "\t Address:", listCallNote[i].addr,
        "\t Reason:", listCallNote[i].reason,
        "\t Notes:", listCallNote[i].notes,
        "\t For Who:", listCallNote[i].forWho,
        "\t Date Made:", listCallNote[i].dateMade,
        "\t Made By:", listCallNote[i].madeWho,
        "\t Date Completed:", listCallNote[i].dateComp,
        "\t Completed by:", listCallNote[i].compWho)
        i += 1                                          #Next order


#============================================================================================
# Main: A simple demonstration
#============================================================================================
listCallNote = []                    #Used to store the user's inputted orders.  




displayNotes(listCallNote)