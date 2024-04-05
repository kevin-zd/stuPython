"""
    @project: stuPython
    @Author：Murk
    @file： demo4.py
    @date：2024/4/5 07:33
    @Desc: 
"""

print('p' in 'python')
print('k' in 'python')

lst = [10, 20, 'hello', 'python']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)