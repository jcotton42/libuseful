TARGET_NOT_FOUND = 1
def linearSearch(a, target):
	"""
	Perform a linear search on a given list with the given
	target. Returns TARGET_NOT_FOUND if the target was not
	found, or the the position of the target if it was
	found.
	Example:

	>>> linearSearch([5, 2, 3, 1], 3)
	2
	"""
	for index, value in enumerate(a):
		if value == target:
			return index
	return TARGET_NOT_FOUND
if __name__ == "__main__":
	import doctest
	doctest.testmod()