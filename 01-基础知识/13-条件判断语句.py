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