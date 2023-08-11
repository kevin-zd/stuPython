"""
以下是Python中常见的数据类型转换函数：
"""
# 1.int()：用于将一个字符串或浮点数转换为整数。
num1 = int("123")
num2 = int(3.14)
print(num1, num2)  # 输出123 3
print(type(num1), type(num2))

# 2.float()：用于将一个字符串或整数转换为浮点数。
num1 = float("3.14")
num2 = float(123)
print(num1, num2)  # 输出3.14 123.0
print(type(num1), type(num2))

# 3.str()：用于将一个整数、浮点数或其他数据类型转换为字符串。
str1 = str(123)
str2 = str(3.14)
print(str1, str2)  # 输出'123' '3.14'
print(type(str1), type(str2))

# 4.bool()：用于将一个数据类型转换为布尔值。
bool1 = bool(0)
bool2 = bool("")
bool3 = bool(None)
bool4 = bool(123)
print(bool1, bool2, bool3, bool4)  # 输出False False False True
print(type(bool1), type(bool2), type(bool3), type(bool4))

# 5.tuple()：用于将一个列表或其他可迭代对象转换为元组。
list1 = [1, 2, 3]
tuple1 = tuple(list1)
print(tuple1)  # 输出(1, 2, 3)
print(type(tuple1))

# 6.list()：用于将一个元组或其他可迭代对象转换为列表。
tuple1 = (1, 2, 3)
list1 = list(tuple1)
print(list1)  # 输出[1, 2, 3]
print(type(list1))

# 7.set()：用于将一个列表、元组或其他可迭代对象转换为集合。
list1 = [1, 2, 3]
set1 = set(list1)
print(set1)  # 输出{1, 2, 3}
print(type(set1))

# 8.eval()：用于将一个字符串作为Python表达式执行，并返回表达式的结果。
x = 10
y = 20
result = eval("x + y")
print(result)  # 输出30
print(type(result))

list_str = "[1, 2, 3]"
list_result = eval(list_str)
print(list_result)  # 输出[1, 2, 3]
print(type(list_result))






