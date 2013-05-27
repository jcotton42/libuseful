from Tkinter import *

class ReGui(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.inputType = StringVar(self)
        self.inputField = Entry(self)
        self.reEntry = Text(self, width=60, height=10, wrap=NONE)
        self.reMatches = Entry(self)

        Label(self, text='Input type: ').grid(row=0, column=0, sticky=W)
        OptionMenu(self, self.inputType, 'File').grid(row=0, column=1, sticky=W)

        Label(self, text='Input file: ').grid(row=1, column=0, sticky=W)
        self.inputField.grid(row=1, column=1, columnspan=2, sticky=W, ipadx=60)
        Button(self, text='Browse...').grid(row=1, column=3, sticky=W)

        Label(self, text='Regular expression:').grid(row=2, column=0, columnspan=4, sticky=W)
        self.reEntry.grid(row=3, column=0, columnspan=4, sticky=W)

        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.reEntry.yview)
        self.scrollY.grid(row=3, column=4, sticky=N+S+W)

        self.scrollX = Scrollbar(self, orient=HORIZONTAL, command=self.reEntry.xview)
        self.scrollX.grid(row=4, column=0, columnspan=4, sticky=N+E+W)

        self.reEntry.config(yscrollcommand = self.scrollY.set)
        self.reEntry.config(xscrollcommand = self.scrollX.set)

        self.mainloop()

def main():
    ReGui()
