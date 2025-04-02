data_aggregation_data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 12, 35, 22, 18, 40],
    'Group': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z', 'Y', 'X', 'Z']
}

import pandas as pd
df=pd.DataFrame(data_aggregation_data)
df=df["Value"].mean()
print(df)