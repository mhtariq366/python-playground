"""
File handling refers to managing files, including operations such as read, write append or create file etc.
Mostly two types of file read or write modes are used, text and binary.
Lets see how file is created, read, and more.
"""

"""
to read a file in python, the 'open' function is used. Within its paramter, pass the file path or name.
if the file is in the same folder as the python file, just write the file name as written below.
lets suppose if file is in a folder named 'datasets', then write entire path as 'datasets/file_handling.txt'
"""


f_obj = open('file_handling.txt')
#   this way, file is opened. but it needs to be closed explicitly later on.


"""
the file object can be named as any variable named. we named it 'f_obj'. The file content is now in this object.
use the read() function on file object, as below.
the read() function is used to read the entire file in one time.
to read the file line by line, use the readline() function.
Lastly, to read the entire file into a list, use the readlines() functions. This will create a list of all lines, with each
line as an element in the list.
Below all three functions are written. Use one while commenting the other two to see the difference.
"""
#print(f_obj.read())

print(f_obj.readlines())

#print(f_obj.read())


#   to close. use the 'close()' function of file object.
f_obj.close()


"""
we have seen 
"""
