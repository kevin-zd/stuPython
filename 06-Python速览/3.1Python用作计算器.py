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
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

# 在 Python shell 中，字符串定义和输出字符串看起来可能不同。 print() 函数会略去标示用的引号，并打印经过转义的特殊字符，产生更为易读的输出:
s = 'First line.\nSecond line.'  # \n 表示换行符
print(s)  # 用 print()，特殊字符会被转写，因此 \n 将产生一个新行

# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可：
print('C:\some\name')  # 这里 \n 表示换行符！
print(r'C:\some\name')  # 请注意引号前的 r

# 字符串文字可以跨越多行。一种方法是使用三重引号："""...""" 或 '''...''' 。行尾会自动包含在字符串中，但可以通过在行尾添加 \ 来避免这种情况
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 字符串可以用 + 合并（粘到一起），也可以用 * 重复：
print(3 * 'un' + 'ium')

# 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并：
print('Py' 'thon')

# 拼接分隔开的长字符串时，这个功能特别实用：
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# 合并多个变量，或合并变量与字面值，要用 +：
prefix = 'Py'
print(prefix + 'thon')

# 字符串支持 索引 （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：
word = 'Python'
print(word[0])
print(word[5])

# 索引还支持负数，用负数索引时，从右边开始计数：
print(word[-1])
print(word[-2])
print(word[-6])
word[-2]

# 除了索引操作，还支持 切片。 索引用来获取单个字符，而 切片 允许你获取子字符串:
word[0:2]
word[2:5]

# 切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：
word[:2]
word[4:]
word[-2:]

# 注意，输出结果包含切片开始，但不包含切片结束。因此，s[:i] + s[i:] 总是等于 s：
word[:2] + word[2:]
word[:4] + word[4:]

# 索引越界会报错：但是，切片会自动处理越界索引：
# Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错：
word[0] = 'J'

# 要生成不同的字符串，应新建一个字符串：
'J' + word[1:]
word[:2] + 'py'

# 内置函数 len() 返回字符串的长度：
s = 'supercalifragilisticexpialidocious'
len(s)

## 3.1.3. 列表¶
# Python 支持多种 复合 数据类型，可将不同值组合在一起。最常用的 列表 ，是用方括号标注，逗号分隔的一组值。列表 可以包含不同类型的元素，但一般情况下，各个元素的类型相同
squares = [1, 4, 9, 16, 25]
squares

# 和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片：
squares[0]  # 索引操作将返回条目
squares[-1]
squares[-3:]  # 切片操作将返回一个新列表

# 列表还支持合并操作：
squares + [36, 49, 64, 81, 100]

# 与 immutable 字符串不同, 列表是 mutable 类型，其内容可以改变：
cubes = [1, 8, 27, 65, 125]  # 这里有点问题
4 ** 3  # 4 的立方是 64，不是 65！
cubes[3] = 64  # 替换错误的值
cubes

# 你也可以在通过使用 list.append() 方法，在列表末尾添加新条目（我们将在后面介绍更多相关的方法）:
cubes.append(216)  # 添加 6 的立方
cubes.append(7 ** 3)  # 和 7 的立方
cubes

# Python 中的简单赋值绝不会复制数据。 当你将一个列表赋值给一个变量时，该变量将引用 现有的列表。你通过一个变量对列表所做的任何更改都会被引用它的所有其他变量看到
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # 它们指向同一个对象
rgba.append("Alph")
rgb

# 切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 浅拷贝：
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba
rgba

# 为切片赋值可以改变列表大小，甚至清空整个列表：
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# 替换一些值
letters[2:5] = ['C', 'D', 'E']
letters
# 现在移除它们
letters[2:5] = []
letters
# 通过用一个空列表替代所有元素来清空列表
letters[:] = []
letters

# 内置函数 len() 也支持列表：
letters = ['a', 'b', 'c', 'd']
len(letters)

# 还可以嵌套列表（创建包含其他列表的列表），例如：
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

## 写出 斐波那契数列 初始部分的子序列:
# 斐波那契数列：
# 前两项之和即下一项的值
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

