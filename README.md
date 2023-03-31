## SDSS Computing Studies Python Assignment
### Assignment 017 Try Except Blocks

Objectives:
* Use try except to catch errors and work around them

https://www.w3schools.com/python/python_try_except.asp
'
When you are running a program and you generate an error, the program will stop and exit.  There are times when you might want to ignore the error and have the program keep going, or do something if an error pops up and use some alternate code.  In these cases, we use a try...except structure.  Many programs have this, although it is sometimes called try...catch.


Try...except is especially useful when you are asking the user to enter in a number, and they keep trying to enter in something with characters or symbols.  We could receive each keystroke, and check to see if the characters are valid keys, or we could just try to convert it, and if it doesn't work, throw an exception and ask them to do it again: example2.py

In example2.py, the **try** attempts to execute the code on lines 6 and 7.  If they are valid, then they are all kept. However, if the code is invalid, then the parts up to where the error occurred are kept, and everything below the error is ignored.