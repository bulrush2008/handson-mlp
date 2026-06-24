# 学习可迭代对象（Iterable） vs 迭代器（Iterator）

# 一句话区分：
#   - 可迭代对象（Iterable）：能提供迭代器的东西      → 可以 for 遍历
#   - 迭代器（Iterator）：能记住遍历位置的东西          → 可以一个接一个取值

# 更形象地理解：
#   - 可迭代对象就像一本书                → 它可以被阅读
#   - 迭代器就像书签                      → 它知道读到哪里了，并且每次翻一页

from collections.abc import Iterable, Iterator

# ====================================================================
# 例1：list 是可迭代对象，但不是迭代器
# ====================================================================
lst = [1, 2, 3]
print("=== list：可迭代对象，但不是迭代器 ===")
print(f"list 是 Iterable? {isinstance(lst, Iterable)}")   # True
print(f"list 是 Iterator? {isinstance(lst, Iterator)}")   # False

# 可以用 for 遍历（因为 list 实现了 __iter__() 方法）
for x in lst:
    print(f"  {x}")

# 但是直接对 list 用 next() 会报错
# next(lst)  # TypeError: 'list' object is not an iterator

# ====================================================================
# 例2：通过 iter() 从可迭代对象获取迭代器
# ====================================================================
print("\n=== iter() 从 list 获取迭代器 ===")
it = iter(lst)   # 等价于 lst.__iter__()
print(f"迭代器 it 是 Iterable? {isinstance(it, Iterable)}")   # True
print(f"迭代器 it 是 Iterator? {isinstance(it, Iterator)}")   # True

print("用 next() 一个一个取：")
print(f"  next(it) = {next(it)}")   # 1
print(f"  next(it) = {next(it)}")   # 2
print(f"  next(it) = {next(it)}")   # 3
# print(f"  next(it) = {next(it)}")  # StopIteration 异常：迭代器用完了

# 关键区别：迭代器是有状态的！它记住了当前取到哪里
# 而 list 本身没有这个"当前读到哪"的状态

# ====================================================================
# 例3：迭代器的特性 —— 一次性消费
# ====================================================================
print("\n=== 迭代器是一次性的 ===")
it2 = iter([10, 20, 30])
print(f"第一次遍历：{list(it2)}")   # [10, 20, 30]
print(f"第二次遍历：{list(it2)}")   # []  —— 已经空了

# 对比：可迭代对象（比如 list）可以反复遍历
lst2 = [10, 20, 30]
print(f"list 第一次遍历：{list(lst2)}")     # [10, 20, 30]
print(f"list 第二次遍历：{list(lst2)}")     # [10, 20, 30] —— 还在

# ====================================================================
# 例4：zip() 返回的就是迭代器
# ====================================================================
print("\n=== zip() 返回的是迭代器 ===")
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(f"zip 是 Iterable? {isinstance(z, Iterable)}")   # True
print(f"zip 是 Iterator? {isinstance(z, Iterator)}")   # True

print(f"遍历 zip：{list(z)}")   # [(1, 'a'), (2, 'b'), (3, 'c')]
print(f"再次遍历 zip：{list(z)}")   # [] —— 一次性的！

# ====================================================================
# 例5：range() 是可迭代对象，但不是迭代器
# ====================================================================
print("\n=== range 是可迭代对象，不是迭代器 ===")
r = range(3)
print(f"range 是 Iterable? {isinstance(r, Iterable)}")   # True
print(f"range 是 Iterator? {isinstance(r, Iterator)}")   # False
print(f"range 可以反复遍历：{list(r)}")   # [0, 1, 2]
print(f"range 可以反复遍历：{list(r)}")   # [0, 1, 2]

# ====================================================================
# 例6：自己实现一个迭代器 —— 理解原理
# ====================================================================
print("\n=== 手动实现一个迭代器 ===")

# 模拟 range(3) 的迭代过程
class MyRange:
    """可迭代对象：可以用 for 遍历"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):           # 返回一个迭代器
        return MyRangeIterator(self.n)

class MyRangeIterator:
    """迭代器：知道遍历到哪里了"""
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):           # 迭代器本身也是可迭代的
        return self

    def __next__(self):           # 核心方法：每次返回下一个值
        if self.current >= self.n:
            raise StopIteration    # 结束信号
        value = self.current
        self.current += 1          # 记住当前读到哪了
        return value

from collections.abc import Iterable, Iterator

# 验证核心判断
my_iterator = iter([1, 2, 3])
print(f"迭代器是 Iterable? {isinstance(my_iterator, Iterable):>5}")   # True
print(f"迭代器是 Iterator? {isinstance(my_iterator, Iterator):>5}")   # True

my_list = [1, 2, 3]
print(f"列表是   Iterable? {isinstance(my_list, Iterable):>5}")       # True
print(f"列表是   Iterator? {isinstance(my_list, Iterator):>5}")       # False

# 测试
my_range = MyRange(3)
print("自定义 MyRange 用 for 遍历：")
for x in my_range:       # 隐式调用 iter(my_range) 获取迭代器
    print(f"  {x}")

# 手动使用迭代器
print("手动 next()：")
it = iter(MyRange(3))    # 等价于 MyRange(3).__iter__()
print(f"  next1 = {next(it)}")    # 0
print(f"  next2 = {next(it)}")    # 1
print(f"  next3 = {next(it)}")    # 2

# ====================================================================
# 总结对比
# ====================================================================
#                | 可迭代对象 Iterable        | 迭代器 Iterator
# --------------|---------------------------|---------------------------
# 能否 for 遍历   | ✓ 能                      | ✓ 能
# 能否 next() 取值 | ✗ 不能                    | ✓ 能
# 能否反复遍历     | ✓ 能（每次重新产生新迭代器） | ✗ 不能（一次性消费）
# 是否有状态       | ✗ 没有状态                 | ✓ 记住当前遍历位置
# 关键方法         | __iter__()                | __iter__() + __next__()
# 常见例子         | list, tuple, str, dict,   | 文件对象, zip(), map(),
#                 | set, range, np.array      | filter(), iter() 返回值
#
# 一句话：
#   可迭代对象 = 有原材料（有数据）
#   迭代器    = 有原材料 + 有书签（记住读到哪了 + 能取下一个）
#
# for x in obj 的工作原理：
#   1. 调用 iter(obj) 获取迭代器
#   2. 不断调用 next(迭代器) 取值，直到 StopIteration