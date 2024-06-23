"""
    @project: stuPython
    @Author：Murk
    @file： 任务四.py
    @date：2024/5/22 20:42
    @Desc: 预测未来子女的身高
"""
father_height = float(input('请输入父亲的身高：'))
mother_height = float(input('请输入母亲的身高：'))
son_height = (father_height + mother_height)*0.54
print('预测子女的身高为：{}cm'.format(son_height))

