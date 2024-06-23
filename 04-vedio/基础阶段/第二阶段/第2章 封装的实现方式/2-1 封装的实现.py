"""
    @project: stuPython
    @Author：Murk
    @file： 2-1 封装的实现.py
    @date：2024/4/14 10:58
    @Desc: 
"""


class Student:
    def __init__(self, age):
        self.__age = None
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 19
stu1 = Student(150)
stu2 = Student(30)
print(stu1.get_age())
print(stu2.get_age())