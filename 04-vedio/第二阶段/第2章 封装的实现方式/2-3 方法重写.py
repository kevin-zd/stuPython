"""
    @project: stuPython
    @Author：Murk
    @file： 2-2 继承的实现.py
    @date：2024/4/14 11:08
    @Desc: 
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))

# 定义子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        super().info()
        print('学号：{0}'.format(self.score))

# 测试
stu = Student('Jack', 20, '1001')
stu.info()

# 多继承
class A(object):
    pass

class B(object):
    pass

class C(A, B):
    pass
