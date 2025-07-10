import numpy as np
arr = np.zeros(3)#1D array or list with 3 zeros
arr1 =np.zeros((3,4))#2d array or list with 3 rows and 4 column (or) it is a list of 3 lists each containing 4 zeros
print("1D array")
print(arr)

print("2D array")
print(arr1)

print(type(arr))# even though it is a 1D array it is considered as nD array
print(type(arr1))# even though it is a 2D array it is considered as nD array

print(arr[0])

print(arr1[1][3])

print(type(arr[2]))# this will be 64 bit float