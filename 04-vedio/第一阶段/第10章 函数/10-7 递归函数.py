"""
    @project: stuPython
    @Author：Murk
    @file： 10-7 递归函数.py
    @date：2024/4/7 21:28
    @Desc: 
"""
'''使用递归来计算阶乘'''
def fac(n):
    if n == 1:
        return 1
    else:
        res = n * fac(n-1)
        return res
        # return n * fac(n-1)

print(fac(6))
