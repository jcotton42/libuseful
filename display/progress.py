from __future__ import division
import sys
class ProgressBar:
    """
    Progress bar class. Displays text-based progress bars.
    """
    def __init__(self, maximum=100, start=0, twidth=50)
        """
        Init method. Takes a maximum value, start value, 
        width, character to indicate filled, character
        to indicate blank, and whether or not to show
        a percentage.
        """
        self.maximum   = maximum
        self.twidth    = twidth
        self.ratio     = maximum / twidth
        self.fillchar  = "#"
        self.blankchar = " "
        self.percent   = True
        self.update(start)
    def update(self, value):
        """
        Update the progress bar with a new value. This also
        redraws the progress bar.
        """
        if value > self.maximum:
            raise Exception("Value out of bounds")
        filled = value / self.ratio
        blanks = self.twidth - int(filled)
        percent = (value / self.maximum) * 100
        sys.stdout.write("[")
        sys.stdout.write(self.fillchar * int(filled))
        sys.stdout.write(self.blankchar * int(blanks))
        if self.percent: sys.stdout.write("] %i%%     " % percent)
        else: sys.stdout.write("]")
        sys.stdout.write("\r")
        sys.stdout.flush()
    def blank(self):
        sys.stdout.write(" " * (self.twidth + 8))
        sys.stdout.write("\n")
