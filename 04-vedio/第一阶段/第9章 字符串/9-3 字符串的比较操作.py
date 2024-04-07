"""
    @project: stuPython
    @Author：Murk
    @file： 9-3 字符串的比较操作.py
    @date：2024/4/6 13:46
    @Desc: 
"""
print('apple' > 'app')     # True
print('apple' > 'banana')  # False
print(ord('a'), ord('b'))

print(chr(97), chr(98))
print(chr(26472))

'''== 与 is的区别
    == 比较的是value
    is 比较的是id是否相等'''
a = b = 'Python'
c = 'Python'
print(a == b)  # True
print(b == c)  # True

print(a is b)  # True
print(a is c)  # True
print(id(a))
print(id(b))
print(id(c))
