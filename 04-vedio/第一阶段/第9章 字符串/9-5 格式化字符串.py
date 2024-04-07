"""
    @project: stuPython
    @Author：Murk
    @file： 9-5 格式化字符串.py
    @date：2024/4/6 14:18
    @Desc: 
"""
print('-'*8+' % 占位符 '+'-'*8)
name = '张三'
age = 20
print('我叫%s, 今年%d岁了' % (name, age))

print('-'*8+' {} 占位符 '+'-'*8)
print('我叫{0}, 今年{1}岁了'.format(name, age))

print('-'*8+' f-string 占位符 '+'-'*8)
print(f'我叫{name}，今年{age}岁了')

print('-'*8+' 精度和宽度 占位符 '+'-'*8)
print('%10d' % 99)   # 10表示的是宽度
print('%.3f' % 3.1415912)   # .3表示的是小数点后三位
# 同时表示宽度和精度
print('%10.3f' % 3.1415926)   # 一共总宽度为10，小数点后3位

print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))    # .3表示的是一共是3位数
print('{:.3f}'.format(3.1415926))    # .3f表示的是3位小数
print('{:10.3f}'.format(3.1415926))   # 同时设置宽度和精度，一共是10位，3位是小数

