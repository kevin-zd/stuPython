"""
    @project: stuPython
    @Author：Murk
    @file： 11-2 bug的解决方案.py
    @date：2024/4/9 19:30
    @Desc: 
"""
lst = [
        {'rating': [9, 7, 50], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '霸王别姬', 'actors': ['张国荣', '张丰毅', '公历']},
        {'rating': [9, 7, 50], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '霸王别姬', 'actors': ['张违反', '张丰毅', '公历']},
        {'rating': [9, 7, 50], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '霸王别姬', 'actors': ['张是否', '张丰毅', '公历']}
       ]

name = input('请输入你要查询的演员：')
for item in lst:    # 遍历列表   => {}     item是一个有一个字典
    act_lst = item['actors']
    print(act_lst)
    for actor in act_lst:
        if name in actor:
            print(name+'出演了'+item['title'])
    # for movie in item:
    #     print(movie)
    # print('--------')
        # actors = movie['actors']
        # print(actors)
        # if name in actors:
        #     print(name + '出演了'+movie)