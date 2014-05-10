
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from .binary import *
from .linear import *
"""
This file contains the searches GUI
"""
class SearchesGui(Tk):
    """
    Searches GUI for Libuseful
    """
    def __init__(self, *args, **kwargs):
        """
        Create the GUI elements.
        """
        Tk.__init__(self, *args, **kwargs)

        self.title("Searches")

        self.left_frame = Frame(self)
        self.left_frame.pack(side=LEFT)

        self.right_frame = Frame(self)
        self.right_frame.pack(side=RIGHT)

        self.items = Listbox(self.left_frame)
        self.items.pack()

        self.file_field = Entry(self.right_frame)
        self.file_field.pack()

        self.file_load_button = Button(self.right_frame, text = "Load File", command = self.loadfile)
        self.file_load_button.pack()

        self.file_choose_button = Button(self.right_frame, text = "Pick File", command = self.pickfile)
        self.file_choose_button.pack()

        self.to_search_field = Entry(self.right_frame)
        self.to_search_field.pack()

        self.bsearch_button = Button(self.right_frame, text = "Binary search", command = self.do_bsearch)
        self.bsearch_button.pack()

        self.lsearch_button = Button(self.right_frame, text = "Linear search", command = self.do_lsearch)
        self.lsearch_button.pack()

        self.mainloop()

    def loadfile(self):
        """
        Load a file into the GUI.
        """
        f = open(self.file_field.get())
        self.litems = [i[:-1] for i in f.readlines()]
        self.litems.sort()
        for i in self.litems:
            self.items.insert(END, i)
        f.close()

    def pickfile(self):
        """
        Pick a file to load into the GUI.
        """
        x = askopenfilename()
        if x == '':
            return
        self.file_field.delete(0, END)
        self.file_field.insert(0, x)

    def do_bsearch(self):
        """
        Perform binary search.
        """
        self.loadfile()
        self.items.selection_clear(0, END)
        x = binary_search(self.litems, self.to_search_field.get())[0]
        if x is -1:
            showwarning("", "That item wasn't found.")
        self.items.selection_set(x)
        self.items.see(x)

    def do_lsearch(self):
        """
        Perform linear search.
        """
        self.loadfile()
        self.items.selection_clear(0, END)
        x = linear_search(self.litems, self.to_search_field.get())[0]
        if x is -1:
            showwarning("", "That item wasn't found.")
        self.items.selection_set(x)
        self.items.see(x)

def main():
    """
    Run the GUI.
    """
    SearchesGui()

if __name__ == '__main__':
    main()
