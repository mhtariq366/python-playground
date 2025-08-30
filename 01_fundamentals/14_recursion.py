"""
Recursion is when a function keeps calling itself from within the function from within the function from within the funcion.

recursion is useful when the problem can be broken down into smaller parts. the smaller parts are then solved easily.

The recursion function must have a base case and recurring case. Base case is the stopping condition, while the recurring case
is used to keep dividing problem into smaller parts.
"""

def factorial(num):
    if num == 1 or num == 0:            #   base case
        return num
    else:                               #   recurring case
        return num * factorial(num-1)
    
print(factorial(5))


"""
above is simple example of recursion in calculating the factorial of a number.
now add print statement to see how recursion calls are made.
"""

def factorial(num):
    if num == 1 or num == 0:            #   base case
        print(f'base case, {num}')
        return num
    else:                               #   recurring case
        print(f'recurring case, {num}')
        return num * factorial(num-1)
    
print(factorial(5))

"""
you can now see that problem is being divided into smaller parts.
5 then 4 then 3 and so on. when it reaches base case 1. then the return statement of base cases is nultiplied
with the num previous values.

for example
1. at start the num passed to function was 5.
2. in first function call, '5' remained to be multiplied to the recurring call of 5-1 i.e., 4.
3. in second function call (the actual first call from within the function), '4' remained to be multiplied with 4-1
4. in third function call (the actual second call from within the function), '3' remained to be multiplied with 3-1.
5. in fourth function call (the actual third call from within the function), '2' remained to be multiplied with 2-1.
6. in fifth function call (the actual fourth call from within the function), '1' remained. it encountered base case
and return itself i.e.c 1 to the previous function call.
7. 1 returned to previous call to be multiplied with 2, so 2*1 = 2
8. 2 returned to previous call to be multiplied with 3, so 3*2 = 6
9. 6 returned to previous call to be multiplied with 4, so 4*6 = 24
10. 24 returned to previous call to be multiplied with 5, so 24*5 = 120
"""

