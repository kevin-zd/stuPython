"""
    @project: stuPython
    @Author：Murk
    @file： 4.1 if语句.py
    @date：2024/2/21 16:10
    @Desc: 
"""

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print("Zero")
elif x == 1:
    print('Single')
else:
    print('More')
