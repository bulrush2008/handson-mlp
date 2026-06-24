"""
总结：
- 取行：使用 `loc`，单行返回 Series，多行返回 DataFrame。
- 取列：使用 `[]`，单列返回 Series，多列返回 DataFrame
"""
import pandas as pd

# 创造一个 DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df)

print("取行---------")
print("第0行:\n", df.loc[0], '\n', type(df.loc[0]))  # 取第 0 行 - series
print("第0行:\n", df.loc[[0]], '\n', type(df.loc[[0]]))  # 取第 0 行 - dataframe

print("第0行和第2行:\n", df.loc[[0,2]], '\n', type(df.loc[[0,2]]))  # 取 0&2 两行

print("取列---------")
print("列A:\n", df["A"], '\n', type(df["A"]))  # 取单列 - series
print("列A:\n", df[["A"]], '\n', type(df[["A"]]))  # 取单列 - dataframe
print("列A和列C:\n", df[["A","C"]], '\n', type(df[["A","C"]]))    # 取多列，注意：单列返回 Series，多列返回 DataFrame