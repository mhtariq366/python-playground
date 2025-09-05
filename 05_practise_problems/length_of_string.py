"""
Count the length of string. The total characters in a string.
"""


var = "hello python"

#   the easy way.
print(len(var))



#   without using the len() function

c=0
for i in var:
    c+=1
print(c)