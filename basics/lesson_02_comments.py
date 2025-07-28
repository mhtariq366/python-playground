# Comments


# python typically supports single line comments.
# but there a work around for multi line comment.

# A hash symbol is used at start of line to make it a single line comments.
# you can keep using it on every line to make it single line comment.


"""
You can use a set of three double quotes at start
and at the end the multi line comment.

However, theres as catch, this multi line comment is not an official python multi line comment,
but a multi line string. This can also be assigned to a variable and printed.
But if you dont assign it to any variable, treat it as a multi line comment.
"""


var = """
assign
this
to a 
str variable
and print
it.
"""

print(var)