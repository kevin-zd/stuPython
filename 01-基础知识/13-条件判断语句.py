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


