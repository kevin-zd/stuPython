"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/5/22 21:10
    @Desc: 循环输出26个字母对应的ASCII码值
"""
x = 97   # 代表的是a的ascii值
for _ in range(1, 27):
    print(chr(x), '--->', x)
    x += 1

print('------------------')
x = 97
while x < 123:
    print(chr(x), '--->', x)
    x += 1