"""
Tuple is data structure with following properties:
1. Immutable (cant be changed after initialization)
2. Can contain elements of different data types.
"""

# tuple is defined as follows:
my_tuple = (1, 5, 9, 3)
print(my_tuple)

"""
normally parenthesis () are used to define tuple. However, it can be defined without ()
view the example below:
"""

my_tuple = 5, 9, 3, 1       # just write elements separated by commas, no parenthesis
print(type(my_tuple))       # output the type, it will show a class tuple.

"""
these two ways, a tuple can be defined.
they can contain elements of different data types
"""

my_tuple = ('hello', 5, 9, 3.1)
print(my_tuple)

# Accessing the values of tuples is similar to list

print(my_tuple[3])  # element at index 3


# definition difference:
my_tuple = (3)          # not a tuple
print(type(my_tuple))

my_tuple = (3, )        # is a tuple
print(type(my_tuple))


# As stated above, tuples are immutable. lets see:

my_tuple = (1, 2, 3, 4, 5)

# lets replace 3rd index element with another new value
my_tuple[3] = 55    # this will raise an error, cause tuples does not support it.



