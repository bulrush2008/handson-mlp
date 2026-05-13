
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(np.sum(a, axis=0))    # 15
print("-" * 50)

b = np.array([[1, 2], [3, 4], [5, 6]])
print(np.sum(b, axis=0))    # [ 9 12]
print(np.sum(b, axis=1))    # [ 3  7 11]
print("-" * 50)

# 3 dimensional array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(np.sum(c, axis=0))    # [[ 6  8]
                            #  [10 12]]
print("-" * 50)