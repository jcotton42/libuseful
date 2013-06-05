from __future__ import *

# window.py
"""
Abstracts a GUI window
"""
from Tkinter import *
class Window(Tk):
    def __init__(self):
        self.initgui()
    def initgui():
        """
        Defined in subclasses
        """
        pass

# sortsgui.py
"""
Sorts GUI interface
"""
from window import *
class SortsGui(Window):
    """
    Sorts GUI class
    """
    def initgui(self):
        """
        Initialize the GUI
        """
        pass
    def sort(self):
        """
        Sort the items in the GUI
        """
        pass
    def loadfile(self):
        """
        Load a file into the GUI
        """
        pass

# searchesgui.py
"""
Searches GUI interface
"""
from window import *
class SearchsGui(Window):
    """
    Searches GUI class
    """
    def initgui(self):
        """
        Initialize the GUI
        """
        pass
    def search(self):
        """
        Search the items in the GUI
        """
        pass
    def loadfile(self):
        """
        Load a file into the GUI 
        """
        pass

#regui.py
"""
Regexs GUI
"""
class REGui(Window):
    """
    RE Gui
    """
    def initgui(self):
        """
        Init gui
        """
        pass
    def loadfile(self):
        """
        Load file into interface
        """
        pass
    def search(self):
        """
        Perform the search
        """
        pass

# mergesort.py
"""
This module implements the mergesort algorithm
"""

def merge_sort(arr):
    """
    Perform a merge sort on a given list. Return the sorted list.
    """
    pass

# selectionsort.py
"""
This module implements the selection sort algorithim
"""

def selection_sort(arr):
    """
    Perform a selection sort on a given list. Return the sorted list.
    Example:

    >>> selection_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> selection_sort(['a', 'd', 'b', 'c'])
    ['a', 'b', 'c', 'd']
    """
    pass

# bubblesort.py
"""
This module implements the bubble sort algorithim
"""

def bubble_sort(arr):
    """
    Perform a bubble sort on a given list. Return the sorted list.
    Example:

    >>> bubble_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> bubble_sort(['a', 'd', 'b', 'c'])
    ['a', 'b', 'c', 'd']
    """
    pass

# quicksort.py
"""
This module implements the quicksort algorithm.
"""
from random import choice
def quick_sort(arr, key=lambda x:x):
    """
    Perform a quicksort on a given list. Return the sorted list.
    Example:

    >>> quick_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> quick_sort([
    ... {"name": "Fox", "age": 13},
    ... {"name": "John Doe", "age": 12},
    ... {"name": "Wumpus", "age": 15}], key=lambda x: x["age"])
    [{'age': 12, 'name': 'John Doe'}, {'age': 13, 'name': 'Fox'}, {'age': 15, 'name': 'Wumpus'}]
    """
    pass

# heapsort.py
"""
This module implements the heapsort algorithm
"""

def heap_sort(arr):
    """
    Perform a heap sort on a given list. Return the sorted list.
    """
    pass

# binary.py
"""
This module implements a very fast binary search.
"""
TARGET_NOT_FOUND = -1
def binary_search(arr, target, key=lambda x:x):
    """
    Perform a binary search on a given list with the given
    target. Returns TARGET_NOT_FOUND if the target was not
    found, or the position of the target if it was
    found in the form of a tuple (position, object).
    Example:

    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8], 4)[0]
    3
    >>> binary_search([1, 3, 5, 7, 9, 11], 3)[0]
    1
    >>> binary_search(["five", "four", "one", "six", "three", "two"], "two")[0]
    5
    >>> binary_search([0, 1, 3, 4, 5], 2)[0]
    -1
    """
    pass

# linear.py
"""
This module implements a simple linear search.
"""
TARGET_NOT_FOUND = 1
def linear_search(arr, target, key=lambda x:x):
    """
    Perform a linear search on a given list with the given
    target. Returns TARGET_NOT_FOUND if the target was not
    found, or the the position of the target if it was
    found in the form of a tuple (position, object).
    Example:

    >>> linear_search([5, 2, 3, 1], 3)[0]
    2
    """
    pass

# progress.py
import sys
class ProgressBar:
    def __init__(self, maximum=100, start=0, twidth=50):
        """
        Init method. Takes a maximum value, start value, 
        width, character to indicate filled, character
        to indicate blank, and whether or not to show
        a percentage.
        """
        self.update(start)
    def update(self, value):
        """
        Update the progress bar with a new value. This also
        redraws the progress bar.
        """
        pass
    def blank(self):
        """
        Remove the progress bar from the screen.
        """
        pass
