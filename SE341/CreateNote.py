import tkinter as tk

fields = ('First Name', 'Last Name', 'Student ID', 'Phone Number', 'Address', 'For Who', 'Reason', 'Notes')

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()                              # Makes the screen
    root.title("Create Callback Note")          # Changes the title of window
    root.geometry("300x300")                    # Default screen size
    ent = makeform(root, fields)                # Makes the entry forms

    b1 = tk.Button(root, text='   Go Back   ')
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='    Clear    ')
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text=' Create Note' )
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()