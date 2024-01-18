"""
    @project: stuPython
    @Author：Murk
    @file： 4.7 定义函数.py
    @date：2024/1/18 21:22
    @Desc: 
"""
# 创建一个可以输出限定数值内的斐波那契数列函数


def fib(n):
    a, b = 1, 2
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
fib(100)

# 不直接输出斐波那契数列运算结果，而是返回运算结果列表的函数


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib2(200))
