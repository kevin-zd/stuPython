"""
    @project: stuPython
    @Author：Murk
    @file： 任务三.py
    @date：2024/5/22 20:40
    @Desc: 计算能量的消耗
"""
num = int(input('请输入你当天行走的步数：'))
calorie = num * 28
print(f'今天共消耗了卡路里{calorie}, 即{calorie/1000}千卡')
