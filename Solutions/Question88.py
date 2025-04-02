data_aggregation_data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 12, 35, 22, 18, 40],
    'Group': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z', 'Y', 'X', 'Z']
}

import pandas as pd
df=pd.DataFrame(data_aggregation_data)
category_mean=df.groupby("Category")["Value"].mean()
highest_average_category=category_mean.idxmax()
highest_average_value=category_mean.max()
print(highest_average_category,highest_average_value)