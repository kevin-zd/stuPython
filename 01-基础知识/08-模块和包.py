"""
了解如何使用Python中的模块和包，以及如何导入和使用模块。
"""

'''
在Python中，模块和包是一种组织代码的方式，可以将代码分组、重用和管理。
以下是Python中使用模块和包的基本用法：
'''
# 1.导入模块：可以使用import语句导入一个模块，并使用其中的函数、变量等。
import math

result = math.sqrt(16)
print(result)  # 输出4.0

'''
在上面的示例中，我们使用import语句导入了Python标准库中的math模块，并使用其中的sqrt()函数计算16的平方根。
'''

# 2.导入模块中的部分内容：可以使用from-import语句导入一个模块中的部分内容，并直接使用它们。
from math import sqrt

result = sqrt(16)
print(result)  # 输出4.0

'''
在上面的示例中，我们使用from-import语句从math模块中导入了sqrt()函数，并直接使用它。
'''

# 3.导入自定义模块：可以创建自己的模块，并使用import语句导入它。
# 创建一个名为my_module.py的模块
# def greet(name):
#     print("Hello, " + name + "!")

# 在另一个脚本中导入my_module模块
import my_module

my_module.greet("John")  # 输出Hello, John!

'''
在上面的示例中，我们创建了一个名为my_module.py的模块，并在其中定义了一个greet()函数。
然后，我们在另一个脚本中使用import语句导入了my_module模块，并使用其中的greet()函数。
'''

# 4.导入包：可以将多个相关的模块组织在一个包中，并使用import语句导入整个包或其中的部分内容。
# 在一个名为mypackage的包中创建两个模块module1和module2
# mypackage/module1.py
# def greet(name):
#     print("Hello, " + name + "!")

# mypackage/module2.py
# def add(a, b):
#     return a + b

# 在另一个脚本中导入mypackage包和其中的module1模块
import mypackage.module1

mypackage.module1.greet("John")  # 输出Hello, John!

'''
在上面的示例中，我们在一个名为mypackage的包中创建了两个模块module1和module2。
然后，我们在另一个脚本中使用import语句导入了mypackage包和其中的module1模块，并使用其中的greet()函数。
'''



