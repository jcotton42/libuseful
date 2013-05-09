# Sorts
This project includes/will include several sorts. Among these will be:

- Quicksort
- Selection sort
- Bubble sort
- Insertion sort

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

