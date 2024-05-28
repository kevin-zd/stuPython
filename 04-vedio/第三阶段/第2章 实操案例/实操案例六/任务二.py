"""
    @project: stuPython
    @Author：Murk
    @file： 任务二.py
    @date：2024/5/28 20:58
    @Desc: 京东购物流程
"""
lst = []
for i in range(0, 5):
    goods = input('请输入商品编号和商品名称进入商品的入库，每次只能输入一件商品：\n')
    lst.append(goods)
for item in lst:
    print(item)


cart = []
while True:
    num = input('请输入要购买的商品编码：')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break   # 退出for
    if num == 'q':
        break   # 退出while循环
print('你购物车里已经选好的商品为：')
for m in cart:
    print(m)

for i in range(len(cart)-1, -1):
    print(cart[i])