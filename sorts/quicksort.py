from random import choice
def quickSort(a):
	"""
	Perform a quicksort on a given list. Return the sorted list.
	Example:

	>>> quickSort([1, 5, 7, 2, 3, 4, 1])
	[1, 1, 2, 3, 4, 5, 7]
	"""
	if a == []: return [] # Don't infinitely recurse
	pivot = choice(a) # Choose a pivot value
	less = [i for i in a if i < pivot] # Get values less than the pivot
	equal = [i for i in a if i == pivot] # Values equal to the pivot
	greater = [i for i in a if i > pivot] # And greater than the pivot
	return quickSort(less) + equal + quickSort(greater) # Recursively sort
if __name__ == "__main__":
	import doctest
	doctest.testmod()