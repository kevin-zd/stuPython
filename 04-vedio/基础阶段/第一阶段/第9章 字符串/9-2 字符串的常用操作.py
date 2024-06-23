"""
    @project: stuPython
    @Author：Murk
    @file： 9-2 字符串的常用操作.py
    @date：2024/4/6 11:49
    @Desc: 
"""
print('-' * 8 + '字符串的查询操作' + '-' * 8)
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# print(s.index('k'))      # ValueError: substring not found
print(s.find('k'))  # -1
# print(s.rindex('k'))       # ValueError: substring not found
print(s.rfind('k'))  # -1

print('-' * 8 + '字符串的大小写转换操作' + '-' * 8)
s = 'hello,python'
a = s.upper()  # 转成大写之后，会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
b = s.lower()  # 转成之后，会产生一个新的字符串对象
print(b, id(b))
print(s, id(s))
print(b == s)  # True
print(b is s)  # False

s2 = 'hello,Python'
print(s2.swapcase())

print(s2.title())

print('-' * 8 + '字符串内容对齐操作的方法' + '-' * 8)
s = 'hello,Python'
''' 居中对齐'''
c = s.center(20, '*')
print(c)
'''左对齐'''
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20))

'''右对齐'''
print(s.rjust(20, '*'))
print(s.rjust(10))
print(s.rjust(20))

'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(9))

print('-' * 8 + '字符串劈分操作的方法' + '-' * 8)
s = 'hello world python'
lst = s.split()
print(lst)
s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

'''rsplit()从右侧开始劈分'''
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))

print('-' * 8 + '判断字符串操作的方法' + '-' * 8)
s = 'hello,python'
print('1、', s.isidentifier())
print('2、', 'hello'.isidentifier())
print('3、', '张三'.isidentifier())
print('4、', '张三_123'.isidentifier())

print('5、', '\t'.isspace())   # True
print('6、', 'abc'.isalpha())   # True
print('7、', '张三'.isalpha())   # True
print('8、', '张三1'.isalpha())   # False

print('9、', '123'.isdecimal())   # True
print('10、', '123四'.isdecimal())   # False
print('11、', '|||'.isdecimal())   # False

print('12、', '123'.isnumeric())   # True
print('13、', '123四'.isnumeric())   # True
print('14、', '| || |||'.isdecimal())   # True


print('15、', 'abc1'.isalnum())   # True
print('16、', '张三123'.isalnum())   # True
print('17、', 'abc!'.isalnum())   # False

print('-' * 8 + '字符串操作的其他方法' + '-' * 8)
s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello, Python, Python, Python'
print(s1.replace('Python', 'Java', 2))

lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'java', 'Python')
print(''.join(t))

print('*'.join('Python'))






