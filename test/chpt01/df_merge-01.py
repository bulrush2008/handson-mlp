
import pandas as pd

# 创建两个简单的DataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value2': [20, 40, 50, 60]
})

print("原始数据 df1:")
print(df1)
print("\n原始数据 df2:")
print(df2)

# 1. 内连接(inner)：只保留两个表中都有的键
inner_merged = pd.merge(df1, df2, on='key', how='inner')
print("\n内连接 (inner join):")
print(inner_merged)

# 2. 外连接(outer)：保留两个表中所有的键，缺失值用NaN填充
outer_merged = pd.merge(df1, df2, on='key', how='outer')
print("\n外连接 (outer join):")
print(outer_merged)

# 3. 左连接(left)：保留左表所有键，右表没有的键对应列为NaN
left_merged = pd.merge(df1, df2, on='key', how='left')
print("\n左连接 (left join):")
print(left_merged)

# 4. 右连接(right)：保留右表所有键，左表没有的键对应列为NaN
right_merged = pd.merge(df1, df2, on='key', how='right')
print("\n右连接 (right join):")
print(right_merged)