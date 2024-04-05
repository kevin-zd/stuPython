"""
    @project: stuPython
    @Author：Murk
    @file： demoAdd.py
    @date：2024/4/5 07:40
    @Desc: 
"""

lst = [10, 20, 30]
print('添加元素之前：', lst, id(lst))
lst.append(40)
print('添加元素之后：', lst, id(lst))

lst2 = ['hello', 'world']
lst.append(lst2)    # 将lst2作为一个元素添加到列表的末尾
print('添加元素之后：', lst, id(lst))    # [10, 20, 30, 40, ['hello', 'world']]

# 向列表的末尾一次性添加多个元素
lst.extend(lst2)    # 将lst2作为一个元素添加到列表的末尾
print('添加元素之后：', lst, id(lst))    # [10, 20, 30, 40, 'hello', 'world']

# 在任意位置添加一个元素
lst.insert(1, 90)
print(lst)

lst3 = [True, False, 'animal', 'city']
lst[1:] = lst3
print(lst)