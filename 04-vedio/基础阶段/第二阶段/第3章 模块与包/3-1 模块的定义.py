"""
    @project: stuPython
    @Author：Murk
    @file： 3-1 模块的定义.py
    @date：2024/5/3 11:02
    @Desc: 
"""


def fun():
    pass

def fun2():
    pass

class Student:
    native_place = '上海'  # 类属性

    def eat(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

a = 10
b = 20
print(a + b)
