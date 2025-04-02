statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

import pandas as pd
df=pd.DataFrame(statistics_data)

Q1=df["Values"].quantile(0.25)
Q3=df["Values"].quantile(0.75)

IQR=Q3-Q1
print("Inter Quartile Range:",IQR)