import numpy as np
arr = np.full((3,3),4)# this creates a nD array that is 3x3 and all the elements are 4
print(arr)
print(type(arr))
print(type(arr[2][2]))# this will be an int by default
# we can specify which data type it can be
arr1 = np.full((3,3),5,dtype=float)
print(arr1)
print(type(arr1))
print(type(arr1[2][2]))# this will be float