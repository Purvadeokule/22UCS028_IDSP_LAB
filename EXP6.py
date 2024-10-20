# A simple lambda function to multiply two numbers
multiply = lambda x, y: x * y
print("Multiplication of 7 and 4:", multiply(7, 4))

# Using lambda with map to find the cube of each number in a list
numbers = [2, 4, 6, 8, 10]
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print("\nCubed Numbers:", cubed_numbers)
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nEven Numbers:", even_numbers)
# Calculate factorial using reduce
from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print("\nFactorial of 5:", factorial(5))
# Sort a list of tuples by the second element
tuples_list = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print("\nSorted Tuples by Second Element:", sorted_tuples)
# Convert a list of strings to uppercase using map
words = ['hello', 'world', 'python', 'lambda']
uppercase_words = list(map(lambda x: x.upper(), words))
print("\nUppercase Words:", uppercase_words)
# Filter palindromes from a list of strings
words = ['level', 'world', 'deed', 'python', 'noon']
palindromes = list(filter(lambda x: x == x[::-1], words))
print("\nPalindromes:", palindromes)
# Calculate powers of numbers in a list
base = 3
numbers = [1, 2, 3, 4, 5]
powers = list(map(lambda x: base ** x, numbers))
print(f"\nPowers of {base}:", powers)
