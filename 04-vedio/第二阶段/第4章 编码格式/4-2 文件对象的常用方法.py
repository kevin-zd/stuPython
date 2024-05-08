"""
    @project: stuPython
    @Author：Murk
    @file： 4-2 文件对象的常用方法.py
    @date：2024/5/4 12:15
    @Desc: 
"""
file = open('a.txt', 'r')
# file.write('hello')
# lst = ['java', 'python', 'go']
# file.writelines(lst)
# file.close()


file.seek(2)
print(file.read())
file.close()
