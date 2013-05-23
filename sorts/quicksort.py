"""
This module implements the quicksort algorithm.
"""
from random import choice

def quick_sort(arr, key=lambda x:x):
    """
    Perform a quicksort on a given list. Return the sorted list.
    Example:

    >>> quick_sort([1, 5, 7, 2, 3, 4, 1])
    [1, 1, 2, 3, 4, 5, 7]
    >>> quick_sort([
    ... {"name": "Fox", "age": 13},
    ... {"name": "John Doe", "age": 12},
    ... {"name": "Wumpus", "age": 15}], key=lambda x: x["age"])
    [{'age': 12, 'name': 'John Doe'}, {'age': 13, 'name': 'Fox'}, {'age': 15, 'name': 'Wumpus'}]

    :returns: Sorted list
    """
    if arr == []:
        return [] # Don't infinitely recurse

    pivot = key(choice(arr)) # Choose a pivot value
    less = [i for i in arr if key(i) < pivot] # Get values less than the pivot
    equal = [i for i in arr if key(i) == pivot] # Values equal to the pivot
    greater = [i for i in arr if key(i) > pivot] # And greater than the pivot
    return quick_sort(less) + equal + quick_sort(greater) # Recursively sort

if __name__ == "__main__":
    import doctest
    doctest.testmod()
