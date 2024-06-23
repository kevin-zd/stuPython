"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/5/26 16:15
    @Desc: 千年虫
"""
year = [82, 89, 90, 75, 88, 00]
print('原列表：', year)
for index, value in enumerate(year):
    # print(index, value)
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))

print('修改之后的列表：', year)
# 列表的排序
year.sort()
print('排序之后的列表为：', year)