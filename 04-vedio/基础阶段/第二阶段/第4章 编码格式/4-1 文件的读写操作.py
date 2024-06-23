"""
    @project: stuPython
    @Author：Murk
    @file： 4-1 文件的读写操作.py
    @date：2024/5/4 11:20
    @Desc: 
"""
file = open('编码格式知识点.md', 'r')
print(file.readline())
file.close()
