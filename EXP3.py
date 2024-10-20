import numpy as np

arr = np.array([7.8, 2.5, 9.0, 4.4, np.nan])

# Length of the array, including nan
print("Length of array:", len(arr))  # It will print 5

# Maximum value in the array, will print nan
print("Maximum value (including nan):", arr.max())  # prints nan

# Maximum value ignoring nan
print("Maximum value (ignoring nan):", np.nanmax(arr))

# Summation of array elements, ignoring nan
print("Sum of elements (ignoring nan):", np.nansum(arr))

# Finding the average of array elements, ignoring nan
avg = np.nansum(arr) / np.count_nonzero(~np.isnan(arr))
print("Average (ignoring nan):", avg)
