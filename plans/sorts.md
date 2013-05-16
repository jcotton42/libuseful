# Sorts
This project includes/will include several sorts. Among these will be:

- Quicksort
- Selection sort
- Bubble sort

## Quicksort
Algorithm:
<pre>
if list is empty
	return empty list
pivot = random value from list

less list = all values from list less than pivot
equal list = all values from list equal to pivot
greater list = all values from list greater than pivot

return quicksort(less list) plus equal list plus quicksort(greater list)
</pre>

## Selection sort
Algorithm:
<pre>
set the maximum index to the length of the list minus one
while the maximum index is greater than zero
	find the position of largest object in the list with respect to the maximum index
	switch the largest object in the list with the last item in the list with respect to the maximum index
	decrement the maximum index
return the sorted list
</pre>

## Bubble sort
Algorithm:
<pre>
set the current index to the length of the array minus one
while the current index is greater than zero
	compare the element at the current index with
		the element at the current index minus one
	if the second element is smaller
		swap the elements
	decrement the current index
return the sorted list
</pre>

## Insertion sort
Algorithm:
<pre>
for each itemA in the reversed array
    remove the item
    for each itemB in the array
        if itemA is less than itemB
            insert itemB at the current position
            end loop
    otherwise add itemA to the array
return the array
</pre>

## GUI
Interface containing the following fields:

* Input type - default is file and array, files must be in CSV format, matrix keys must be the first line (dropdown)
    * File
        * Array
        * Matrix
    * Type the data directly
        * Array
        * Matrix
* Output type
    * File
    * Display
* Input feild - textbox + Browse... button for file, large textbox for direct typing
* Pivot value - matricies only
* Sort type (dropdown)
* Output feild - textbox + Browse... button for file, large textbox for direct typing
* Sort (button)

### Required variables for sort GUI

Each file in the sort package must have two variables

* `_sort_name` - the name of the algiothrim
* `_sort` - variable that points to the sorting method or a lambda or method that calls the sorting method, must accept two argumetns, an array and a key
