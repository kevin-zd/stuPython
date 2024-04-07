"""
    @project: stuPython
    @Author：Murk
    @file： 10-4 函数的参数定义.py
    @date：2024/4/7 20:22
    @Desc: 
"""
print('*'*8+'函数定义默认值参数'+'*'*8)
def fun(a, b=10):
    print(a, b)

# 函数的调用
fun(100)       # 只传一个参数，b采用默认值
fun(20, 30)    # 30将默认值10替换


print('hello', end='\t')
print('python')

print('*'*8+'个数可变的位置参数'+'*'*8)
def fun(*args):    # 函数定义时，可变的位置参数
    print(args)
    # print(args[0])

fun(10)
fun(10, 20, 30)

print('*'*8+'个数可变的关键字参数'+'*'*8)
def fun(**args):
    print(args)

fun(a=10)
fun(a=10, b=20, c=30)

'''
def fun(*args, *a):
    pass
以上代码，程序会报错，个数可变的位置参数，只能是1个

def fun(**args, **a):
    pass
以上代码，程序会报错，个数可变的关键字参数，也只能是1个
'''
def fun(*args1, **args2):
    pass

'''
def fun(**ars1, *args2):
    pass
在一个函数的定义过程中，即有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
'''