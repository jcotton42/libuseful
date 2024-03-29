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

    :param arr: List to sort
    :type arr: list
    :returns: Sorted list
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
    return bubble_sort(*args, **kwargs)

_sort_name = "Bubble sort"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
