"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/6/2 10:46
    @Desc: 编写程序输入学员成绩
"""
try:
    score = int(input('请输入你的分数：'))
    if 0 <= score <= 100:
        print(f'你的分数为：{score}')
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
