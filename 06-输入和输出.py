"""
Python中进行标准输入和输出，以及如何读写文件
"""
'''
在Python中，标准输入和输出可以通过input()和print()函数实现，文件的读写可以通过open()函数和相关的文件对象方法实现。
以下是Python中标准输入和输出、文件读写的基本用法：
'''
# 1.标准输入和输出：可以使用input()函数读取用户输入的内容，使用print()函数输出内容到控制台。
name = input("请输入你的名字：")
print("你好，" + name + "！")

# 2.文件读写：可以使用open()函数打开一个文件，并使用相关的文件对象方法读写文件内容。
# 打开一个文件并写入内容
file = open("test.txt", "w")
file.write("Hello, world!\n")
file.write("This is a test file.\n")
file.close()

# 打开一个文件并读取内容
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()


'''
在上面的示例中，我们首先使用open()函数打开一个名为test.txt的文件，并指定打开模式为"w"，表示写入模式。
然后，我们使用文件对象的write()方法向文件中写入两行文本内容，并使用close()方法关闭文件。

接着，我们再次打开同一个文件，但是这次指定打开模式为"r"，表示读取模式。
然后，我们使用文件对象的read()方法读取整个文件的内容，并使用print()函数输出到控制台。最后，我们使用close()方法关闭文件。
'''

