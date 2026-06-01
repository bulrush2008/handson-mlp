
def add(x, y):
    return x + y

a_plus_b = add  # a_plus_b 是个函数，它指向 add 函数
print(a_plus_b(1, 2))  # 输出 3

a_plus_b = add(1,2)
print(a_plus_b)  # 输出 3，因为 a_plus_b 现在是 add(1, 2) 的结果，而不是函数本身