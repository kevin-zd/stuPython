"""
了解如何在Python中处理异常，以及如何使用try-except语句捕获异常。
"""

'''
在Python中，异常处理是一种机制，用于在程序出现错误时进行恰当的处理，以避免程序崩溃或产生不可预知的结果。
以下是Python中处理异常的基本用法：
'''

# 1.使用try-except语句捕获异常：可以使用try-except语句来捕获可能出现的异常，并在发生异常时执行相应的处理。
try:
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    result = num1 / num2
    print("结果为：", result)
except ZeroDivisionError:
    print("除数不能为0！")
except ValueError:
    print("请输入整数！")

'''
在上面的示例中，我们使用try-except语句来尝试执行一些可能会出现异常的代码。首先，我们使用input()函数读取两个整数，并尝试将它们相除。
如果除数为0，则会抛出ZeroDivisionError异常；如果输入的不是整数，则会抛出ValueError异常。
在except语句中，我们分别捕获这两种可能的异常，并在发生异常时输出相应的提示信息。
'''

# 2.使用finally语句进行清理操作：可以使用finally语句来定义一些无论是否发生异常都需要执行的代码，例如释放资源、关闭文件等。
file = None
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件不存在！")
finally:
    if file:
        file.close()

'''
在上面的示例中，我们使用try-except语句打开一个名为test.txt的文件，并尝试读取文件内容。如果文件不存在，则会抛出FileNotFoundError异常。
无论是否发生异常，我们都使用finally语句来关闭文件，以释放资源。

通过上面的示例，我们可以看到，在Python中处理异常非常简单、直观。
合理地使用异常处理可以让我们的程序更加健壮、可靠，避免因为意外情况而导致程序崩溃或产生不可预知的结果。
'''


