"""
Objects are made to use the classes, its functions and member variables.
Without objects, class is just a blue print of members functions and variables.


"""

class Fruit:
    def __init__(self, name):
        self.name = name

    def fruit_name(self):
        print(f"Fruit name is {self.name}")


fruit_obj = Fruit('Apple')

#   you can call member function using object
fruit_obj.fruit_name()

#   member variable value can be changed using object
fruit_obj.name = 'Banana'
fruit_obj.fruit_name()

#   if in any case an object needs to be deleted, 'del' keyword is used.
del fruit_obj