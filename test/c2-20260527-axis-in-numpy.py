
"""
总结：
- axis参数在numpy中表示沿着哪个轴进行操作：

- 在一维数组中，axis=0是唯一选择，
- 在二维数组中，axis=0表示沿着列方向进行操作，axis=1表示沿着行方向进行操作，
- 对于 n (n>=2) 维数组，轴索引从 0 到 n-1，分别对应从外层到内层的维度
"""


import numpy as np

a1 = np.array([1,2,3])
m1 = a1.mean(axis=0)
print(m1)

print('---' * 5)
a2 = np.array([[1,2,3],[4,5,6]])
m2 = a2.mean(axis=0)
print(m2)

print('---' * 5)
m2 = a2.mean(axis=1)
print(m2)