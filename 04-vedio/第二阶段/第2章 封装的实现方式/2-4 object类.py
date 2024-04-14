"""
    @project: stuPython
    @Author：Murk
    @file： 2-4 object类.py
    @date：2024/4/14 11:29
    @Desc: 
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))

    def __str__(self):
        return '姓名：{0}，年龄：{1}'.format(self.name, self.age)

o = object()
p = Person('Jack', 20)
print(dir(o))
print(dir(p))
print(p)

