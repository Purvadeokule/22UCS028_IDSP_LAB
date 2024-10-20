import numpy as np

# Create a NumPy array
array = np.array([10, -20, 30, -40, 50])
print("Original Array:")
print(array)

# Unary Operations
# Negation
negated_array = -array
print("\nNegated Array:")
print(negated_array)

# Absolute value
absolute_array = np.abs(array)
print("\nAbsolute Value of Array:")
print(absolute_array)

# Square root (note: applying it to non-negative values)
sqrt_array = np.sqrt(absolute_array)
print("\nSquare Root of Absolute Values:")
print(sqrt_array)

# Exponential
exp_array = np.exp(array)
print("\nExponential of Array:")
print(exp_array)

# Sine values
sin_array = np.sin(array)
print("\nSine of Array:")
print(sin_array)

# Create two NumPy arrays of integers
array1 = np.array([8, 9, 10, 11])  # Binary: 1000, 1001, 1010, 1011
array2 = np.array([1, 2, 4, 8])    # Binary: 0001, 0010, 0100, 1000
print("\nArray 1:")
print(array1)
print("\nArray 2:")
print(array2)

# Bitwise AND
bitwise_and = array1 & array2
print("\nBitwise AND (array1 & array2):")
print(bitwise_and)

# Bitwise OR
bitwise_or = array1 | array2
print("\nBitwise OR (array1 | array2):")
print(bitwise_or)

# Bitwise XOR
bitwise_xor = array1 ^ array2
print("\nBitwise XOR (array1 ^ array2):")
print(bitwise_xor)

# Bitwise NOT
bitwise_not_array1 = ~array1
print("\nBitwise NOT (~array1):")
print(bitwise_not_array1)

bitwise_not_array2 = ~array2
print("\nBitwise NOT (~array2):")
print(bitwise_not_array2)

# Left Shift
left_shift = array1 << 1  # Shift bits to the left by 1
print("\nLeft Shift (array1 << 1):")
print(left_shift)

# Right Shift
right_shift = array1 >> 1  # Shift bits to the right by 1
print("\nRight Shift (array1 >> 1):")
print(right_shift)
