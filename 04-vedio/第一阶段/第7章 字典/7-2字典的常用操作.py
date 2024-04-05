"""
    @project: stuPython
    @Author：Murk
    @file： 7-2字典的常用操作.py
    @date：2024/4/5 14:13
    @Desc: 
"""
print('-'*8+'获取字典的元素'+'-'*8)
scores = {'张三': 100, '李四': 98, '王五': 21}

''' 第一种方式，使用[] '''
print(scores['张三'])
# print(scores['张三三']        # KeyError: '张三三'

''' 第二种方式，使用get()方法 '''
print(scores.get('张三'))
print(scores.get('张三三'))     # None

''' key的判断'''
print('张三' in scores)
print('张三' not in scores)

print(scores)

''' del 删除指定元素'''
del scores['张三']
print(scores)

''' clear() 清空元素'''
# scores.clear()
print(scores)

''' 新增元素'''
scores['赵六'] = 88
print(scores)

''' 修改元素'''
scores['赵六'] = 888
print(scores)

''' 获取所有的key'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))   # 将所有的key组成的视图转成列表

''' 获取所有的value '''
values = scores.values()
print(values)
print(type(values))
print(list(values))

''' 获取所有的key-value键值对 '''
items = scores.items()
print(items)
print(type(items))
print(list(items))  # 转换之后的列表元素是由元组组成

''' 字典元素的遍历'''
print('-'*8+'字典元素的遍历'+'-'*8)
scores = {'张三': 100, '李四': 98, '王五': 21}
for item in scores:
    print(item, scores[item], scores.get(item))
