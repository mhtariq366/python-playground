# Input

# input like in any other language, is taken for various purposes. Python performs the input process via the command:

input() 

"""
This command allows input. But this input is not useful to us yet. We assign this input function to variable, this way, the input
value will be stored in that particular variable.
for example: 
"""
# var = input()

"""
this is better. Not perfect yet. Now will would like to display a message for user to view before input. this done by writing message
in the parenthesis of the input function, enclosed by quotes.
for example:
"""
var = input("Please enter number: ") # this will display a message before getting input:

print(var) # this will now print the input taken.

"""
An important thing to note down is that, every input is considered to be a string. No matter if your enter numbers only. Initially,
its considered a string. Verify this by running the type() function we learned in lesson 01.
"""