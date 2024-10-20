import re

# String Manipulation

# 1. Creating a string
text = "Hi there, my name is Purva."

# 2. Basic string operations
print("Original String:")
print(text)

# Length of the string
print("\nLength of the string:", len(text))

# Converting to uppercase
upper_text = text.upper()
print("\nUppercase:", upper_text)

# Finding a substring
substring = "Purva"
if substring in text:
    print(f"\nSubstring '{substring}' found at index:", text.index(substring))
else:
    print(f"\nSubstring '{substring}' not found.")

# Searching pattern in string
text = "Hi there, my email address is purva@domain.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print("\nFound email:", match.group())

# Replacing email with "REDACTED"
replaced_txt = re.sub(pattern, "REDACTED", text)
print("Replaced text:", replaced_txt)
