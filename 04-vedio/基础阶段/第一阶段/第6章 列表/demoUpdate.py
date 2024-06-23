"""
    @project: stuPython
    @Author：Murk
    @file： demoUpdate.py
    @date：2024/4/5 08:23
    @Desc: 
"""
lst = [10, 20, 30, 40]
# 一次修改一个值
print(lst, id(lst))
lst[2] = 100
print(lst, id(lst))

lst[1:3] = [100, 200, 300, 400]
print(lst)