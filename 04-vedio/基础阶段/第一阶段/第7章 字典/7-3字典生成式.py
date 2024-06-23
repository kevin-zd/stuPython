"""
    @project: stuPython
    @Author：Murk
    @file： 7-3字典生成式.py
    @date：2024/4/5 15:58
    @Desc: 
"""
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 33]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
