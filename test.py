"""
Testing script for libuseful
"""
# pylint: disable-all
from __future__ import print_function
import searches 
import searches.linear
import searches.binary
import sorts 
import sorts.quicksort
global passcount, failcount
passcount = 0
failcount = 0
def test(name, func):
    """
    Test a function.
    """
    global passcount, failcount
    if func():
        print("Test '%s' passed" % name)
        passcount += 1
    else:
        print("Test '%s' FAILED" % name)
        failcount += 1
### Start tests
def linearsearch_test():
    """
    Test linear searching.
    """
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 5
    r = searches.linear.linear_search(data, target)
    if r == (2, 5):
        return True
    else:
        return False
test("linear search", linearsearch_test)
def binarysearch_test():
    """
    Test binary searching.
    """
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 5
    r = searches.linear.linear_search(data, target)
    if r == (2, 5):
        return True
    else:
        return False
test("binary search", binarysearch_test)
def quicksort_test():
    """
    Test quicksorting.
    """
    data = [9, 7, 5, 3, 1]
    expected = [1, 3, 5, 7, 9]
    if sorts.quicksort.quick_sort(data) == expected:
        return True
    else:
        return False
test("quicksort", quicksort_test)
### End tests
print("%i tests passed, %i tests failed" % (passcount, failcount))
