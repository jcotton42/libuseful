"""
This is the gui for the sorts module
"""
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror, showinfo
import os, csv, sys

class SortsGui(Tk):
    """
    Main window of application
    """
    def __init__(self, screenName=None, baseName=None, className='Tk',
                 useTk=1, sync=0, use=None):
        """
        Constructs a new main window for the sorts gui
        for info on paramaters see the docs for Tk.__init__
        """
        Tk.__init__(self, screenName, baseName, className,
                 useTk, sync, use)

        self.title("Sorts")

        self.data = [] # the data to sort
        # Create fields
        self.outputType = StringVar(self) # where to put the data
        self.inputField = Entry(self) # filename for input file
        self.sortType = StringVar(self) # which sort to use
        self.outputField = Entry(self) # filename for output file
        self.sortTypes = dict() # holds the names and sort methods

        # Get sort types - this is a kludge, see if there's a better way
        old_dir = os.getcwd()
        os.chdir(os.path.join(os.path.dirname(sys.argv[0]), os.path.dirname(__file__))) # Change to root package directory needed for __import__
        for name in os.listdir('.'): # get the files and folders in the current direcoty
            if name.endswith('.py'): # python files
                modName = name[0:-3] # strip .py suffix
                if modName in ['__init__', '__main__', 'gui']: continue # thses files will not have any algorithims
                mod = __import__(modName, globals(), locals(), [], -1) # see /gui.py for explanaton
                if '_sort' in mod.__dict__ and isinstance(mod._sort, FunctionType): # if _sort exists and is callable
                    sortName = ''
                    if '_sort_name' in mod.__dict__: sortName = mod._sort_name
                    else: sortName = modName

                    self.sortTypes[sortName] = mod._sort

        os.chdir(old_dir)
        if len(list(self.sortTypes.keys())) == 0:
            raise NotImplementedError("No sort definitions found")
            # NotImplementedError used because no sorts were implemented

        # Layout elemetns

        Label(self, text ='Sort type: ').grid(row=0, column=0, sticky=NW)
        OptionMenu(
                self, self.sortType, *list(self.sortTypes.keys())
            ).grid(row=0, column=1, sticky=NW)

        Label(self, text='Input file: ').grid(row=1, column=0, sticky=NW)
        self.inputField.grid(row=1, column=1, sticky=NW)
        Button(self, text='Browse...', command=self.getinputfile).grid(row=1, column=2, sticky=NW)

        Label(self, text='Output file: ').grid(row=2, column=0, sticky=NW)
        self.outputField.grid(row=2, column=1, sticky=NW)
        Button(self, text='Browse...', command=self.getoutputfile).grid(row=2, column=2, sticky=NW)

        Button(self, text='Sort', command=self.sortdata).grid(row=3, column=0, sticky=NW)

        self.mainloop()

    def loadfile(self, csvData = None, **fmtparams):
        """
        Load the contents of file into the self.data variable

        :param csvData: Whether or not the input data is in CSV format
        :type csvData: bool
        :param fmtparams: Format paramaters for the csv reader
        :type fmtparams: dict
        """
        fileName = self.inputField.get()
        if fileName.endswith('.csv') and csvData is None: csvData = True
        with open(fileName, 'r') as inputFile:
            self.data = []
            if csvData:
                for row in csv.reader(inputFile, **fmtparams):
                    list(map(self.data.append, row))
            else:
                for line in inputFile.readlines():
                    self.data.append(line)

    def savefile(self, csvData = None, **fmtparams):
        """
        Saves the sorted list/dictionary to a file

        :param csvData: Whether or not the output data should be saved in CSV \
        format
        :type csvData: bool
        :param fmtparams: Format paramaters for the csv writer
        :type fmtparams: dict
        """
        fileName = self.outputField.get()
        if fileName.endswith('.csv') and csvData is None: csvData = True
        with open(fileName, 'w') as outputFile:
            if csvData:
                tmp = csv.writer(outputFile, **fmtparams)
                tmp.writerow(self.data)
            else:
                list(map(outputFile.write, self.data))

    def getinputfile(self):
        """
        Get the filename of the input file with a dialog
        """
        fileName = askopenfilename()
        if fileName == '': return # '' is returned if cancel is clicked
        self.inputField.delete(0, END)
        self.inputField.insert(0, fileName)

    def getoutputfile(self):
        """
        Get the filename of the output file with a dialog
        """
        fileName = asksaveasfilename()
        if fileName == '': return # '' is returned if cancel is clicked
        self.outputField.delete(0, END)
        self.outputField.insert(0, fileName)

    def sortdata(self):
        """
        Preform the actual sorting
        """
        # Check the fields
        # This is where I wish ptyhon had a switch statment, oh well
        if self.sortType.get() == '':
            showerror('Missing sort type', 'Please specify a sort type')
            return
        if self.inputField.get() == '':
            showerror('Missing input filename', 'Please specify an input filename')
            return
        if self.outputField.get() == '':
            showerror('Missing input filename', 'Please specify an output filename')
            return
        # If we reach here all the fields are good
        self.loadfile()

        self.data = self.sortTypes[self.sortType.get()](self.data)

        self.savefile()

def main():
    SortsGui()
