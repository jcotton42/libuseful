# Regular expressions GUI

## Interface

* Input type
    * File
    * Type text
* Very large textbox for regular expression to run
* Very large textbox for typing or textbox + Browse... button for file, provides content to run the RE on
* Very large textbox for matches
* Search button
* Help button (pops up regex and macro (feature of the program) references)

<code>
function readfile
    get filename from text box
    open file
    read file contents
    close file
    store file contents
end function

function search
    get regex from text box
    get text from file contents
    use re.findall to find all matches
    display matches in match list
end function

function help
    create a new window
    display help string
    wait until quit
end function
</code>
