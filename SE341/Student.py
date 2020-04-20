class Student:
  def __init__(self,sID, fname, lname, addr, pnum):
        self.sID = int(sID)              # Required *
        self.firstname = fname     # Optional
        self.lastname = lname  # Optional
        self.address  = addr     # Optional
        self.phonenumber  = pnum      #Employee who created the note
                                # Required later / Automated / Get from login