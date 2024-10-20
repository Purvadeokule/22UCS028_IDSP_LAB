import pandas as pd

# Sample data to create a DataFrame
data = {
    'Name': ['Purva', 'Revati', 'Sakshi', 'Prachi', 'Ahilya'],
    'Age': [24, 30, 22, 35, 29],
    'Salary': [50000, 60000, 45000, 70000, 65000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

age_filter = df.query('Age>25')
print("\nEmployees with Age greater than 25:")
print(age_filter)

# Multiple Condition Filtering

multiple_condition_filter = df.query('Department=="IT" & Salary>60000')
print("\nEmployees in 'IT' department with Salary greater than 60000:")
print(multiple_condition_filter)

# Another example of multiple conditions: Age less than 30 or Salary greater than 60000
another_multiple_condition_filter = df.query('Age<30 and Salary<60000')
print("\nEmployees with Age less than 30 or Salary greater than 60000:")
print(another_multiple_condition_filter)
