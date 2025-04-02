statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

import pandas as pd
df=pd.DataFrame(statistics_data)

max_value=df["Values"].max()
min_value=df["Values"].min()

print("Max_value:",max_value)
print("Min_value:",min_value)