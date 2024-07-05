"""
    @project: stuPython
    @Author：Murk
    @file： 去重.py
    @date：2024/7/5 17:46
    @Desc: 
"""
from collections import OrderedDict

data = [61,62,63,64,61,62,63,64,61,62,63,64,61,62,63,64,61,62,63,61,62,63,64]
unique_data = list(OrderedDict.fromkeys(data))
print(unique_data)  # 输出: [61, 62, 63]