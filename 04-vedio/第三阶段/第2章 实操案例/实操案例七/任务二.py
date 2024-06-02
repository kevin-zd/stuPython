"""
    @project: stuPython
    @Author：Murk
    @file： 任务二.py
    @date：2024/5/28 21:54
    @Desc: 模拟12306火车票订票下单
"""
dict_ticket = {
    'G1569': ['北京南 - 天津南', '18:05', '18:39', '00:34'],
    'G1567': ['北京南 - 天津南', '18:15', '18:49', '00:34'],
    'G8917': ['北京南 - 天津西', '18:25', '18:39', '00:59'],
    'G2034': ['北京南 - 天津南', '18:35', '19:39', '00:34']
}
print('车次\t\t 出发站 - 到达站\t\t 出发时间\t\t 到达时间\t\t 历时时长')
for item in dict_ticket:
    print(item, end=' \t ')
    for i in dict_ticket[item]:
        print(i, end=' \t \t  ')
    print()    # 换行
# 输入要购买的车次
train_no = input('请输入要购买的车次：')
persons = input('请输入乘车人，如果是多人请使用逗号分隔：')
s = f'你购买了{train_no}次列车'
s_info = dict_ticket[train_no]   # 获取车次详细信息
s += s_info[0] + '' + s_info[1] + ' 开'
print(f'{s}请{persons}尽快取走纸质车票。【铁路客服】')
