"""
Lists are data structures in the python.
Lists:
1. Ordered
2. Mutable (this means that new once the list is created, items can be added, updated and removed)
3. It can contain elements of different data types at once.

There are many built in functions, that help in coding. SUch as sort, count, these help in many cases.

Lets further explore the different operations that can be done on lists.
"""

my_list = [5, 6, 9, 0, 3]   # list is initialized using square brackets, and elements separated by comma symbol.

print(my_list[2])   # list items are accessed by using square brackets with item position. first position is index 0.

print(my_list[-1])  # negative 1, as stated in basics lessons, accesses last index

"""
index slicing can be done using colon operator, with left side stating start position and right side stating end position
keeping in mind that the end position itself is not included, instead the 2nd last is included.
in the below example, index 1 of list is included, index 2 is included but not 3. slicing stop at end position - 1.
"""
print(my_list[1:3])

# as stated, lists can have elements of different data types. lets try it.

my_list = [5, "Hello", 3.1, 'bye']
print(my_list)  # it prints all the elements in the list.

# 1. add new element at end
print(my_list)  # output: [5, "Hello", 3.1, 'bye']

my_list.append(66)  # adding new element at last position

print(my_list)  # output: [5, "Hello", 3.1, 'bye', 66]



# 2. add new element at a specifc position
print(my_list)  # output: [5, "Hello", 3.1, 'bye', 66]

my_list.insert(1, 66)  # adding new element 66 at position 1

# a new element is inserted at position 1. Currently at position 1 is "hello". it will be moved one step forward.
# and new number 66 will be added at position 1 now.
print(my_list)  # output: [5, 66,"Hello", 3.1, 'bye', 66]


# 3. removing an element

my_list.remove("Hello") # this removes the hello element from the list
print(my_list)

# However, keep in mind that, the remove function works by exactly matching the element passed. so incase of string, make sure the lower and upper case is followed.

# 4. remove element by index position

my_list.pop(2)      # element at position 2, is removed.
print(my_list)

# 5. Sort function, must use list of same data type elements.
my_list = [5, 6, 8, 0, 3, 5, 6, 1]
print("Unsorted:", my_list)

my_list.sort()      # this line sorts the list in ascending order.
print("Sorted:", my_list)


# 6. Reverse
my_list = [5, 6, 8, 0, 3, 5, 6, 1]
print("Current order:", my_list)

my_list.reverse()      # this line reverses the list.
print("Reverse:", my_list)


# 7. Count
my_list = [0, 1, 1, 0, 2, 5, 6, 1]
print("Count of 1: ", my_list.count(1))     # count function counts all occurance of element that is passed to it as parameter


###### There are many more built in operations that can be performed on list, try searching and using them for practise.

