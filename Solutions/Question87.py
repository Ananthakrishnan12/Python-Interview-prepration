data_aggregation_data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 12, 35, 22, 18, 40],
    'Group': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z', 'Y', 'X', 'Z']
}

import pandas as pd
df=pd.DataFrame(data_aggregation_data)
category_sum=df.groupby("Category")["Value"].sum()
overall_sum=category_sum.sum()
percentage=(category_sum/overall_sum)*100
print(percentage)