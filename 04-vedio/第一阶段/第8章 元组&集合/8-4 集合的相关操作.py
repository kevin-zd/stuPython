"""
    @project: stuPython
    @Author：Murk
    @file： 8-4 集合的相关操作.py
    @date：2024/4/5 18:23
    @Desc: 
"""
print('-'*8+'集合元素的判断操作'+'-'*8)
s = {10, 20, 30, 40, 50}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

print('-'*8+'集合元素的新增操作'+'-'*8)
s.add(100)     # add一次添加一个元素
print(s)

s.update({300, 200})    # 一次至少添加一个元素
print(s)
s.update([11, 22, 33])
s.update((111, 222, 333))
print(s)

print('-'*8+'集合元素的删除操作'+'-'*8)
s.remove(100)
print(s)
# s.remove(500)    # KeyError: 500
s.discard(500)
print(s)
s.pop()
# s.pop(800)     # 不能添加参数，只能无参 TypeError: set.pop() takes no arguments (1 given)
print(s)
s.clear()
print(s)