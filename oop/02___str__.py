"""
__str__ function is declared in defined in a class.
It is used set what is to be returned when the class object is displayed or used as a string value.

Lets see an example to further understand its implementation.
"""

class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

    def __str__(self):
        return f"This is a {self.v_type}"


vehicle = Vehicle("Car")

#   print an object is see its string value we set up in __str__ funciton
print(vehicle)