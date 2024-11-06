# 参考网站：https://docs.python.org/zh-cn/3/tutorial/introduction.html
# 3.python用作计算器
a = 17 / 3  # 经典除法运算返回一个浮点数
print(a)
#5.666666666666667

b = 17 // 3  # 向下取整除法运算会丢弃小数部分
print(b)
#5
c = 17 % 3  # % 运算返回相除的余数
print(c)
#2
d = 5 * 3 + 2  # 向下取整的商 * 除数 + 余数
print(d)
#17

a1 = 5 ** 2   # 5的平方
print(a1)

width = 5
height = 7
print(width * height)

print(4 * 3.75 - 1)

# 交互模式 上次输出的表达式会赋给变量 _。把 Python 当作计算器时，用该变量实现下一步计算更简单
tax = 12.5 / 100
price = 100.50
x1 =price * tax
print('x1 =',x1)

# 要标示引号本身，我们需要对它进行“转义”，即在前面加一个 \。 或者，我们也可以使用不同类型的引号:
print('doesn\'t')  # 使用 \' 来转义单引号...
print("doesn't") # ...或者改用双引号
print('"Yes," they said.')
