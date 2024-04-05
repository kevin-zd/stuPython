"""
    @project: stuPython
    @Author：Murk
    @file： 8-2 元组的常用操作.py
    @date：2024/4/5 17:59
    @Desc: 
"""
print('-'*8+'元组的遍历'+'-'*8)
t = ('python', 'world', 98)
''' 第一种获取元组的方式，使用索引 '''
print(t[0])
print(t[1])
print(t[2])

''' 遍历元组 '''
for item in t:
    print(item)
