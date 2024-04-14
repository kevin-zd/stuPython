"""
    @project: stuPython
    @Author：Murk
    @file： 2-7 特殊方法.py
    @date：2024/4/14 17:32
    @Desc: 
"""
a = 20
b = 100
c = a + b
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2     # 实现类两个对象的加法运算（因为在Student类中，编写__add__()特殊的方法）
print(s)

s = stu1.__add__(stu2)
print(s)

print('-'*8)
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
print(len(stu1))
