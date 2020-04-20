import pymysql.cursors
import Note
from tkinter import *
import Student

class NoteList:


    def addToDB(self,vals):
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        # Gets a new note ID
        uniqueID = self.newNoteID()
        #note = Note.callNote(entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get())
        for v in vals:
            print(v)
        note = Note.callNote(vals[0], vals[1], vals[2], vals[3], vals[4])
        note.noteID = uniqueID
        print("S id is " + str(note.sID))
        print("E id is " + str(note.eID))
        print("Note id is " + str(note.noteID))
        print("For who is " + note.forWho)
        print("Reason is " + note.reason)
        print("notes are " + note.note)
        
        sExists = self.studentExists(note.sID)
        eExists = self.empExists(note.eID)
        print("Student exists: ", sExists)
        print("Employee exists: ",  eExists)
        sqlFormula = sqlFormula = "INSERT INTO studentNotes (student_id, for_who, reason, note, Employee_ID,Note_ID) VALUES(%s, %s, %s, %s, %s, %s)"
        noteValues = (note.sID, note.forWho, note.reason, note.note, note.eID, note.noteID)


        if(sExists & eExists):
            try:
                cursor.execute(sqlFormula, noteValues)
                database.commit()
                #Label(screen, text="Note added successfully!\n", fg='green',font=('arial', 12, 'bold')).pack(anchor='w')
                print("Note added successfully")
            except:
                print("Error: Unable to add note to database. Check inside NoteList.addToDB()")
            finally:
                database.close()
        else:
            screen = Tk()  # Declares it as a Tk GUI
            screen.geometry("350x100")  # The dimensions
            if(not sExists):
                Label(screen, text="Error: Invalid student ID, please try again!\n", fg = 'red', font = ('arial',12,'bold')).pack(anchor = 'w')
            if(not eExists):
                Label(screen, text="Error: Invalid employee ID, please try again!\n", fg='red', font=('arial', 12,'bold')).pack(anchor='w')







    def markAsComplete(self, note):
        print("Create this")

    def getAllNotes(self):
        allNotes = []

        database = self.getDatabaseConnection()
        cursor = database.cursor()
        try:
            cursor.execute("SELECT * FROM studentNotes")
            notes = cursor.fetchall()
        except:
            print("Error:  Unable to fetch notes! Check inside NoteList > getAllNotes() ")
        finally:
            database.close()

        for n in notes:
            note = Note.callNote(n["student_id"], n["for_who"], n["reason"], n["note"], n["Employee_ID"])
            note.noteID = n["Note_ID"]
            allNotes.append(note)
        
        return allNotes
    
    def studentExists(self,sID):
        exists = False
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        
        try:
            cursor.execute("SELECT student_id FROM Student")
            studentIDs = cursor.fetchall()
        except:
            print("unable to get check if students exist")
        finally:
            database.close()

        for s in studentIDs:
            if int(s['student_id']) == int(sID):
                exists = True
        return exists
    
    def empExists(self,eID):
        exists = False
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        try:
            cursor.execute("SELECT Employee_ID FROM Employee")
            empIDs = cursor.fetchall()
        except:
            print("unable to get check if employee exists")
        finally:
            database.close()

        for e in empIDs:
            if int(e['Employee_ID']) == int(eID):
                exists = True
        return exists



    def getNote(self, noteID):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        print("The noteid inside getNote is ", noteID)
        print("The noteID type is ", type(noteID))

        #try:
        cursor.execute("SELECT * FROM studentNotes")
        notevalues = cursor.fetchall()
        print(notevalues)
        print(type(notevalues[1]))
        #except:
        #    print("Error: Unable to retrieve note from database. Check inside NoteList.getNote(noteID)")
        #finally:
        #    database.close()

        #Loop through note rows until one is found with the given noteID, then make a note object using thsoe values
        for n in notevalues:
            if(int(n['Note_ID']) == int(noteID)):
                theNote = Note.callNote(n['student_id'], n['for_who'], n['reason'], n['note'], n['Employee_ID'])
                theNote.noteID = n['Note_ID']
        
        try:
            return theNote
        except:
            print("Error: Unable to return note, check inside getNote()")





    def getDatabaseConnection(self):
        database = pymysql.connect(host="callbackinstance.clmbtzcmhna9.us-east-2.rds.amazonaws.com",
                                   user="admin",
                                   password="se3412020",
                                   db="callbackDb",
                                   charset="latin1",
                                   cursorclass=pymysql.cursors.DictCursor)
        return database

    def newNoteID(self):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        id = 1

        try:
            cursor.execute("SELECT Note_ID FROM studentNotes")
            noteIDs = cursor.fetchall()
        except:
            print("Exception: Unable to fetch note ids")
        finally:
            database.close()

        for i in noteIDs:
            if int(i['Note_ID']) > int(id):
                (id) = int(i['Note_ID'])
        return id+1
    
    def getStudentInfo(self, sID):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        sID = int(sID)
        
        try:
            cursor.execute("SELECT * FROM Student")
            students = cursor.fetchall()
        except:
            print("Error: Unable to fetch student from DB. Check inside getStudentInfo()")
        finally:
            database.close()
        
        for s in students:
            if int(s['Student_ID']) == sID:
                theStudent = Student.Student(sID, fname= s['First_Name'], lname = s['Last_Name'], addr = s['Address'], pnum = s['Phone_Number'])
        try:
            return theStudent
        except:
            print("Error: Student not found exception. Check inside getStudentInfo()")
        