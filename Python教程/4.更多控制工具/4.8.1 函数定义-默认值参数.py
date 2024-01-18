"""
    @project: stuPython
    @Author：Murk
    @file： 4.8.1 函数定义-默认值参数.py
    @date：2024/1/18 21:35
    @Desc: 
"""
""" 语法一： """


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


"""
该函数可以用以下方式调用：
只给出必选实参：ask_ok('Do you really want to quit?')
给出一个可选实参：ask_ok('OK to overwrite the file?', 2)
给出所有实参：ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
本例还使用了关键字 in ，用于确认序列中是否包含某个值。
"""
""" 语法二： """
# 默认值在 定义 作用域里的函数定义中求值
i = 5


def f(arg=i):
    print(arg)


i = 6
f()

""" 语法三： """
""" 重要警告： 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数： """
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# 不想在后续调用之间共享默认值时，应以如下方式编写函数：
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
