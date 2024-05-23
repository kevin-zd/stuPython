"""
    @project: stuPython
    @Author：Murk
    @file： 任务三.py
    @date：2024/5/22 21:18
    @Desc: 猜数游戏
"""
import random
rand = random.randint(1, 100)
for i in range(1, 11):
    num = int(input('在我心中有个数1-100，请你猜一猜：'))
    if num < rand:
        print('小了')
    elif num > rand:
        print('大了')
    else:
        print('恭喜你，猜对了')
        break
print(f'你一共猜了{i}次')
if i < 3:
    print('棒棒哒')
elif i <= 7:
    print('还凑合')
else:
    print('太笨拉～')