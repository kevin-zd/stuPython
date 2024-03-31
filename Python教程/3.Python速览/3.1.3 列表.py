"""
    @project: stuPython
    @Author：Murk
    @file： 3.1.3 列表.py
    @date：2024/2/22 11:48
    @Desc: 
"""
"""
Python 支持多种 复合 数据类型，可将不同值组合在一起。最常用的 列表 ，是用方括号标注，逗号分隔的一组值。列表 可以包含不同类型的元素，但一般情况下，各个元素的类型相同：
"""
squares = [1, 4, 9, 16, 25]
print(squares)

print('和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片：')
print(squares[0])
print(squares[-1])
print(squares[-3:])