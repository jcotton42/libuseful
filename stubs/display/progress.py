from __future__ import division
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
