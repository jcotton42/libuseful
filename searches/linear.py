"""
This module implements a simple linear search.
"""
TARGET_NOT_FOUND = -1
def linear_search(arr, target, key=lambda x:x):
    """
    Perform a linear search on a given list with the given
    target. Returns TARGET_NOT_FOUND if the target was not
    found, or the the position of the target if it was
    found in the form of a tuple (position, object).
    Example:

    >>> linear_search([5, 2, 3, 1], 3)[0]
    2

    :param arr: The array to search through
    :param target: The target value
    :param key: A function which defines how to search
    :returns: A tuple in the form (index, target) 
    """
    for index, value in enumerate(arr):
        if key(value) == target:
            return (index, value)
    return (TARGET_NOT_FOUND, target)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
