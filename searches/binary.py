TARGET_NOT_FOUND = -1
def binarySearch(a, target):
	"""
	Perform a binary search on a given list with the given
	target. Returns TARGET_NOT_FOUND if the target was not
	found, or the position of the target if it was
	found.
	Example:

	>>> binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 4)
	3
	>>> binarySearch([1, 3, 5, 7, 9, 11], 3)
	1
	>>> binarySearch(["five", "four", "one", "six", "three", "two"], "two")
	5
	>>> binarySearch([0, 1, 3, 4, 5], 2)
	-1
	"""
	upperBound = len(a)
	lowerBound = 0
	center = len(a)/2
	while upperBound - lowerBound > 1:
		if target == a[center]:
			return center
		if target > a[center]:
			lowerBound = center
			center = (upperBound + lowerBound) / 2
			continue
		if target < a[center]:
			upperBound = center
			center = (upperBound + lowerBound) / 2
			continue
	return TARGET_NOT_FOUND
if __name__ == "__main__":
	import doctest
	doctest.testmod()
