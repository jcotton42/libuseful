"""
This module implements the selection sort algorithim
"""

from __future__ import print_function

def selection_sort(arr):
    """
    Perform a selection sort on a given list. Return the sorted list.
    Example:

    >>> selection_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> selection_sort(['a', 'd', 'b', 'c'])
    ['a', 'b', 'c', 'd']

    :returns: Sorted list
    """
    if arr == []: # No point in sorting an exmpty list
        return []

    for max_index in range(len(arr) -1 , 0, -1):
        max_pos = arr.index(max(arr[0:max_index + 1]), 0, max_index + 1)
        arr[max_index], arr[max_pos] = arr[max_pos], arr[max_index]

    return arr

def _sort(*args, **kwargs):
    return selection_sort(*args, **kwargs)

_sort_name = "Selection sort"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
