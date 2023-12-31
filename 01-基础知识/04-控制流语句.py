"""
在Python中，控制流语句是用于控制程序执行流程的语句。
以下是Python中常见的控制流语句：
"""
'''
1.if语句：用于执行条件判断，当条件成立时执行相应的代码块。
'''
a = 10
if a > 0:
    print("a是正数")
else:
    print("a是负数")

'''
2.for循环：用于遍历一个序列（例如列表、元组、字符串等），并执行相应的代码块。
'''
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

'''
3.while循环：用于重复执行一段代码，直到条件不成立为止。
'''
a = 0
while a < 5:
    print(a)
    a += 1

'''
4.break语句：用于跳出循环，停止执行循环内剩余的代码。
'''
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)

'''
5.continue语句：用于跳过当前循环中的某些代码，继续执行下一次循环。
'''
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        continue
    print(i)

'''
6.pass语句：用于占位，表示不执行任何操作。通常用于占据一个代码块的位置，以后再填充具体的代码。
'''
a = 10
if a > 0:
    pass
else:
    print("a是负数或0")

""" ------------    控制流语句嵌套      ---------- """
"""
在Python中，控制流语句可以互相嵌套，以实现更加复杂的逻辑。
以下是一些常见的控制流语句嵌套示例：
"""
'''
1.if语句嵌套：可以在if语句中嵌套另一个if语句，以实现更加复杂的条件判断。
'''
a = 10
if a > 0:
    if a < 5:
        print("a是小于5的正数")
    else:
        print("a是大于等于5的正数")
else:
    print("a是负数或0")

'''
2.for循环嵌套：可以在for循环中嵌套另一个for循环，以实现对多维数组的遍历。
'''
a = [[1, 2], [3, 4], [5, 6]]
for i in a:
    for j in i:
        print(j)

'''
3.while循环嵌套：可以在while循环中嵌套另一个while循环，以实现更加复杂的条件判断和循环控制。
'''
a = 0
while a < 5:
    b = 0
    while b < a:
        print("*", end="")
        b += 1
    print("")
    a += 1

'''
4.控制流语句嵌套：可以在一个控制流语句中嵌套另一个控制流语句，以实现更加复杂的逻辑控制。
'''
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        continue
    elif i == 4:
        break
    else:
        print(i)
