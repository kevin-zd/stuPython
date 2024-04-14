"""
    @project: stuPython
    @Author：Murk
    @file： 2-5 多态.py
    @date：2024/4/14 11:39
    @Desc: 
"""
class Animal(object):
    def eat(self):
        print('eating')

class Dog(Animal):
    def eat(self):
        print('dog eating')

class Cat(Animal):
    def eat(self):
        print('cat is eating')

class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

# 定义一个函数
def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())