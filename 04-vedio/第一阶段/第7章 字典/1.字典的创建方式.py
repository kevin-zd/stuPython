"""
    @project: stuPython
    @Author：Murk
    @file： 1.字典的创建方式.py
    @date：2024/4/5 14:02
    @Desc: 
"""
''' 使用{}创建字典 '''
scores = {'张三': 20, '李四': 98, '王五': 100}
print(scores)
print(type(scores))

''' 第二种 创建dict()'''
student = dict(name='jack', age=20)
print(student)
print(type(student))
print(student.get('name'))

''' 空字典'''
d = {}
print(d)
