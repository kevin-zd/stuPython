"""
掌握如何定义和调用函数，以及如何传递参数和返回值
"""
'''
在Python中，函数是一段可重用的代码块，用于执行特定的任务。
以下是Python中定义和调用函数的基本语法：
'''
# 1.定义函数：使用def关键字定义一个函数，并在函数体中编写相应的代码。
def greet(name):
    print("Hello, " + name + "!")

# 2.调用函数：使用函数名和参数列表来调用函数，并执行其中的代码。
greet("John")  # 输出Hello, John!

# 3.传递参数：可以在函数定义时指定参数，以接收外部传递的值。可以定义默认参数和可变参数，以满足不同的需求。
# 定义默认参数
def greet(name="world"):
    print("Hello, " + name + "!")

greet()  # 输出Hello, world!
greet("John")  # 输出Hello, John!

# 定义可变参数
def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(add(1, 2, 3))  # 输出6
print(add(4, 5, 6, 7))  # 输出22

# 4.返回值：可以在函数体中使用return语句返回一个值，以供外部调用者使用。
def add(a, b):
    return a + b

result = add(1, 2)
print(result)  # 输出3




