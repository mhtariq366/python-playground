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


#You can clearly see that same random numbers are generated if we set the state to a specific state we saved earlier.

"""
RandRange(), similar to randint generates a random number. But theres a slight difference. In randint, the range given are 
both included. However, in randrange, the range given does not include the endpoint of range. 
Also, randrange allows third parameter as step. which can be used to generate a random number with specific 
step difference.
lets see how it works.
"""

print(random.randrange(1, 10, 4))
"""
in above example,
1. the first parameter is starting point. this will be included.
2. second parameter is the endpoint. whoch will not be included. So this means at endpoint minus 1. 
in case of example above, the number 10 will not be included. 
3. third parameter is step. so if start at 1. next random number will always be in gaps of 4 in this example.
they can be 1+4, or 1+4+4 etc.

for example, if you want to generate random numbers from 10 to 100. and print only numbers starting from 10 
and allow only even numbers. this can be done as follows.
"""

print(random.randrange(10, 101, 2))
