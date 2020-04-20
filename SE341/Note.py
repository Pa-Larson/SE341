class callNote:
  def __init__(self, sID, forWho, reason, notes, empID):
        self.sID = int(sID)              # Required *
        self.reason = reason      # Optional
        self.note = notes       # Optional
        self.forWho = forWho        # Optional
        self.eID = int(empID)          #Employee who created the note
        self.createdDate = "Get from device"       # Required Now / Automated / Get from device
        self.finishedDate = "Get from device"       # Required later / Automated / Get from device
        self.status = 0         # Required Now / Automated / Get from login
        self.noteID = 0        # Required later / Automated / Get from login

