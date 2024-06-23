"""
    @project: stuPython
    @Author：Murk
    @file： 10-6 变量的作用域.py
    @date：2024/4/7 21:17
    @Desc: 
"""
def fun(a, b):
    c = a + b       # c,就称为局部变量，因为c是在函数体内进行定义的变量，a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

# print(c)   # 因为a,c超出了起作用的范围（超出了作用域）
# print(a)


name = '上海'    # name的作用范围为函数内部和外部都可以使用 --> 称为全局变量
print(name)
def fun():
    print(name)
# 调用函数
fun()

def fun():
    global age  # 函数内部定义的变量，局部变量。局部变量使用global声明，这个变量实际上就变成了全局变量
    age = 20
    print(age)
fun()
print(age)