from Tkinter import *

class SortsGui(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Create fields
        self.inputType = Listbox(self) # type of data and where to take it from
        self.outputType = Listbox(self) # where to put the data
        self.inputField = None # set later depending on options
        self.pivotValue = None # set later depending on options
        self.sortType = Listbox(self) # which sort to use
        self.outputField = None # set later depending on options
        self.sortData = None # create later

        # Get sort types


def main():
    SortsGui()
