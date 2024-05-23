"""
    @project: stuPython
    @Author：Murk
    @file： 任务三.py
    @date：2024/5/22 20:54
    @Desc: 商品价格大竞猜
"""
import random
price = random.randint(1000, 1500)
print('今日竞猜的商品为小米扫地机器人：价格在[1000-1500]之间：')
guess = int(input())
if guess > price:
    print('大了')
elif guess < price:
    print('小了')
else:
    print('恭喜你，猜对了')
print('真实价格为：', price)
