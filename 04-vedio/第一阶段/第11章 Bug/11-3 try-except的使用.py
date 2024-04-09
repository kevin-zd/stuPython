"""
    @project: stuPython
    @Author：Murk
    @file： 11-3 try-except的使用.py
    @date：2024/4/9 19:54
    @Desc: 
"""
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第一个整数：'))
    result = a/ b
    print('result = ', result)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('end')