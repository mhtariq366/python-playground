"""
Reverse a given string
"""

var = "hello python"

#   using built in reverse
new_str = ''.join(reversed(var))
print(new_str)

#   using slicing
print(var[::-1])


#   without built in or slicing. using loop

new_s = ''
for i in var:
    new_s = i + new_s

print(new_s)