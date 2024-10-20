import numpy as np

# Creating a multi-dimensional array
arr1 = np.array([[10, 20, 30], 
                 [40, 50, 60], 
                 [70, 80, 90]])
print("Original 2D Array:")
print(arr1)

# Creating 1D arrays
array_1 = np.array([3, 6, 9])
array_2 = np.array([2, 4, 8])

# Element-wise operations (squaring each element)
squared_array = array_1 ** 2
print("\nArray after squaring each element:")
print(squared_array)

# Dot product
dot_product = np.dot(array_1, array_2)
print("\nDot product of Array 1 and Array 2:", dot_product)

# Create a single NumPy array of zeros
array_zeros = np.zeros(7)  # 1D array with 7 zeros
print("\nSingle Array of Zeros:")
print(array_zeros)

# Create a single NumPy array of ones
array_ones = np.ones(7)  # 1D array with 7 ones
print("\nSingle Array of Ones:")
print(array_ones)
