
# 字典数据转化为 DataFrame
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)