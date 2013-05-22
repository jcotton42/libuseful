"""
This module implements the bubble sort algorithim
"""

from __future__ import print_function

def bubble_sort(arr):
    """
    Perform a bubble sort on a given list. Return the sorted list.
    @return Sorted list
    Example:

    >>> bubble_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> bubble_sort(['a', 'd', 'b', 'c'])
    ['a', 'b', 'c', 'd']
    """
    if arr == []: # No point in sorting an exmpty list
        return []

    swapped = True

    while swapped:
        swapped = False
        for index in range(1, len(arr)):
            if arr[index - 1] > arr[index]:
                arr[index - 1], arr[index] = arr[index], arr[index - 1]
                swapped = True
    return arr

def _sort(*args, **kwargs):
    bubble_sort(*args, **kwargs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

