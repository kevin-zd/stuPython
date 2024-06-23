"""
能够使用while循环，完成猜数字案例
需求：设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数

import random
num = random.randint(1,100)
"""

# 获取范围在1-100的随机数字
import random
num = random.randint(1, 100)

# 定义一个变量，记录总共猜测了多少次
count = 0

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 设置false就是终止循环的条件
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜小了")

print(f"你总共猜了{count}次")