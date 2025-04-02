data_filtering_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 22, 35, 28, 40, 25, 32, 29, 31],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'New York', 'London', 'Tokyo', 'Paris', 'New York', 'London'],
    'Salary': [50000, 60000, 45000, 70000, 55000, 80000, 52000, 65000, 58000, 72000]
}

import pandas as pd
df=pd.DataFrame(data_filtering_data)

merged_df=df.merge(df,on="Age",how="inner",suffixes=("_left","_right"))

filtered_df=merged_df[merged_df["Name_left"]!=merged_df["Name_right"]]

result_df=df[df["Age"].isin(filtered_df["Age"])]

print(filtered_df)