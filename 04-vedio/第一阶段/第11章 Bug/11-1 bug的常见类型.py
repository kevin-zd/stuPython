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