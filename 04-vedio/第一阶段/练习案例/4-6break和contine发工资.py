"""
    @project: stuPython
    @Author：Murk
    @file： 4-6break和contine发工资.py
    @date：2023/9/7 19:15
    @Desc: 练习案例：发工资
"""
'''
某公司，账户余额有1w元，给20名员工发工作
1、员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
2、领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
3、如果工资发完了，结束发工资
'''

# 定义账户余额变量
money = 10000
# for循环对员工发放工资
for i in range(1, 21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分{score}，不满足，不发工资，下一位")
        # continue跳过发放
        continue

    # 判断余额不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，满足条件发放工资1000，公司账户余额：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再发")
        # break结束发放
        break