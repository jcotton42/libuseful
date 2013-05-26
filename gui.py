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
        os.chdir(os.path.dirname(__file__))
        for name in os.listdir('.'):
            button_name = ''
            if os.path.isdir(name) and os.path.isfile(name + '/__init__.py'):
                mod = __import__(name, globals(), locals(), [], 0)
                if '_gui' in mod.__dict__ and mod._gui == True and 'main' in mod.__dict__:
                    if '_gui_name' in mod.__dict__: button_name = mod._gui_name
                    else: button_name = name
                    btn = Button(master = self, text = button_name, command = mod.main)
                    btn.pack()

def main():
    maingui()
