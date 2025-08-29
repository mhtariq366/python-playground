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
we have seen that we have to explicitly close the file once we are done with the file.
to ease this, we now use the 'with' keyword to open file.
"""
with open('file_handling.txt') as f_obj:
    print(f_obj.read())


"""
since we have been using a text file, we did not need to write modes in the open function.
Modes are to indicate what we are going to do with the file. Modes are as follows:
r   read
w   write
t   text file
b   binary file
a   append
x   create
lets use the read mode.
"""
print('Start using modes:')

with open('file_handling.txt', 'rt') as f_obj:  #   we use mode r and t. this means read text file 
    print(f_obj.read())


"""
lets now create a new file. We are using the create mode.
The below code will create a new file in the same folder as the python file.
if using the create mode named 'x'. The new file can only be created if the file with same path and file name does not exist already.
If the file with same path and name already exists, then an error will be raised.
"""

with open('newfile_text.txt', 'x') as f_obj:
    f_obj.write('New file using create mode')


"""
Now we will look at writing in the file. We will use the new file created just above.
"""
with open('newfile_text.txt', 'w') as f_obj:
    f_obj.write('Writing in new file')

"""
After running the code to write in the new file. You can see that the text written in above line when new file was being created has been overwritten by the write file lines above.
To avoid this issue, if your use case demands to not over write an already written file, then do not use the write mode. instead, use the append mode. lets try it.
"""

with open('newfile_text.txt', 'a') as f_obj:
    f_obj.write('\nAppending in the new file.')

