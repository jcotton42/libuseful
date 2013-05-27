from Tkinter import *

class SearchesGui(Tk):
    def __init__(self, *args, **kwargs):
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

        self.to_search_field = Entry(self.right_frame)
        self.to_search_field.pack()

        self.search_button = Button(self.right_frame, text = "Search", command = self.do_search)
        self.search_button.pack()

        self.mainloop()

    def loadfile(self):
        f = open(self.file_field.get())
        items = [i[:-1] for i in f.readlines()]
        for i in items:
            self.items.insert(END, i)
        f.close()

    def do_search(self):
        pass

def main():
    SearchesGui()
