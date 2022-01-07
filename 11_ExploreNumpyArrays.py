# Command to install numpy packages
# pip install numpy

# So in this doc we will be exploring the image processing using numpy and some functions of numpy

import numpy

# This is a normal python list
mylist = [[123,333,44,33,55],[],[]]
print(mylist)

# O/P : [[123, 333, 44, 33, 55], [], []]

# This will create a 1-D numpy array
n = numpy.arange(27)
print(n)

# O/P : [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26]

type(n) # the type is ndarray, which is numpy array
# O/P  numpy.ndarray

# To create the numpy 2-D array
np2Darray = n.reshape(3,9)
np2Darray

# O/P :- 
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
#        [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23, 24, 25, 26]])



# Create 3-D numoy array 
np3Darray = n.reshape(3,3,3)
np3Darray

# O/P 
# array([[[ 0,  1,  2],
#         [ 3,  4,  5],
#         [ 6,  7,  8]],

#        [[ 9, 10, 11],
#         [12, 13, 14],
#         [15, 16, 17]],

#        [[18, 19, 20],
#         [21, 22, 23],
#         [24, 25, 26]]])

# Now suppose you want to perform some actions may be calucating the BMI of a table using python list
height = [12.3, 34.4, 34.3, 23.33, 23]
weight = [334.3, 324.55, 444.55, 344.4, 344.9]

BMI = weight / height ** 2
print(BMI)

# NOTE: Error message :- TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

# Easy way to doing this is to convert the python list to numpy array

npheight = numpy.array(height)
print(npheight)
type(npheight)

# O/P :- [12.3  34.4  34.3  23.33 23.  ]
# numpy.

npweight = numpy.array(weight)
print(npweight)
type(npweight)

# O/P :- [334.3  324.55 444.55 344.4  344.9 ]
# numpy.ndarray

npBMI = npweight / npheight ** 2
npBMI # easy way to perform any calulation using the numpy array, so numpy array has the ability to perform the 
# any calculation over the array table

# array([2.20966356, 0.27426143, 0.37786127, 0.6327522 , 0.65198488])

# Suppose you tried to create different types of values inside the numpy array then, it will bydefult change the value 
# to sting
numpy.array([12.2, 2, 'Sri', True])

# O/P :- array(['12.2', '2', 'Sri', 'True'], dtype='<U32')

# Suppose you tired to add 2 python arrays, then it will merge the array
arrayval = height + weight
print(arrayval)

# However, if we are adding 2 numpy array, then it will add the arrays value
nparrayval = npheight + npweight
print(nparrayval)

# O/P :
# [12.3, 34.4, 34.3, 23.33, 23, 334.3, 324.55, 444.55, 344.4, 344.9]
# [346.6  358.95 478.85 367.73 367.9 ]


# Extract a particular value from the nparray BMI
npBMI[2]

# O/P :- 0.3778612652891228

# Conditions in nparray 
npBMI[npBMI > 0.02]

# O/P :- array([2.20966356, 0.27426143, 0.37786127, 0.6327522 , 0.65198488])

# Explore the numpy 2D array
print(np2Darray)
np2Darray.shape # this lets you matrix of the 2D nparray

# O/P :
# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]
# (3, 9)

# Now suppose you want to access the 0th row of the 2D nparray
np2Darray[0]

# O/P array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Now suppose you want to access the 4th index column of 2D nparray
np2Darray[:,4]

# O/P :- array([ 4, 13, 22])

# Now suppose you want to access the 2nd index row of 3rd index column
np2Darray[2,3]

# O/P :- 21

# Suppose you want to select the 2nd index row and 1st index column till 4th index column
np2Darray[:, 1:4]

# O/P
# array([[ 1,  2,  3],
#        [10, 11, 12],
#        [19, 20, 21]])

# Or suppose you want to select the 0th index and 2nd index row of only 2nd index column
np2Darray[0:2,2]

# O/P : array([ 2, 11])


# Iterating through the numpy array 
for i in np2Darray:
    print(i)     # this is iterating through row.

# O/P :-
# [0 1 2 3 4 5 6 7 8]
# [ 9 10 11 12 13 14 15 16 17]
# [18 19 20 21 22 23 24 25 26]

# Iterate through column
for i in np2Darray.T:
    print(i)

# O/P :-
# [ 0  9 18]
# [ 1 10 19]
# [ 2 11 20]
# [ 3 12 21]
# [ 4 13 22]
# [ 5 14 23]
# [ 6 15 24]
# [ 7 16 25]
# [ 8 17 26]

# Iterate one by one value
for i in np2Darray.flat:
    print(i)

# O/P :- 
# 0
# 1
# 2
# 3
# 4
# 5 
# .
# .
# 26

# Suppose you want to merge or join 2 numpy array
# So, there is 2 types of joining 
# a) Horizontal
# b) Vertical

# a) Horizontal Joining 
horijoin = numpy.hstack((np2Darray, np2Darray)) # So, here in the argument we have a tuple of images that we are joining
print(horijoin)

# Suppose you want to merge or join 2 numpy array
# So, there is 2 types of joining 
# a) Horizontal
# b) Vertical

# Important NOTE : You can only the merge the array of same dimension, you cannot merge the array of
# different dimension

# Horizontal Joint or Merge
horijoin = numpy.hstack((np2Darray, np2Darray)) # So, here in the argument we have a tuple of images that we are joining
print(horijoin)

# O/P :-
# [[ 0  1  2  3  4  5  6  7  8  0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17  9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26 18 19 20 21 22 23 24 25 26]]

# Vertical Joint or Merge
vertjoin = numpy.vstack((np2Darray, np2Darray)) # So, here in the argument we have a tuple of images that we are joining and
# if you want you can increase the tuple size
print(vertjoin)

# O/P :-
# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]
#  [ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]

# Important NOTE : You can only the merge the array of same dimension, you cannot merge the array of
# different dimension
differentDimensionjoin = numpy.vstack((np2Darray, np2Darray, np3Darray)) # So, here in the argument we have a tuple of images that we are joining and
# if you want you can increase the tuple size
print(differentDimensionjoin)

# O/p :- 
# Error message 
# ValueError: all the input arrays must have same number of dimensions, 
# but the array at index 0 has 2 dimension(s) and the array at index 2 has 3 dimension(s)


# Spliting the numpy array
# So, there is 2 types of spliting 
# a) Horizontal split
# b) Vertical split

# a) Horizontal split
horisplit = numpy.hsplit(horijoin, 3)
print(horisplit) # Slpit the data into 3 parts 

# O/P :-
# [array([[ 0,  1,  2,  3,  4,  5],
#        [ 9, 10, 11, 12, 13, 14],
#        [18, 19, 20, 21, 22, 23]]), 
# array([[ 6,  7,  8,  0,  1,  2],
#        [15, 16, 17,  9, 10, 11],
#        [24, 25, 26, 18, 19, 20]]),
# array([[ 3,  4,  5,  6,  7,  8],
#        [12, 13, 14, 15, 16, 17],
#        [21, 22, 23, 24, 25, 26]])]

# b) Vertical split
vertsplit = numpy.vsplit(vertjoin, 3)
print(vertsplit) # Slpit the data into 3 parts 

# O/P
# [array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
#        [ 9, 10, 11, 12, 13, 14, 15, 16, 17]]), 
# array([[18, 19, 20, 21, 22, 23, 24, 25, 26],
#        [ 0,  1,  2,  3,  4,  5,  6,  7,  8]]), 
# array([[ 9, 10, 11, 12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23, 24, 25, 26]])]

