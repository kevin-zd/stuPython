"""
    @project: stuPython
    @Author：Murk
    @file： 2-9 类的赋值与浅拷贝.py
    @date：2024/4/20 11:10
    @Desc: 
"""
class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

# 1、变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)
