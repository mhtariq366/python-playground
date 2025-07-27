print("*********** Hello! ***********")

#Variables
"""
Variable names can be of different types. Almost the same naming conventions,
as that of other languages.
There are no variable declarations used in python.
A variable is created the very moment you assign a value to the variable.

For example: 

var = 5     # correct, this is int variable

int temp    # this is not right

num = "5"   # this is str variable

var = 5.6   # this is float variable

to print the type of variable, use type(variable) command.

lets see now.
"""

var = 5
print(type(var))    # this line prints int

var = 5.6           # you can reuse variable names with updated values, also updated data types
print(type(var))    # this prints float, cause now variable is of float type

var = "hello"
print(type(var))    # this prints str