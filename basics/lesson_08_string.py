"""
String is fascinating. in some languages, like cpp. string is used by calling a library.
python has built in str data type.
"""

var = "hi people.   "       # it declared using double or single quotation marks.

# there are many built in functions for str. lets explore them one by one.

print("Original String:", var)

print("Upper Case: ", var.upper())      # upper case the entire string

print("Lower Case: ", var.lower())      # lower case the entire string

print("Capitalize:", var.capitalize())  # capitalize first alphabet in the string

print("Title:", var.title())            # capitalize first alphabet of every word in the string

print("Count:", var.count('p'))         # count total occurances of any element

print("Presence:", "hi" in var)         # check if an alphabet or word is present in string. output is either true or false.

print("Replace:", var.replace("people", "world"))       # replace first paramter with second parameter

print("Slicing:", var[2:5])             # slice and select elements ffrom 2 to 5-1