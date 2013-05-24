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
    """
    pass
