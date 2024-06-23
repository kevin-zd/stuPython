"""
    @project: stuPython
    @Author：Murk
    @file： 4-4range语句基础应用.py
    @date：2023/9/4 20:28
    @Desc: range()语句的基本使用

语法1:
range(num)
获取一个从0开始，到num结束的数字序列（不含num本身）
如range(5)取得的数据是：[0,1,2,3,4]

语法2:
range(num1,num2)
获取一个num1开始，到num2结束的数字序列（不含num2本身）
如，range(5,10)取得的数据是：[5,6,7,8,9]

语法3:
range(num1,num2,step)
获得一个从num1开始，到num2结束的数字序列（不含num2本身）
数字之间的步长，以step为准（step默认为1）
如，range(5,10,2)取得的数据是：[5,7,9]
"""

# range语法1，range(num)
for x in range(10):
    print(x)

# range语法2，range(num1,num2)
for x in range(5,10):
    print(x)

# range语法3，range(num1,num2,step)
for x in range(5,10,2):
    print(x)