"""
    @project: stuPython
    @Author：Murk
    @file： demoRemove.py
    @date：2024/4/5 08:04
    @Desc: 
"""
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)     # 从列表中删除第一个元素，如果有重复元素只移除第一个元素
print(lst)

# lst.remove(100)   # ValueError: list.remove(x): x not in list
# pop()：根据索引移除元素
lst.pop(2)
print(lst)
# lst.pop(5)   # IndexError: pop index out of range 如果指定的索引不存在，将抛出异常
lst.pop()     # 如果不指定参（索引），将默认删除最后一个元素
print(lst)

print('-'*8+'切片：删除至少一个元素，将产生一个新的列表对象'+'-'*8)
new_lst = lst[1:3]
print('原列表：', lst)
print('切片后：', new_lst)

print('-'*8+'切片：不产生一个新的列表对象，而是删除原列表中的内容'+'-'*8)
lst[1:3] = []
print(lst)

print('-'*8+'清空列表中的元素'+'-'*8)
lst.clear()
print(lst)

print('-'*8+'del语句将列表对象'+'-'*8)
del lst
# print(lst)    # NameError: name 'lst' is not defined. Did you mean: 'list'?



