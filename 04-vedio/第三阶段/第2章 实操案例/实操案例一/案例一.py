"""
    @project: stuPython
    @Author：Murk
    @file： 案例一.py
    @date：2024/5/12 16:51
    @Desc: 任务1：向文件输出 内容
"""
'''一、使用print方式进行输出（输出的目的地是文件）'''
fp = open('h:/text.txt', 'w')
print('奋斗成就更好的字节', file = fp)
fp.close()

'''二、使用文件读写操作'''
with open('h:/test.txt', 'w') as file:
    file.write('奋斗成绩更好的字节')