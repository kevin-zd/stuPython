"""
    @project: stuPython
    @Author：Murk
    @file： 案例八.py
    @date：2024/5/22 20:11
    @Desc: 输出身高指标
"""
height = 170
weight = 50.5
bmi = weight/(height+weight)
print('你的身高是：'+str(height))
print('你的体重是：'+str(weight))
print('你的BMI指数是：{:0.2f}'.format(bmi))
