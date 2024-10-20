import pandas as pd

# Sample data to create a DataFrame
data = {
    'Name': ['Purva', 'Revati', 'Sakshi', 'Prachi', 'Ahilya'],
    'Age': [28, 34, 23, 41, 37],
    'Salary': [55000, 62000, 47000, 78000, 66000],
    'Department': ['Sales', 'IT', 'Marketing', 'Finance', 'IT']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Get a list of the column headers
column_headers = df.columns.tolist()
print("\nColumn Headers:")
print(column_headers)

# 2. Delete a column by name
df.drop(columns=['Department'], inplace=True)
print("\nDataFrame after deleting 'Department' column:")
print(df)

# 3. Delete a column by index (e.g., index 1 which corresponds to 'Age')
df.drop(df.columns[1], axis=1, inplace=True)
print("\nDataFrame after deleting column at index 1:")
print(df)

# 4. Add a new column to the existing DataFrame
df['Location'] = ['Boston', 'Seattle', 'San Francisco', 'Houston', 'Chicago']
print("\nDataFrame after adding new 'Location' column:")
print(df)
