from Tkinter import *
import os

class SortsGui(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.data = None # the data to sort
        # Create fields
        self.inputType = StringVar(self) # type of data and where to take it from
        self.outputType = None # where to put the data
        self.inputField = None # set later depending on options
        self.pivotValue = None # set later depending on options
        self.sortType = StringVar(self) # which sort to use
        self.outputField = None # set later depending on options
        self.sortData = None # create later
        self.sortTypes = dict() # holds the names and sort methods

        # Get sort types - this is a kludge, see if there's a better way
        old_dir = os.getcwd()
        os.chdir(os.path.dirname(__file__)) # Change to root package directory needed for __import__

        for name in os.listdir('.'):
            if name.endswith('.py'):
                modName = name[0:-3] # strip .py suffix
                if modName in ['__init__', '__main__', 'gui']: continue
                mod = __import__(modName, globals(), locals(), [], -1) # see /gui.py for explanaton
                if '_sort' in mod.__dict__:
                    sortName = ''
                    if '_sort_name' in mod.__dict__: sortName = mod._sort_name
                    else: sortName = modName
                    self.sortTypes[sortName] = mod._sort

        os.chdir(old_dir)

        Label(self, text = 'Input type').pack()
        OptionMenu(self, self.inputType, 'Array', 'Matrix')

        Label(self, text = 'Sort type').pack()
        OptionMenu(self, self.sortType, self.sortTypes.keys()[0], *self.sortTypes.keys()[1:]).pack(side = 'right')
        self.mainloop()

    def loadfile(self, fileName, csvData = None, sep = ','):
        inputData = open(fileName, 'r')
        if fileName.endswith('.csv') and csvData is None: csvData = True
        if self.inputType.get() == 'Array':
            for line in inputData.readlines():
                if csvData:
                    for

def main():
    SortsGui()
