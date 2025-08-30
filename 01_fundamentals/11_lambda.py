"""
Lambda keyword is used to write small functions where theres no need to write lengthy functions using the
def keyword.

syntax:

lambda arguments(parameters): expression
"""


#   add two numbers lambda function
two_add = lambda a,b: a+b

print(two_add(5,3))


"""
lets say you need to write a function that needs to check if a number is even. lets write it using
def and lambda keywords separately.
"""

#   using def
def even_check(num):
    if num%2==0:
        return True
    return False

print(even_check(5))

#   using lambda
even_check_lambda = lambda x: x%2==0
print(even_check_lambda(5))


#   as can be seen above that lambda is quite easier in writing functions for smaller problems.
