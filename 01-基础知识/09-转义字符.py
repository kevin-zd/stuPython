"""
Python中常见的转义字符包括：

\n：换行
\t：制表符
\r：回车
\\：反斜线
\’：单引号
\”：双引号
"""

'''
以下是一个示例代码，演示如何在Python中使用转义字符：
'''
print("Hello\tworld!")
print("This is a new\nline.")
print("This is a backslash: \\")
print("I\'m using a single quote.")
print("She said, \"Hello!\"")

"""
print的结束符
在Python中，print函数默认的结束符是换行符"\n"，可以通过指定end参数来修改结束符。以下是一个案例：
"""
# 输出一行文本，不换行
print("Hello, ", end="")
print("world!")  # 输出Hello, world!

# 输出一行文本，以逗号分隔
print("Python", "is", "awesome", sep=", ")  # 输出Python, is, awesome

'''
在上面的示例中，我们首先使用print函数输出两个文本片段，但是通过指定end参数为空字符串，使得它们不会换行，而是连成一行输出。
然后，我们使用print函数输出三个文本片段，并通过指定sep参数为", "，使得它们以逗号分隔输出。

通过这些例子，我们可以看到，通过指定end和sep参数，可以灵活地控制print函数的输出格式。这在处理文本文件、生成报告等任务中非常有用。
'''
'''
在Python中，print函数的结束符可以通过指定end参数来修改，默认为换行符"\n"。
以下是一些常见的结束符及其用法：
'''
# 1.换行符："\n"是print函数默认的结束符，用于在输出文本后换行。
print("Hello, world!")
print("Welcome to Python!")
# 输出：
# Hello, world!
# Welcome to Python!

# 2.空格符："\s"可以用于在输出文本之间添加空格。
print("Hello,", "world!")
# 输出：Hello, world!

# 3.制表符："\t"可以用于在输出文本之间添加制表符。
print("Name", "\t", "Age")
print("John", "\t", "30")
# 输出：
# Name    Age
# John    30

# 4.分号：";"可以用于在一行中输出多个语句。
print("Hello,"); print("world!")
# 输出：
# Hello,
# world!


