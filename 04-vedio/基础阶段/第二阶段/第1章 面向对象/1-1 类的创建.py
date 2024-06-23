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

print(id(Student))
print(type(Student))
print(Student)

print('-' * 8 + '创建类的对象' + '-' * 8)
stu1 = Student('张三', 20)
print(stu1)
stu1.info()  # 对象名.方法名()
stu1.sm()
stu1.cm()
print(stu1.name)
print(stu1.age)
Student.info(stu1)  # 43行和38行代码功能相同，都是调用Student中info方法
# 类名.方法名(类的对象) --> 实际上就是方法定义处的self


