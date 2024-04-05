"""
    @project: stuPython
    @Author：Murk
    @file： 8-3 集合的创建方式.py
    @date：2024/4/5 18:07
    @Desc: 
"""
print('-'*8+'第一种创建方式使用{}'+'-'*8)
s = {2, 3, 3, 3, 5, 6, 7}    # 集合中的元素不允许重复
print(s)

print('-'*8+'第二种创建方式使用set()'+'-'*8)
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 4, 5, 6, 6, 6, 7])
print(s2, type(s2))

s3 = set((11, 2, 3, 3, 4, 5, 65))     # 集合中的元素是无序的
print(s3, type(s3))

s4 = set('python')
print(s4, type(s4))

s5 = set({11, 2, 3, 3, 4, 7})
print(s5, type(s5))

''' 定义一个空集合 '''
s6 = {}     # dict字典类型
print(type(s6))

s7 = set()
print(type(s7))