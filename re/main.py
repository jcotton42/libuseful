from Tkinter import *
import re
class Window(Tk):
	"""
	Helper class to make the creation of windows and dialogs easier.
	"""
	def __init__(self):
		Tk.__init__()
		self.init()
		self.mainloop()
	def init(self):
		"""
		Stub method which subclasses use to initialize GUI 
		components.
		"""
		pass
