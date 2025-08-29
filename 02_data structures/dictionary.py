"""
Another data structure provided by python is dictionary.
A dictionary stores key value pair. Unlike list, every value is represented by a key.
A dictionary can contain many key-value pairs. Each pair is represented by a key, a colon symbol and its value.
Multiple pairs, are separated by commas.
lets see below:
"""

my_dict = {
    "name": "Jon",
    "color": "Yellow",
    "Phone": 123,
}

print(my_dict)      # you can print entire dictionary

# 1. Accessing a value. you can access single value by two ways:

print(my_dict["name"])      # key name passed in square brackets

print(my_dict.get("Phone")) # using the built in get function


# 2. Add or update new value 

my_dict["color"] = "black"
print(my_dict)


# 3. Delete: Can be done in three ways

del my_dict["color"]        # deleteing the key value pair with key 'color'
print(my_dict)

my_dict.pop("Phone")        # using the pop function and passing the key name as paramter
print(my_dict)

my_dict.clear()             # erase all value pairs in the dictionary
print(my_dict)


# 4. View all keys in dictionary

my_dict = {
    "fruit": "Apple",
    "color": "pink",
    "number": 0,
    "sky": "blue"
}

print(my_dict.keys())       # prints all keys in the dict


# 5. dict of dict

nested_dict = {
    "my_dict" : { "nested_key": "nested_value" },
    "outer_key": "outer_value",
}

#print(nested_dict)

# this is the nested dictionary, or dictionary of dictionaries.

# explore more built in functions of dictionaries for better practise.

