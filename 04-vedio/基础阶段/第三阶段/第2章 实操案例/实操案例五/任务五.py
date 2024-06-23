"""
    @project: stuPython
    @Author：Murk
    @file： 任务五.py
    @date：2024/5/26 16:09
    @Desc: 计算100-999之间的水仙花数
"""
import math
for i in  range(100, 1000):
    if math.pow((i % 10), 3) + math.pow((i // 10 % 10), 3) + math.pow(i // 100, 3) == i:
        print(i)
