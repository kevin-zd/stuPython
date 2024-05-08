"""
    @project: stuPython
    @Author：Murk
    @file： 4-3 with语句的使用.py
    @date：2024/5/5 02:47
    @Desc: 
"""
with open('4-3 with语句的使用.py', 'r') as file:
    print(file.read())

print('-'+'案例二'+'-'*6)
with open('4-1 文件的读写操作.py', 'r') as src_file:
    with open('4-1 文件的读写操作.bak.py', 'w') as target_file:
        target_file.write(src_file.read())