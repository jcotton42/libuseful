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

# Searches GUI

- Open files
- Search by attribute

<pre>
function parsefile
    read the first line of the file
    store column names
    read the rest of the file
    create a list of dictionaries (keys are column names)
    store the list of dictionaries
end function

function search
    read attribute from textbox
    read search value from textbox
    call binary_search with these values
    display the result in a textbox
end function
</pre>
    
