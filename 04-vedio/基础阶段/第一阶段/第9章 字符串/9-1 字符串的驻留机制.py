"""
    @project: stuPython
    @Author：Murk
    @file： 9-1 字符串的驻留机制.py
    @date：2024/4/6 09:24
    @Desc: 
"""
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))