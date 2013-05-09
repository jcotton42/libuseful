# Searches
This project includes/will include several searches. Among these will be:

- Linear search
- Binary search

## Linear search
Algorithm
<pre>
for each item in the list
	if the item is the target
		return the position of the item
return the flag indicating that the target was not found
</pre>

## Binary search
Algorithm
<pre>
set the upper bound to the length of the list
set the lower bound to 0
set the center to the length of the list divided by 2
while the difference between the upper and the lower bound is greater than 1
	if the target is the value at the center
		return the center position
	if the target is greater than the value at the center
		set the lower bound to the center
		recalculate the center position
		skip to the next iteration
	if the target is less than the value at the center
		set the upper bound to the center
		recalculate the center position
		skip to the next iteration
return the flag indicating that the target was not found
</pre>
