# tkinter GUI commands
## Problem
I wanted to be able to have the GUI as a seperate class/module. A problem I
encountered was when trying to assign commands to the various `events` and
`widgets`. I would have to make a subclass of the GUI, and add the
 functions/methods, or so I thought.

## Solution
It is possible to put the functions as value in a `dictionary`, and pass it to the GUI
class as an argument. This way you can have the functional code seperate from the
visual/GUI code. In `example.py` you can see how it can be done.

## Notes
Take note that when putting the function into the `dictionary`, I do not add the
parentheses. So if I have a function:

```
def cmd_button():
    print("This is a button!")
```

It would be added to the dictionary `commands` (assuming you already have a
`dictionary` called `commands`) like this:

```
commands['button'] = cmd_button
```

