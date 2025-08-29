"""
In this previous file in sequence named '04_inheritance_01. We discussed inheritance, and how the absence of constructor __init__
in child class automatically passes the control to parent class.

Now we see what happens when child class has its own constructor __init__
"""

class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def declaration(self):
        print("This is person class")

"""
In this child class below, it has its own default constructor __init__.
Now, a function 'super()' can be used to access all elements of the parent class. This way,
child class can use some attributes or function of parent class, as well as, can introduce its own
variations. In student class, using super() function, students' id and name is used from parent class.
while child class has its own new attribute classroom.
"""
class Student(Person):
    def __init__(self, id, name, classroom):
        super().__init__(id, name) 
        self.classroom = classroom
        
    def display(self):
        print (f"{self.id}, {self.name}, {self.classroom}")

std_obj = Student(101, 'Jon', 'A')

std_obj.display()