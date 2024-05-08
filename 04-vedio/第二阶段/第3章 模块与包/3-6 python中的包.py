"""
    @project: stuPython
    @Author：Murk
    @file： 3-6 python中的包.py
    @date：2024/5/4 07:43
    @Desc: 
"""
# 导入带有包的模块时注意事项
import package
import calc

# 使用import方式进行导入时，只能跟包名或模块名

from package import module_A
from package.module_B import b
# 使用from...import可以导入包、模块、函数、变量