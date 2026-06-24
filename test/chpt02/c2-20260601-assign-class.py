
class MyClass:
    def __init__(self, value):
        self.value = value

    def add(self, x):
        return self.value + x

my_instance = MyClass(10)
add_method = my_instance.add  # add_method 是一个方法，它指向 my_instance 的 add 方法
print(add_method(5))  # 输出 15，因为 add_method(5) 实际上调用了 my_instance.add(5)

add_class = MyClass  # add_class 是一个类，它指向 MyClass 类
new_instance = add_class(20)  # new_instance 是 MyClass 的一个实例，它的 value 属性被设置为 20
print(new_instance.value)  # 输出 20，因为 new_instance 是 MyClass 的一个实例，value 属性被设置为 20

print(new_instance.add(5))  # 输出 25，因为 new_instance.add(5) 实际上调用了 MyClass 的 add 方法，使用 new_instance 的 value 属性（20）加上 5