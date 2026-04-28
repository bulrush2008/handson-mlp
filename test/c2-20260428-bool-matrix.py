
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a < 5
print(b)

c = b.sum(axis=1)
print(c)
