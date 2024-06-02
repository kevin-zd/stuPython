"""
    @project: stuPython
    @Author：Murk
    @file： 任务三.py
    @date：2024/6/2 08:08
    @Desc: 模拟手机通讯录
"""
phones = set()
for i in range(5):
    info = input(f'请输入第{i+1}个朋友的姓名和手机号：')
    phones.add(info)

for index, item in phones:
    print(item)