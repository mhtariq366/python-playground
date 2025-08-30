"""
lambda can also be used with map function
map syntax: map(function, iterable)

map function is used when the purpose is to apply one single function to every element of a list, tuple etc.

"""


nums = [2, 4, 6, 8, 10]

num_sq = map(lambda x: x*x, nums)   #   map has two parameters, first one is lambda function. second one is any iterable.

"""
now map function runs the first paramter which is a lambda function on every element of the list one by one.
the num_sq variable has an object returned to it from map function.
to print this, we convert the object to a list as follows
"""

print(list(num_sq))