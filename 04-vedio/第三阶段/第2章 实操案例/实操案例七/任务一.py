"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/5/28 21:27
    @Desc: 根据星座测试性格特点
"""
# 创建星座的列表
constellation = ['金牛宮', '雙子宮', '巨蟹宮', '獅子宮', '室女宮', '天秤宮', '天蠍宮', '人馬宮', '摩羯宮', '寶瓶宮', '雙魚宮']

# 创建性格列表
nature = ['和蔼可亲', '助人为乐', '活泼开朗', '口是心非', '冰雪聪明', '心直口快', '专心致志', '与人为善', '自高自大', '表里如一', '忠心耿耿', '人中之龙']

# 将两个列表转成集合
d = dict(zip(constellation, nature))
''' for item in a:
        print(item) '''
print(d)
key = input('请输入你的星座名称：')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key, '的性格特点是：', d.get(key))
        break
    else:
        # print('对不起，你输入的星座有误。')
        flag = False
if not flag:
    print('对不起，你输入的星座有误。')
