"""
    @project: stuPython
    @Author：Murk
    @file： 案例六.py
    @date：2024/5/22 19:46
    @Desc: 输出《红楼梦》中金陵十二拆前五位
"""
# 变量赋值
'''方式一'''
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'
print('➊\t'+name1)
print('➋\t'+name2)
print('➌\t'+name3)
print('➍\t'+name4)
print('➎\t'+name5)
print('--------------------')

'''方式二：列表'''
lst_name = ['妙玉', '贾迎春', '贾惜春', '王熙凤', '巧姐']
lst_sig = ['❶', '❷', '❸', '❹', '❺']
for i in range(5):
    print(lst_sig[i], lst_name[i])
print('--------------------')

'''方式三：字典'''
d = {'➀': '巧姐', '➁': '李纨', '➂': '秦可卿'}
for key in d:
    print(key, d[key])
print('--------------------')

'''方式四：zip'''
for s, name in zip(lst_sig, lst_name):
    print(s, name)
