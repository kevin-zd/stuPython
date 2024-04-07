"""
    @project: stuPython
    @Author：Murk
    @file： 10-3 函数的返回值.py
    @date：2024/4/7 20:10
    @Desc: 
"""

print(bool(0))    # False
print(bool(8))    # True

def fun(num):
    odd = []   # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

print(fun([10, 29, 34, 23, 44, 53, 55]))

'''
函数的返回值：
    （1）如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】 return 可以省略不写
    （2）函数的返回值，如果是1个，直接返回类型
    （3）函数的返回值，如果是多个，返回的结果为元组
'''
print('-'*8+'情况1'+'-'*8)
def fun1():
    print('hello')

fun1()

print('-'*8+'情况2'+'-'*8)
def fun2():
    return 'hello'

res = fun2()
print(res)

print('-'*8+'情况3'+'-'*8)
def fun3():
    return 'hello', 'world'
print(fun3())

'''函数在定义时，是否需要返回值，视情况而定'''

