# GUI
This is the main gui for libuseful and serves as an invoker for the other guis
## Layout
One button for quit and one button per gui, packages in libuseful must have the variables `_gui` set to `True` and `_gui_name` set to the desired name of the button in the init file, each module must also have a main method, __main__.py is optional
## Setting up the interface
<pre>
foreach module in libuseful package
    if _gui exists and is set to True
        import main from module
        create a button
        set button label to _gui_name and command to main
        un-import main
    end if
end foreach
</pre>
