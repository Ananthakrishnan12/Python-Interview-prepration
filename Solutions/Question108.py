statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

import pandas as pd

df=pd.DataFrame(statistics_data)

df["Cummulative_sum"]=df["Values"].cumsum()

Covariance_values=df[["Values","Cummulative_sum"]].cov()
print(Covariance_values)