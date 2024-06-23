"""
    @project: stuPython
    @Author：Murk
    @file： 2-6 特殊方法和特殊属性.py
    @date：2024/4/14 13:50
    @Desc: 
"""
print(dir(object))
class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建C类的对象
x = C('Jack', 20)    # x是C类型的一个实例对象
print(x.__dict__)    # 实例对象的属性字典
print(C.__dict__)
print('-'*8)
print(x.__class__)    # 输出类对象所属的类
print(C.__bases__)    # C类的父类类型的元素
print(C.__base__)     # 类的基类  A
print(C.__mro__)      # 类的层次结构
print(A.__subclasses__())  # 子类的列表