"""
    @project: stuPython
    @Author：Murk
    @file： listSort.py
    @date：2024/4/5 08:35
    @Desc: 
"""
lst = [10, 20, 33, 4, 12]
print('排序前的列表：', lst)
lst.sort()
print('排序后的列表：', lst)
lst.sort(reverse=True)
print('降序后的列表：', lst)

print('-'*8+'使用内置函数sorted()对列表进行排序，将产生一个新的列表对象'+'-'*8)
lst = [10, 20, 33, 4, 12]
print('排序前的列表：', lst, id(lst))
new_lst = sorted(lst)
print('内置函数排序：', new_lst, id(new_lst))
# 指定关键字参数，实现列表元素的降序排序
desc_list = sorted(lst, reverse=True)
print('降序后的列表：', desc_list)
