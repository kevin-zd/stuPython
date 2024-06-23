"""
    @project: stuPython
    @Author：Murk
    @file： 11-4 try-except-else的使用.py
    @date：2024/4/9 20:02
    @Desc: 
"""

try:
    a = int(input('input a :'))
    b = int(input('input b:'))
    result = a/ b
except BaseException as e:
    print('error :', e)
else:
    print('result = ', result)