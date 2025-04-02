data_integration_data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Price': [1.0, 0.5, 2.0, 1.5, 2.5]
}
data_integration_data2 = {
    'ID': [3, 4, 5, 6, 7],
    'Quantity': [10, 20, 30, 40, 50],
    'Location': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
}

import pandas as pd
df1=pd.DataFrame(data_integration_data1)
df2=pd.DataFrame(data_integration_data2)

df3=pd.merge(df1,df2,how="inner",on="ID")
df3_average_quantity=df3.groupby("Product")["Quantity"].mean().reset_index()
print(df3_average_quantity)