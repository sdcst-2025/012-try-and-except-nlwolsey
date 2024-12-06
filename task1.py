#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

number = input("Please enter in an integer value")
try:
    number = int(number)
    print(f" the integer entered was {number}")
except:
    print("the value entered could not be converted to an integer")