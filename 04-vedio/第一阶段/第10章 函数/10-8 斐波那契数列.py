"""
    @project: stuPython
    @Author：Murk
    @file： 10-8 斐波那契数列.py
    @date：2024/4/7 21:35
    @Desc: 
"""
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 斐波那契数列第6位上的数字
n = fib(6)
print(n)

# 输出这个数列的前6位上的数字
for i in range(1, 7):
    print(fib(i))