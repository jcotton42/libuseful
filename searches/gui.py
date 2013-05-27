from Tkinter import *
from binary import *
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
        self.litems = [i[:-1] for i in f.readlines()]
        self.litems.sort()
        for i in self.litems:
            self.items.insert(END, i)
        f.close()

    def do_search(self):
        x = binary_search(self.litems, self.to_search_field.get())[0]
        self.items.selection_set(x)
        self.items.see(x)

def main():
    SearchesGui()

if __name__ == '__main__':
    main()
