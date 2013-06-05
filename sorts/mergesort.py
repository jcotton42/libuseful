"""
This module implements the quicksort algorithm.
"""
from random import choice

def _merge(l1, l2):
    res = []
    while len(l1) >= 1 or len(l2) >= 1:
        if len(l1) >= 1 and len(l2) >= 1:
            if l1[0] <= l2[0]:
                res.append(l1[0])
                l1 = l1[1:]
            else:
                res.append(l2[0])
                l2 = l2[1:]
        elif len(l1) >= 1:
            res.append(l1[0])
            l1 = l1[1:]
        elif len(l2) >= 1:
            res.append(l2[0])
            l2 = l2[1:]
    return res

def merge_sort(arr):
    """
    Perform a mergesort on a given list. Return the sorted list.
    Example:

    >>> merge_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    
    :param arr: List to sort
    :type arr: list
    :returns: Sorted list
    """
    if len(arr) < 2:
        return arr
    less = [i[1] for i in enumerate(arr) if i[0] < int(len(arr) / 2)]
    more = [i[1] for i in enumerate(arr) if i[0] >= int(len(arr) / 2)]
    return _merge(merge_sort(less), merge_sort(more))

def _sort(*args, **kwargs):
    return merge_sort(*args, **kwargs)

_sort_name = "Merge sort"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
