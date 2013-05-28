"""
This is the gui for the regular expression module
"""
#TODO: multi-file search (use listbox for filenames)
#TODO: re flags support
from Tkinter import *
from tkFileDialog import askopenfilename
import re

class ReGui(Tk):
    """
    Main window of the gui
    """
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.data = ''

        self.inputType = StringVar(self)
        self.inputField = Entry(self)
        self.reEntry = Text(self, width=60, height=10, wrap=NONE)
        self.reMatches = Text(self, width=60, height=10, wrap=NONE)

        Label(self, text='Input type: ').grid(row=0, column=0, sticky=W)
        OptionMenu(self, self.inputType, 'File').grid(row=0, column=1, sticky=W)

        Label(self, text='Input file: ').grid(row=1, column=0, sticky=W)
        self.inputField.grid(row=1, column=1, columnspan=2, sticky=W, ipadx=60)
        Button(self, text='Browse...', command=self.getinputfiles).grid(row=1, column=3, sticky=W)

        Label(self, text='Regular expression:').grid(row=2, column=0, columnspan=4, sticky=W)
        self.reEntry.grid(row=3, column=0, columnspan=4, sticky=W)

        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.reEntry.yview)
        self.scrollY.grid(row=3, column=4, sticky=N+S+W)

        self.scrollX = Scrollbar(self, orient=HORIZONTAL, command=self.reEntry.xview)
        self.scrollX.grid(row=4, column=0, columnspan=4, sticky=N+E+W)

        self.reEntry.config(yscrollcommand = self.scrollY.set)
        self.reEntry.config(xscrollcommand = self.scrollX.set)

        Label(self, text='Matches').grid(row=5, column=0, sticky=W)
        self.reMatches.grid(row=6, column=0, columnspan=4, sticky=W)

        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.reMatches.yview)
        self.scrollY.grid(row=6, column=4, sticky=N+S+W)

        self.scrollX = Scrollbar(self, orient=HORIZONTAL, command=self.reMatches.xview)
        self.scrollX.grid(row=7, column=0, columnspan=4, sticky=N+E+W)

        self.reMatches.config(yscrollcommand = self.scrollY.set)
        self.reMatches.config(xscrollcommand = self.scrollX.set)

        Button(self, text='Search', command=self.reSearch).grid(row=8, column=0, sticky=W)

        Button(self, text='Help', command=lambda: ReHelp()).grid(row=8, column=4, sticky=E)

        self.bind('<F1>', lambda evt: ReHelp())

        self.lift()
        self.focus()
        self.mainloop()

    def getinputfiles(self):
        """
        Asks for a filename using an open dialog and sets the text of self.inputField
        Does not erase field if Cancel is pressed
        """
        fileName = askopenfilename() # open an open file dialog, ask for the name
        if fileName == '': return # pressing Cancel returns ''
        self.inputField.delete(0, END) # empty the field
        self.inputField.insert(0, fileName)

    def loadfile(self):
        """
        Loads the file in the self.data string variable
        """
        with open(self.inputField.get(), 'r') as inputFile:
            self.data = ''.join(inputFile.readlines())

    def reSearch(self):
        """
        Applies the regualr expression to the file and shows the matches in the
        match box
        """
        self.loadfile()
        matches = re.findall(self.reEntry.get('1.0', END), self.data)
        self.reMatches.delete('1.0', END)
        if len(matches) == 0:
            self.reMatches.insert('1.0', 'No mathces.')
            return
        self.reMatches.insert('1.0', '\n'.join(matches))

class ReHelp(Toplevel):
    """
    Class for the help window
    """
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        Label(self, justify=LEFT, text="""
Regex quick ref
* - Zero or more instances of the previous regex
? - Zero or one instances of the previous regex
[abc] - Match a, b, or c
[^abc] - Match anytning but a, b, or c
^abc - Match abc at the beginnig of a line
abc$ - Match abc at the end of a line
. - Match any character except newline
For more search the web for 'python re'
""".strip()).grid(row=0, column=0, sticky=W)

        self.lift(self.master)
        self.focus()

def main():
    ReGui()
