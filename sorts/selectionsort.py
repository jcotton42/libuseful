#-------------------------------------------------------------------------------
# Name:        selectionsort
# Purpose:
#
# Author:      Joshua Cotton
#
# Created:     12/05/2013
# Copyright:   (c) Joshua Cotton and Fox Wilson 2013
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------
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
    """
    if arr == []: # No point in sorting an exmpty list
        return []

    for maxIndex in range(len(arr) -1 , 0, -1):
        maxPos = arr.index(max(arr[0:maxIndex + 1]), 0, maxIndex + 1)
        arr[maxIndex], arr[maxPos] = arr[maxPos], arr[maxIndex]

    return arr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
