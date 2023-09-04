"""
    @project: stuPython
    @Author：Murk
    @file： 4-4for循环统计字母a个数.py
    @date：2023/9/4 20:14
    @Desc: for循环案例
"""

name = "bytedance is a brand of bytedance"

# 定义一个变量，用来统计有多少个a
count = 0

# for 循环统计
# for 临时变量 in 被统计的数据:
for x in name:
    if x == "a":
        count += 1

print(f"被统计的字符串有{count}个a")