"""
    @project: stuPython
    @Author：Murk
    @file： 4-6for循环嵌套应用.py
    @date：2023/9/4 20:49
    @Desc: for循环的嵌套
"""

i = 1
for i in range(1, 101):
    print(f"今天是搬砖的第{i}天，坚持，fighting")
    for j in range(1, 9):
        print(f"摸鱼工作的第{j}小时")
    print(f"生活不易，且行且珍惜,搬砖{i}天结束")

print(f"总共工作了{i}天")
