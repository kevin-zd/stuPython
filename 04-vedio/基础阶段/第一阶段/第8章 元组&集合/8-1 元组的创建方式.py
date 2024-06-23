"""
    @project: stuPython
    @Author：Murk
    @file： 8-1 元组的创建方式.py
    @date：2024/4/5 16:17
    @Desc: 
"""
''' 第一种创建方式，使用() '''
t = ('Python', 'world', 90)
print(t)
print(type(t))

# 省略小括号
t2 = 'Python', 'world', 92
print(t2)
print(type(t2))

t3 = ('Python',)
print(t3)
print(type(t3))

''' 第二种创建方式，使用内置函数tuple() '''
t1 = tuple(('python', 'world', 91))
print(t1)
print(type(t1))

''' 空元组、空列表的创建方式'''
lst = []
lst1 = list()

d = {}
d2 = dict()

''' 空元组'''
t4 = ()
t5 = tuple()
print('空列表：', lst, lst1)
print('空字典；', d, d2)
print('空元组：', t4, t5)

