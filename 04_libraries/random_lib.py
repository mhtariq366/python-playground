import random

#   random int between 5 and 5000
print(random.randint(5,5000))

"""
although its random, but you can re generate the same random numbers again by using the state of the random number
generator. using the getstate() function.
"""
st = random.getstate()
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

random.setstate(st)
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

"""
You can clearly see that same random numbers are generated if we set the state to a specific state we saved earlier.
"""

