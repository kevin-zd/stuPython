"""
    @project: stuPython
    @Author：Murk
    @file： 4.3 range()函数.py
    @date：2024/2/21 16:39
    @Desc: 
"""
for i in range(5):
    print(i)

print(list(range(5, 10)))

print(list(range(0, 10, 3)))

print(list(range(-10, -100, -30)))

print(' --------要按索引迭代序列，可以组合使用 range() 和 len()：------')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i], len(a[i]))