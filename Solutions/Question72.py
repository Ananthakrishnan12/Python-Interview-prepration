data_manipulation_data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Value1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Value2': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
}

import pandas as pd
df=pd.DataFrame(data_manipulation_data)
df=df.drop(["Value2"],axis="columns")
print(df)