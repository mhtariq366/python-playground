#   lambda can also be used with map function
#   map syntax: map(function, iterable)

nums = [2, 4, 6, 8, 10]

num_sq = map(lambda x: x*x, nums)   #   map has two parameters, first one is lambda function. 

print(list(num_sq))