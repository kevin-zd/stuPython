"""
    @project: stuPython
    @Author：Murk
    @file： 4-4 目录操作.py
    @date：2024/5/5 03:01
    @Desc: 
"""
import os
# os.system('Calculator.app')
# os.system('notepad.app')


import subprocess

# 打开计算器应用程序
# subprocess.call(['open', '-a', 'Calculator'])

print(os.getcwd())
lst = os.listdir('')
print(lst)

os.mkdir('newDir')
os.makedirs('A/B/C')
os.rmdir('newDIr')
os.removedirs('A/B/C')

print('-'*6+'os.path模块操作目录相关的函数'+'-'*6)
print(os.path.abspath('4-1 文件的读写操作.py'))
print(os.path.exists('4-1 文件的读写操作.py'), os.path.exists('4-2 文件对象的常用方法.py'))
print(os.path.join('E:\\python', 'demo3.py'))
