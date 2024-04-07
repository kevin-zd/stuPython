"""
    @project: stuPython
    @Author：Murk
    @file： 9-6 字符串的编码转换.py
    @date：2024/4/6 14:39
    @Desc: 
"""
s = '天涯共此时'

# 编码
print(s.encode(encoding='GBK'))    # 在GBK这种编码中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))   # 在UTF-8这种编码格式中，一个中文占三个字节

# 解码
# byte代表就是一个二进制数据（字节类型的数据）
byte = s.encode(encoding='GBK')    # 编码
print(byte.decode(encoding='GBK')) # 解码
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))