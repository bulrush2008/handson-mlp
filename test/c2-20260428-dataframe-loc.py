
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df)

print("取行---------")
print(df.loc[[0,2]])  # 取 0&2 两行
print(df.loc[np.array([0,2])])  # 取 0&2 两行

print("取列---------")
print(df["A"])
