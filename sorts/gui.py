"""
This is the gui for the sorts module
"""
from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename
from tkMessageBox import showerror, showinfo
import os, csv

class SortsGui(Tk):
    """
    Main window of application
    """
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.data = None # the data to sort
        # Create fields
        self.inputType = StringVar(self) # type of data and where to take it from
        self.outputType = StringVar(self) # where to put the data
        self.inputField = Entry(self) # filename for input file
        self.pivotValue = Entry(self) # pivot value for matrix sort
        self.sortType = StringVar(self) # which sort to use
        self.outputField = Entry(self) # filename for output file
        self.sortTypes = dict() # holds the names and sort methods

        # Get sort types - this is a kludge, see if there's a better way
        old_dir = os.getcwd()
        os.chdir(os.path.dirname(__file__)) # Change to root package directory needed for __import__

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

        # Layout elemetns

        Label(self, text ='Sort type: ').grid(row=0, column=0, sticky=W)
        OptionMenu(self, self.sortType, self.sortTypes.keys()[0], *self.sortTypes.keys()[1:]).grid(row=0, column=1, sticky=W)

        Label(self, text='Input type: ').grid(row=1, column=0, sticky=W)
        OptionMenu(self, self.inputType, 'List', 'Dictionary').grid(row=1, column=1, sticky=W)

        Label(self, text='Output type: ').grid(row=2, column=0, sticky=W)
        OptionMenu(self, self.outputType, 'File').grid(row=2, column=1, sticky=W)

        Label(self, text='Input file: ').grid(row=3, column=0, sticky=W)
        self.inputField.grid(row=3, column=1, sticky=W)
        Button(self, text='Browse...', command=self.getinputfile).grid(row=3, column=2, sticky=W)

        Label(self, text='Output file: ').grid(row=4, column=0, sticky=W)
        self.outputField.grid(row=4, column=1, sticky=W)
        Button(self, text='Browse...', command=self.getoutputfile).grid(row=4, column=2, sticky=W)

        Label(self, text='Pivot value: ').grid(row=5, column=0, sticky=W)
        self.pivotValue.grid(row=5, column=1, sticky=W)

        Button(self, text='Sort', command=self.sortdata).grid(row=6, column=0, sticky=W)

        self.mainloop()

    def loadfile(self, csvData = None, **fmtparams):
        """
        Load the contents of file into the self.data variable
        """
        fileName = self.inputField.get()
        if fileName.endswith('.csv') and csvData is None: csvData = True
        with open(fileName, 'r') as inputFile:
            if self.inputType.get() == 'List':
                self.data = []
                if csvData:
                    for row in csv.reader(inputFile, **fmtparams):
                        map(self.data.append, row)
                else:
                    for line in inputFile.readlines():
                        self.data.append(line)
            elif self.inputType.get() == 'Dictionary':
                self.data = dict()
                inputFile.close()
                raise NotImplementedError('Dictionary support not ready yet')

    def savefile(self, csvData = None, **fmtparams):
        """
        Saves the sorted list/dictionary to a file
        """
        fileName = self.outputField.get()
        if fileName.endswith('.csv') and csvData is None: csvData = True
        with open(fileName, 'w') as outputFile:
            if self.inputType.get() == 'List': # That is *not* a typo, output type should match input type
                if csvData:
                    tmp = csv.writer(outputFile, **fmtparams)
                    tmp.writerow(self.data)
                else:
                    map(outputFile.write, self.data)
            elif self.inputType.get() == 'Dictionary':
                outputFile.close()
                raise NotImplementedError('Dictionary support not ready yet')

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
        if self.inputType.get() == '':
            showerror('Missing input type', 'Please specify an input type')
            return
        if self.outputType.get() == '':
            showerror('Missing output type', 'Please specify an output type')
            return
        if self.inputField.get() == '':
            showerror('Missing input filename', 'Please specify an input filename')
            return
        if self.outputField.get() == '':
            showerror('Missing input filename', 'Please specify an output filename')
            return
        if self.pivotValue.get() == '' and self.inputType.get() == 'Dictionary':
            showerror('Missing pivot value with dictionary', 'Please specify a pivot value or switch to list')
            return
        # If we reach here all the fields are good
        self.loadfile()

        if self.inputType.get() == 'List':
            self.data = self.sortTypes[self.sortType.get()](self.data)
        elif self.inputType.get() == 'Dictionary':
            self.data = self.sortTypes[self.sortType.get()](self.data, key = lambda x,y=self.pivotValue.get(): x[y])

        self.savefile()

def main():
    SortsGui()
