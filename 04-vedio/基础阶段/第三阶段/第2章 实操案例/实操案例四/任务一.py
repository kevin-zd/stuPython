"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/5/22 20:46
    @Desc: 支付密码的验证
"""
pwd = input('支付宝支付密码：')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能是数字')

'''方式二：'''
print('支付数据合法' if pwd.isdigit() else '支付数据不合法，支付密码必须是数字')