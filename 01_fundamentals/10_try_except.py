"""
Try except is used to test if a piece of code gives error.
Lets see how this works.
"""


try:
    print(1/0)
except:
    print('Except block')

"""
In the above case, 1/0 will not be printed as it will raise an error. Thus except will be printed. if the
try block does not cause any error, then except block is not executed. This can be seen in example below.
"""

try:
    print('try block')
except:
    print('Except block')


"""
We have written fairly simple examples above. In the first example, an error occured and except block was 
executed. But we were unable to see which type of error occured.
To see what type of error or exception has occured, we use the Exception as below.
"""

try:
    print(1/0)
except Exception as e:
    print(f'Except block error type: {type(e).__name__} : {str(e)}')