# 学习 Python 可迭代对象（Iterable）

# 可迭代对象：能用 for 循环遍历的对象
# 判断一个对象是否可迭代：可以用 isinstance(obj, Iterable) 检查
# 或者直接用 for ... in obj 实验

from collections.abc import Iterable

# --------------------------------------------------------------------
# 1. list（列表）—— 可迭代对象 ✓
# --------------------------------------------------------------------
list1 = [1, 2, 3]
print(f"list 是可迭代的: {isinstance(list1, Iterable)}")
for item in list1:
    print(f"  {item}")

# --------------------------------------------------------------------
# 2. array（数组）
#    Python 内置 array 模块中的 array
#    numpy 中的 np.ndarray
#    两种都是可迭代的 ✓
# --------------------------------------------------------------------
from array import array
arr = array('i', [10, 20, 30])   # int 类型数组
print(f"\n内置 array 是可迭代的: {isinstance(arr, Iterable)}")
for item in arr:
    print(f"  {item}")

import numpy as np
np_arr = np.array([100, 200, 300])
print(f"numpy array 是可迭代的: {isinstance(np_arr, Iterable)}")
for item in np_arr:
    print(f"  {item}")

# --------------------------------------------------------------------
# 3. dictionary（字典）—— 可迭代对象 ✓
#    默认迭代的是 key，不是 value
# --------------------------------------------------------------------
d = {"name": "Alice", "age": 30, "city": "Beijing"}
print(f"\ndict 是可迭代的: {isinstance(d, Iterable)}")
print("默认迭代 dict（遍历 key）：")
for key in d:
    print(f"  key = {key}")

print("遍历 value：")
for value in d.values():
    print(f"  value = {value}")

print("遍历 key-value 对：")
for k, v in d.items():
    print(f"  {k} -> {v}")

# --------------------------------------------------------------------
# 4. tuple（元组）—— 可迭代对象 ✓
# --------------------------------------------------------------------
t = (4, 5, 6)
print(f"\ntuple 是可迭代的: {isinstance(t, Iterable)}")
for item in t:
    print(f"  {item}")

# --------------------------------------------------------------------
# 5. str（字符串）—— 可迭代对象 ✓
# --------------------------------------------------------------------
s = "Python"
print(f"\nstr 是可迭代的: {isinstance(s, Iterable)}")
for ch in s:
    print(f"  {ch}")

# --------------------------------------------------------------------
# 6. set（集合）—— 可迭代对象 ✓
# --------------------------------------------------------------------
set1 = {7, 8, 9}
print(f"\nset 是可迭代的: {isinstance(set1, Iterable)}")
for item in set1:
    print(f"  {item}")

# --------------------------------------------------------------------
# 7. range —— 可迭代对象 ✓
# --------------------------------------------------------------------
r = range(3)  # 0, 1, 2
print(f"\nrange 是可迭代的: {isinstance(r, Iterable)}")
for i in r:
    print(f"  {i}")

# --------------------------------------------------------------------
# 8. 不可迭代的例子：int, float, bool
# --------------------------------------------------------------------
print(f"\nint 是可迭代的: {isinstance(42, Iterable)}")         # ×
print(f"float 是可迭代的: {isinstance(3.14, Iterable)}")      # ×
print(f"bool 是可迭代的: {isinstance(True, Iterable)}")       # ×

# --------------------------------------------------------------------
# 可迭代对象的本质
# --------------------------------------------------------------------
# 可迭代对象必须实现 __iter__() 方法，或 __getitem__() 方法
# 底层逻辑：
#   for x in obj:
#       等价于不断调用 iter(obj).__next__()
# 直到抛出 StopIteration 异常为止

# 手动模拟 for 循环：
print("\n手动模拟 for 循环遍历 list:")
it = iter([1, 2, 3])   # 获取迭代器
print(f"  next: {next(it)}")
print(f"  next: {next(it)}")
print(f"  next: {next(it)}")
# print(next(it))       # 如果取消注释，会抛出 StopIteration

# --------------------------------------------------------------------
# zip() 与可迭代对象的关系
# --------------------------------------------------------------------
# zip() 的参数可以是任何可迭代对象，不限于 list
# 常见的用法：

names = ["Alice", "Bob", "Charlie"]
scores = (85, 92, 78)       # tuple
grades = {"math", "eng", "cs"}  # set（注意：set 无序，顺序不一定对应）

zipped = zip(names, scores)    # zip list 和 tuple
print(f"\nzip(list, tuple): {list(zipped)}")

zipped2 = zip(names, "ABC")   # zip list 和 str
print(f"zip(list, str): {list(zipped2)}")

zipped3 = zip(names, range(100, 103))  # zip list 和 range
print(f"zip(list, range): {list(zipped3)}")

# 重要：zip() 返回的是迭代器（本身也是可迭代对象）
# 只能被遍历一次，用完就空了
z = zip([1, 2], ['a', 'b'])
print(f"\n第一次遍历 zip 结果: {list(z)}")  # [(1, 'a'), (2, 'b')]
print(f"第二次遍历 zip 结果: {list(z)}")  # []，已经空了