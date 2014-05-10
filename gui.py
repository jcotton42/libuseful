"""
The GUI that launches all the subprograms
"""
from tkinter import *
import os, sys, webbrowser

class MainGui(Tk):
    """
    Main window of application
    """
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('libuseful')

        old_dir = os.getcwd()
        os.chdir(os.path.dirname(sys.argv[0])) # Change to root package directory needed for __import__
        # Add buttons
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
                    Button(self, text=button_name, command=mod.main).pack()
        docPathPy = os.getcwd() + '/docs/index.html'
        docPathPy = 'file://' + docPathPy.replace('\\', '/')
        Button(self, text='Open Python style docuemtation/API', command=lambda: webbrowser.open(docPathPy)).pack()

        docPathJava = os.getcwd() + '/docs-epydoc/index.html'
        docPathJava = 'file://' + docPathJava.replace('\\', '/')
        Button(self, text='Open Java style docuemtation/API', command=lambda: webbrowser.open(docPathJava)).pack()
        os.chdir(old_dir) # Change to where we were

        self.mainloop()

def main():
    MainGui()
