from Tkinter import *
import os, sys

class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.initgui()
        self.mainloop()
    def initgui():
        """
        Implemented in subclass
        """
        raise NotImplementedError("implement initgui in the subclass please")

class maingui(Window):
    def __init__(self):
        Window.__init__(self)

    def initgui(self):
        old_dir = os.getcwd()
        os.chdir(os.path.dirname(__file__)) # Change to root package directory needed for __import__
        for name in os.listdir('.'):
            button_name = ''
            if os.path.isdir(name) and os.path.isfile(name + '/__init__.py'): # if this directory is a package
                mod = __import__(           # this means import name as mod
                    name,                   # Name of the module
                    globals(), locals(),    # Context for the module (all the globlas and locals it can use)
                    [],                     # the from part
                    0                       # 0 = absalute import only
                )
                if '_gui' in mod.__dict__ and mod._gui == True and 'main' in mod.__dict__:
                    if '_gui_name' in mod.__dict__: button_name = mod._gui_name
                    else: button_name = name
                    Button(master = self, text = button_name, command = mod.main).pack()
        os.chdir(old_dir)   # Change to where were

def main():
    maingui()
