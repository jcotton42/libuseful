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
