"""
    @project: stuPython
    @Author：Murk
    @file： 4-7break和continue中断控制.py
    @date：2023/9/4 21:10
    @Desc: 循环语句中的中断控制：break和continue
"""

# 循环中断语句：continue
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")

# continue的嵌套循环
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")


# 循环中断语句：break
for i in range(1, 101):
    print("语句1")
    break
    print("语句2")

print("语句3")

# break的嵌套循环
for i in range(1, 100):
    print("语句1")
    for j in range(1, 100):
        print("语句2")
        break
        print("语句3")

    print("语句4")
