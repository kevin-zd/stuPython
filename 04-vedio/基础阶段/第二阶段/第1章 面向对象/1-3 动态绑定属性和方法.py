"""
    @project: stuPython
    @Author：Murk
    @file： 1-3 动态绑定属性和方法.py
    @date：2024/4/13 20:09
    @Desc: 
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is a student")

stu1 = Student('张三', 20)
print(id(stu1))
stu2 = Student('李四', 46)
print(id(stu2))

print('-' * 8 + '为st2动态绑定性能' + '-' * 8)
stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

def show():
    print('定义在类之外的，称为函数')
stu1.show = show()
stu1.show()