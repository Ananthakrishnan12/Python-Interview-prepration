statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

import pandas as pd
from scipy.stats import zscore
df=pd.DataFrame(statistics_data)

Z_scores_values=zscore(df["Values"])
print(Z_scores_values)