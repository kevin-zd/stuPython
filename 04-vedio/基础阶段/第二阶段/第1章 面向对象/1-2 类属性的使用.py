"""
    @project: stuPython
    @Author：Murk
    @file： 1-1 类的创建.py
    @date：2024/4/13 16:13
    @Desc: 
"""


class Student:
    native_place = '上海'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def info(self):
        print('name is ：', self.name, 'age is：', self.age)

    # 类方法
    @classmethod
    def cm(cls):
        print('类方法')

    # 静态方法
    @staticmethod
    def sm():
        print('静态方法')

print('-' * 8 + '类属性的使用方式' + '-' * 8)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)

Student.native_place = '北京'
print(stu1.native_place)
print(stu2.native_place)

print('-' * 8 + '类方法的使用方式' + '-' * 8)
Student.cm()

print('-' * 8 + '静态方法的使用方式' + '-' * 8)
Student.sm()


