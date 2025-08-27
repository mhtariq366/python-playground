
"""
The class is declared using the class keyword accompanied by the class name.

Each class have an __init__ function which will run, the very instant an object is created.
__init__ function is often used to assign values to the variables in class.

self keyword is used to refer to the current instance of the class. for example, self.v_type means that current objects v_type variable.
"""

class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

    def vehile_type(self):
        print(f"The vehile type is {self.v_type}")


vehicle = Vehicle("Car")    # create an object and pass the parameter to init function.
vehicle.vehile_type()       # calling class function