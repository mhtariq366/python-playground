"""
Functions are block of code, they are executed only when called.
Name of function starts with def followed by the function name and parenthesis.
If some parameters are to be passed to the functions, they are written in the parenthesis, separated by commas.
End function header with a colon.
Every thing under the indentation of function is under its body.
Simplest function is as follows:
"""
def hello():
    print("hello")

hello()     # this is function call

# function to return value

def hello_return():
    return 3        # return type is by default, no need to explicitly state like in c or c++

print(hello_return())

"""
functions using parameters are defined as follows:
"""

def hello_param(name):
    print("hello", name)

hello_param("Jon")

"""
if number of arguments is unknown, use *args in function parameters.
if number of named arguments is unknown, use **kwargs in functions paramters.
args and kwargs can be replaced by any name. Main concept is of using * and **.
* allows to get paramters as tuples, while ** allows to get parameters as dictionary.

lets explore:
"""

def hello_args(*name):
    print("hello", name[0], name[1])

hello_args("Jon", "Alice")


def hello_kwargs(**name):
    print("hello", name["first_n"], name["last_n"])

hello_kwargs(first_n = "Jon", last_n = "Alice")

"""
now practise passing list to the parameters, without *args or **kwargs
"""