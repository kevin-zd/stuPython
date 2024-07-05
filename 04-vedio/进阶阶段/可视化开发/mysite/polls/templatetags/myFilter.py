"""
    @project: stuPython
    @Author：Murk
    @file： myFilter.py
    @date：2024/6/28 19:26
    @Desc: 
"""
from django import template

register = template.Library()

@register.filter
def myFilterMGW(value, arg1):
    myStr1 = str(value)
    if myStr1.find("敏感词1") >= 0:
        return myStr1.replace("敏感词1", arg1)
    else:
        return value
