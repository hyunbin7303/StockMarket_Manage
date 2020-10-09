import numpy as np

array = np.arange(15).reshape(5,3)

#Reshape
# The dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension.
# For a matrix with n rows and m columns, shape will be (n,m).
# The length of the shape tuple is therefore the number of axes, ndim.
print(array)
# the number of axes(dimensions) of the array
print("THE THE NUMBER OF AXES : " + str(array.ndim))
print("DATA TYPE : " + array.dtype.name)

array2 = np.array([10,20,30,40])
print(array2)
print(np.arange(500))
