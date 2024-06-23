"""
    @project: stuPython
    @Author：Murk
    @file： demoList3.py
    @date：2024/3/31 17:12
    @Desc: 
"""
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[1:6:1])

print('原列表：', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))

# start=1, stop=6, step=1 (不懈默认为1)
print(lst[1:6])
# start=1, stop=6, step=1
print(lst[1:6:])
# start=1, stop=6, step=2
print(lst[1:6:2])
# stop=6, step=2, start采用默认
print(lst[:6:2])
# start=1, step=2, stop采用默认
print(lst[1::2])

print('-'*8+'step步长为负数的情况'+'-'*8)
print('原列表：', lst)
print(lst[::-1])
# start=7, stop省略, step=-1
print(lst[7::-1])
# start=6, stop=0, step=-2
print(lst[6:0:-2])


