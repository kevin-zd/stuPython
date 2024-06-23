"""
    @project: stuPython
    @Author：Murk
    @file： 8-5 集合间的关系.py
    @date：2024/4/5 18:40
    @Desc: 
"""
print('-'*8+'两个集合是否相等（元素相同，就相等）'+'-'*8)
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)
print(s1 != s2)

print('-'*8+'一个集合是否是另一个集合的子集'+'-'*8)
s1 = {10, 20, 30, 40, 50}
s2 = {20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))

print('-'*8+'一个集合是否是另一个集合的超集'+'-'*8)
print(s1.issuperset(s2))
print(s1.issuperset(s3))

print('-'*8+'两个集合是否含有交集'+'-'*8)
print(s2.isdisjoint(s3))    # False 有交集为False，无交集为True
print(s2.isdisjoint(s1))
s4 = {11, 22, 33}
print(s2.isdisjoint(s4))
