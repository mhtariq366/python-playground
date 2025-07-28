# if - elif - else

"""
Python allows conditional structures using if, elif and else.
The major point to consider is that python uses indentations. So when creating a boundry (body) of any conditional structure,
use indentations, and not curly braces like in c.
For example:
"""

if 7 > 6:
    print("True")   # notice the space we left at start of this line? This is indentation. 
    # All lines written in this indentation are within the body of the 'if' statement
# This line is not using the indetation like the one above, hence, it is outside the boundry of 'if' statement.
# in similar way, the else command is implemented.

if 7 > 6:
    print("True")
else:
    print("False")

"""
in the example above, the if and else statements have their own boundries, without the explicit stating of curly braces, instead,
it is represented by the indentation.
If multiple conditional statements are to be checked, python provides 'elif' command for this purpose. Similar to the 'else if' command in 
some languages.
for example:
"""
a, b = 55, 66

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")

"""
this way, multiple elifs can be used.

The relational operators that can be used are: > , < , >= , <= , != , ==
For multiple conditions within an if, logical operators, 'and' and 'or' can be used.
"""