"""
    @project: stuPython
    @Author：Murk
    @file： demoListIndex.py
    @date：2024/3/31 16:47
    @Desc: 
"""

lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))       # 如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
print(lst.index('world'))
print(lst.index('hello', 1, 4))
