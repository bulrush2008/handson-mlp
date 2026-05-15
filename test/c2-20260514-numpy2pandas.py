
import numpy as np
import pandas as pd

a = np.array([[1, 2], [3, 4]])
#print(a)

pd_a = pd.DataFrame(a, columns=['col1', 'col2'], index=['row1', 'row2'])
print(pd_a)