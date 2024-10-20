import numpy as np

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])

print("Original Array:")
print(array_2d)

# Basic indexing: Accessing a single element
element = array_2d[1, 2]  # Access the element in the 2nd row and 3rd column
print("\nElement at (1, 2):", element)

# Slicing: Accessing a sub-array
sub_array = array_2d[0:2, 1:3]  # Access rows 0 to 1 and columns 1 to 2
print("\nSliced Array (rows 0 to 1, columns 1 to 2):")
print(sub_array)

# Modifying elements using indexing
array_2d[0, 0] = 100  # Modify the element at (0, 0)
print("\nArray after modifying element at (0, 0):")
print(array_2d)

# Slicing to modify a sub-array
array_2d[1:3, 2:4] = [[20, 30], [40, 50]]  # Modify a sub-array
print("\nArray after modifying a sub-array (rows 1 to 2, columns 2 to 3):")
print(array_2d)

# Boolean indexing: Accessing elements based on a condition
bool_indexing = array_2d[array_2d > 10]  # Get all elements greater than 10
print("\nElements greater than 10:")
print(bool_indexing)
