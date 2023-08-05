"""
运算符：了解Python中的算术运算符、比较运算符、逻辑运算符等。
"""

'''
在Python中，运算符是用于执行各种算术、逻辑和比较操作的符号。
以下是Python中常见的运算符：
'''

# 1.算术运算符：用于执行基本的算术操作，例如加、减、乘、除等。
a = 10
b = 3
print(a + b)  # 输出13
print(a - b)  # 输出7
print(a * b)  # 输出30
print(a / b)  # 输出3.3333333333333335
print(a % b)  # 输出1
print(a // b)  # 输出3
print(a ** b)  # 输出1000

# 2.比较运算符：用于比较两个值之间的关系，例如等于、不等于、大于、小于等。
a = 10
b = 3
print(a == b)  # 输出False
print(a != b)  # 输出True
print(a > b)  # 输出True
print(a < b)  # 输出False
print(a >= b)  # 输出True
print(a <= b)  # 输出False

# 3.逻辑运算符：用于执行逻辑运算，例如与、或、非等。
a = True
b = False
print(a and b)  # 输出False
print(a or b)  # 输出True
print(not a)  # 输出False

# 4.赋值运算符：用于将值赋给变量，例如等于、加等于、减等于等。
a = 10
b = 3
a += b  # 等价于a = a + b
print(a)  # 输出13

a -= b  # 等价于a = a - b
print(a)  # 输出10

a *= b  # 等价于a = a * b
print(a)  # 输出30

a /= b  # 等价于a = a / b
print(a)  # 输出10.0

a %= b  # 等价于a = a % b
print(a)  # 输出1.0

a //= b  # 等价于a = a // b
print(a)  # 输出3.0

a **= b  # 等价于a = a ** b
print(a)  # 输出27.0

# 5.位运算符：用于执行按位运算，例如按位与、按位或、按位取反等。
a = 0b1010  # 十进制数10的二进制表示方式为1010
b = 0b1100  # 十进制数12的二进制表示方式为1100

print(bin(a & b))  # 输出0b100，表示按位与的结果为100，即十进制数4的二进制表示方式为100。

print(bin(a | b))  # 输出0b1110，表示按位或的结果为1110，即十进制数14的二进制表示方式为1110。

print(bin(~a))  # 输出-0b1011，表示按位取反的结果为-1011，即十进制数-11的二进制表示方式为-1011。



