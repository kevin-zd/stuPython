

import re

while True:
    password = input("请输入密码：")
    if len(password) < 8:
        print("密码长度不能少于8位！")
    elif not re.search(r'[a-z]', password):
        print("密码必须包含小写字母！")
    elif not re.search(r'[A-Z]', password):
        print("密码必须包含大写字母！")
    elif not re.search(r'\d', password):
        print("密码必须包含数字！")
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("密码必须包含特殊字符！")
    else:
        print("密码设置成功！")
        break
