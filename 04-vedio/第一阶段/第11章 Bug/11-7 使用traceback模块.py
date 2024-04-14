"""
    @project: stuPython
    @Author：Murk
    @file： 11-7 使用traceback模块.py
    @date：2024/4/13 15:37
    @Desc: 
"""
import traceback

try:
    print('----------------')
    print(1 / 0)
except:
    traceback.print_exc()
