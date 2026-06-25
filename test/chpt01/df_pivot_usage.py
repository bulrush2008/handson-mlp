
import pandas as pd

# 原始数据：每个学生、每个科目一行（长格式）
data = {
    'Student': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'English', 'Math', 'English', 'Math', 'English'],
    'Score': [85, 90, 78, 82, 95, 88]
}
df = pd.DataFrame(data)

# pivot：以 Student 为行索引，Subject 为列，Score 为值
pivoted = df.pivot(index='Student', columns='Subject', values='Score')

#pivoted.columns.name = None  # 去掉列索引的名称
pivoted.reset_index(inplace=True)  # 将行索引恢复为普通列

print("原始DataFrame（长格式）:")
print(df)
print("-"*40)
print("\n透视后的DataFrame（宽格式）:")
print(pivoted)
print("-"*40)
print(pivoted["Math"])  # 访问 Math 列
print("-"*40)