"""
Sets are unorderd. 
Have unique elements.
They dont allow duplicate values.

"""

#   declaration
my_set = {5, 3, 9, 1}


#   lets see if inserting duplicate items is printed or processed by sets.
print(f"without Duplicate {my_set}")
my_set = {5, 3, 9, 1, 3, 5}
print(f"with Duplicate {my_set}")

#   sets can have values of different data types
my_set = {5, 3, 9, 1, True, 'Hello', 3.5}
print(f"Different Datatypes values: {my_set}")

#   to traverse through the sets, a loop can be used as follows
for item in my_set:
    print(item)

#   Adding new item in set
my_set = {5, 3, 9, 1, True, 'Hello', 3.5}
my_set.add(99)
print(f"Added 99: {my_set}")

#   removing a specific item from the set
my_set = {5, 3, 9, 1, True, 'Hello', 3.5}
my_set.remove(3.5)
print(f"Removed 3.5: {my_set}")


#   removing a random item from the set
my_set = {5, 3, 9, 1, True, 'Hello', 3.5}
my_set.pop()
print(f"After Pop: {my_set}")
