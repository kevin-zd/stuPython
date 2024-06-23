"""
    @project: stuPython
    @Author：Murk
    @file： 任务二.py
    @date：2024/6/2 09:06
    @Desc: 猜数游戏
"""
import random
def guess(num, guess_num):
    if num == guess_num:
        return 0
    elif guess_num > num:
        return 1
    else:
        return -1

num = random.randint(1, 100)
for i in range(10):
    guess_num = int(input('我心中想的数字有【1-100】的整数，猜一猜：'))
    result = guess(num, guess_num)
    if result == 0:
        print('猜对了')
        break
    elif result > 0:
        print('猜大了')
    elif result < 0:
        print('猜小了')
else:
    print('十次都没猜对')

