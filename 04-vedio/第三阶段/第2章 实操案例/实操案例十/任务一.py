"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/6/2 08:47
    @Desc: Mini计算器
"""
def calc(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return '除数不能为0！！！'

if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    op = input('请输入运算符：')
    print(calc(a, b, op))

"""
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
c = input('请输入第二个整数：')
if c == '+':
    add(a, b)
elif c == '-':
    sub(a, b)
elif c == '*':
    mul(a, b)
else:
    print('你输入的有误')
"""