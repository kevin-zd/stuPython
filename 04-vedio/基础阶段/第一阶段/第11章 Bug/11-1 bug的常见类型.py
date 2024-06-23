"""
    @project: stuPython
    @Author：Murk
    @file： 11-1 bug的常见类型.py
    @date：2024/4/7 21:46
    @Desc: 
"""
print('-'*6+' 粗心导致的语法错误 SyntaxError '+'-'*8)
age = input('请输入你的年龄：')
print(type(age))
if int(age) >= 18:
    print('成年人....')

print()
i = 0
while i < 20:
    print(i)

print('-'*6+' 索引越界问题 IndexError '+'-'*8)
lst = [11, 22, 33, 44]
print(lst[4])

print('-'*6+' append()方法的使用掌握不熟练 '+'-'*8)
lst = []
lst = lst.append('A', 'B' 'C')
print(lst)
