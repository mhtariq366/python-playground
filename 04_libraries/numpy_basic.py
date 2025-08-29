import numpy as np


##################### Creating arrays and indexing

arr1 = np.array([1,3,5]) # simple array with values and position

arr0 = np.zeros((2,3))   # an array of zeros, given the dimensions in parenthesis

arr2 = np.array([
    [1, 3, 5],
    [4, 5, 6],
    [7, 8, 9]
    ]) # 2d array with values and position

arr3 = np.array([
    [
    [1, 3, 5]
    ],
    [
    [4, 5, 6]
    ],
    [
    [7, 8, 9]
    ]
    ]) # 3d array with values and position

arr_mutli = np.array([1, 4, 7], ndmin=5)    # stating dimensions manually

print(arr_mutli)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr[1,3])     # row 1, 3rd element

print(arr[0,-1])     # row 0, last element

##################### Array slicing

arr = np.array([1,3,5,7,9,11])

print(arr[3:5:1])   # array slicing, arr[start:end:step]

print(arr[::])     # if start not given, assume 0. if end not given, assume total length. if step not given assume 1.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr[0:2, 1:3])    # for both rows, slice 1 to 3 indexes.

##################### Data types
# all python allowed data types can be used in numpy arrays