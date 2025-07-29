"""
The loops are iterative structures, that run up until a certain condition is met.
The while loop is used as follows:
"""
var=5             # initial value
while var>0:      # run loop while var's value in greater than 0
    print(var)
    var -= 1        # in every iteration, var's value is decremented by 1

# when you run this loop, it can be seen by print(var) that in every iteration, var's value is decremented.

"""
Another loop used in python is for loop.
it has many different styles. For loop can be used to traverse over a string, an object, list etc.
for example:
"""
var = "Hello"
for x in var:   # iterating over every character in Hello
    print(x)

var = [1, 5, 7, 9, 3]
for num in var:
    print(num)  # iterating over every number in list

"""
another way to use for loop is to use its range.
for example:
"""

for i in range(50):
    print(i)

"""
the range allows to specify the range across which the loop will run.
range has three paramters: range(start:end:jump)
start is the starting point. End is where the loop will stop at end-1 step. Jump is how much increment
or decrement is allowed, 1 means increment of 1, while negative number means decrement of said number.
if start is left blank, it starts from 0
if jump is left blank, if assumes a jump of +1 in every iteration.
"""

for i in range(50, 25, -2):
    print(i)        # print starts from 50, decrements to 25, with -2 jumps. Will stop at 26.