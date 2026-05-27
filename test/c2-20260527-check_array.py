
from sklearn.utils import check_array

a = [[1,2,3],[4,5,6],[7,8,9]]
b = check_array(a)
print(b)

#c = [1,2,3]
#d = check_array(c)  # This will raise an error because check_array expects a 2D array by default
#print(d)