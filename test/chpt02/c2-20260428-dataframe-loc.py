
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df)

print("取行---------")
print("第0行:\n", df.loc[0])  # 取第 0 行
print("第0行和第2行:\n", df.loc[[0,2]])  # 取 0&2 两行
print("第0行和第2行:\n", df.loc[np.array([0,2])])  # 取 0&2 两行

print("取列---------")
print("列A:\n", df["A"])  # 取单列
print("列A和列C:\n", df[["A","C"]])    # 取多列，注意：单列返回 Series，多列返回 DataFrame
