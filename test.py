"""
Testing script for libuseful
"""
# pylint: disable-all
from __future__ import print_function, absolute_import
from .searches import linear
from .searches import binary
from .sorts import quicksort
import sys
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
def test_search(search):
    """
    Test a search.
    """
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 5
    r = search(data, target)
    if r == (2, 5):
        return True
    else:
        return False
def linearsearch_test():
    """
    Test linear searching.
    """
    return test_search(linear.linear_search)
test("linear search", linearsearch_test)
def binarysearch_test():
    """
    Test binary searching.
    """
    return test_search(binary.binary_search)
# Sorts
def test_sort(sort):
    data = [9, 7, 5, 3, 1]
    expected = [1, 3, 5, 7, 9]
    if quicksort.quick_sort(data) == expected:
        return True
    else:
        return False
test("binary search", binarysearch_test)
def quicksort_test():
    """
    Test quicksorting.
    """
    return test_sort(quicksort.quick_sort)
test("quicksort", quicksort_test)
def selectionsort_test():
    """
    Test selection sorting
    """
    return test_sort(selectionsort.selection_sort)
test("selection sort", selectionsort_test)
### End tests
print("%i tests passed, %i tests failed" % (passcount, failcount))
if failcount > 0:
    sys.exit(1)
