"""
if 条件：
    条件成立执行的代码1
    ....
"""
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')
print('这个代码执行吗')

age = int(input("请输入你的年龄："))
if age > 18:
    print("可以进入网吧")
else:
    print("go out")

''' if 做判断 elif'''
age = int(input("请输入你的年龄："))
if age < 18:
    print(f'你输入的年龄是{age}，童工')
elif(age >= 18) and (age <= 60):
    print(f'你输入的年龄是{age}，合法')
elif age > 60:
    print(f'你输入的年龄是{age}，退休年龄')

''' if 做判断 elif  简化写法'''
age = int(input("请输入你的年龄："))
if age < 18:
    print(f'你输入的年龄是{age}，童工')
elif 18 <= age <= 60:
    print(f'你输入的年龄是{age}，合法')
elif age > 60:
    print(f'你输入的年龄是{age}，退休年龄')

""" if 嵌套 """
operator = str(input("请输入运算符："))
num1 = float(input("请输入第一个 数字："))
num2 = float(input("请输入第二个数字："))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print('输入的运算符不符合要求')
print(f'运算结果是：{round(result)}')



