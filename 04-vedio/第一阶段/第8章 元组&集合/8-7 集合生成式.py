"""
    @project: stuPython
    @Author：Murk
    @file： 8-7 集合生成式.py
    @date：2024/4/5 19:02
    @Desc: 
"""
'''列表生成式'''
lst = [i*i for i in range(1, 10)]
print(lst)

'''集合生成式'''
lst = {i*i for i in range(1, 10)}
print(lst)
