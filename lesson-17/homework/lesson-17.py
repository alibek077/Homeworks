import pandas as pd
import numpy as np

# Task 1
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# Task 2
print("First 3 rows:")
print(df.head(3))

# Task 3
mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

# Task 4
print("\nName and City:")
print(df[['first_name', 'City']])

# Task 5
df['Salary'] = [55000, 62000, 58000, 60000]  # random salary values

# Task 6
print("\nSummary Statistics:")
print(df.describe())


#2 Homework 2
sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
              'Sales': [5000, 6000, 7500, 8000],
              'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(sales_data)

# Task 2
print("\nMaximum Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].max())

# Task 3
print("\nMinimum Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].min())

# Task 4
print("\nAverage Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].mean())


#3 Homework 3
expense_data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
                'January': [1200, 200, 300, 150],
                'February': [1300, 220, 320, 160],
                'March': [1400, 240, 330, 170],
                'April': [1500, 250, 350, 180]}

expenses = pd.DataFrame(expense_data)
expenses = expenses.set_index('Category')

# Task 2
print("\nMaximum expense per category:")
print(expenses.max(axis=1))

# Task 3
print("\nMinimum expense per category:")
print(expenses.min(axis=1))

# Task 4
print("\nAverage expense per category:")
print(expenses.mean(axis=1))
