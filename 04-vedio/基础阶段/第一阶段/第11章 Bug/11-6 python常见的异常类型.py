"""
    @project: stuPython
    @Author：Murk
    @file： 11-6 python常见的异常类型.py
    @date：2024/4/9 20:11
    @Desc: 
"""
# 数学运算异常
print(10/0)     # ZeroDivisionError

lst = [11, 22, 33, 44]
print(lst[4])     # IndexError   索引从0开始

dic = {'name': '张三', 'age': 20}
print(dic['gender'])      # KeyError

# print(num)   # NameError

# int a = 20   # SyntaxError

a = int('hello')  # ValueError