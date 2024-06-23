"""
    @project: stuPython
    @Author：Murk
    @file： 任务二.py
    @date：2024/5/22 20:33
    @Desc: 为手机充值
"""
print('用户手机账户原有话费金额为：\033[0;35m8元\033[m')
money = int(input('请输入用户充值金额：'))
money += 8
print(f'当前的余额为：\033[0;35m {money}元\033[m')
print(f'当前的余额为：\033[0;33m', money, '元\033[m')
