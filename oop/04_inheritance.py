"""
Like you might have studied inheritance in other languages like c++, java etc.

The basic concept is the same, that the child class inherits all the properties from the parent class.

The child class can have separate implementations of the functionalities, or they can simply use the funcionalities
provided by the parent class.

The inheritance relation can be understand by the 'is - a' concept. Every student 'is a' person. Thus, student class
can inherit person class.

Lets look at example below to understand it more.
"""

class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def declaration(self):
        print("This is person class")


class Student(Person):  #   to inherit person class, all the student class has to do is mention it in the class paramters.
    #   if the student class does not want to separately implement __init__, the object
    #   of student class will call student classs' constructor, which will automatically pass the
    #   variables to parent class person
    pass


std_obj = Student(101, 'Jon')

print(std_obj.id, std_obj.name)