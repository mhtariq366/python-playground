"""
similar in some aspects to map function.
filter() is used when a specific function is to be run on an iterable, like a list, a tuple or any other.

it is used when the iterable needs to be filter.
Only the elements that do not satisfy the lambda function are filtered out.
the elements that return true for the lambda function are selected.

lets see the working of filter function.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pr_num = filter(lambda x: x%2 != 0, nums)

print(list(pr_num))     # list of odd numbers