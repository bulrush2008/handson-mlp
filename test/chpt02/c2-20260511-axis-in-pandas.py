
import numpy as np
import pandas as pd

"""
a = pd.Series([1, 2, 3, 4, 5])
print(a)
print(a.sum(axis=0))    # 15
print("-" * 50)
"""

b = pd.DataFrame([[1, 2, 7], [3, 4, 8], [5, 6, 9]], columns=['A', 'B', 'C'])
print("print b:")
print(b)
print("-" * 50)

print("b.sum(axis=0):")
print(b.sum(axis=0))    # A     9
                        # B    12
                        # C    24
                        # dtype: int64
print("b.sum(axis=1):")
print(b.sum(axis=1))    # 0     10
                        # 1     15
                        # 2     20
                        # dtype: int64
print("-" * 50)
print("b.drop(0, axis=0):")
print(b.drop(0, axis=0))    # drop row 0
print("b.drop('A', axis=1):")
print(b.drop('A', axis=1))    # drop column 'A'