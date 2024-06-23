"""
    @project: stuPython
    @Author：Murk
    @file： 8-6 集合的数学操作.py
    @date：2024/4/5 18:51
    @Desc: 
"""
print('-'*8+'交集'+'-'*8)
s1 = {10, 20, 30, 40, 50}
s2 = {20, 30, 40, 90}
print(s1.intersection(s2))
print(s1 & s2)     # intersection()与& 等价，交集操作

print('-'*8+'并集'+'-'*8)
print(s1.union(s2))
print(s1 | s2)     # union()与| 等价，并集操作

print('-'*8+'差集'+'-'*8)
print(s1.difference(s2))
print(s1 - s2)     # difference()与- 等价，差集操作

print('-'*8+'对称差集'+'-'*8)
print(s1.symmetric_difference(s2))
print(s1 ^ s2)     # symmetric_difference()与^ 等价，差集操作





