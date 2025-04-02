data_filtering_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 22, 35, 28, 40, 27, 32, 29, 31],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'New York', 'London', 'Tokyo', 'Paris', 'New York', 'London'],
    'Salary': [50000, 60000, 45000, 70000, 55000, 80000, 52000, 65000, 58000, 72000]
}

import pandas as pd

df=pd.DataFrame(data_filtering_data)

df=df[df["Salary"]>60000].sort_values(by="Salary",ascending=True)
print(df)