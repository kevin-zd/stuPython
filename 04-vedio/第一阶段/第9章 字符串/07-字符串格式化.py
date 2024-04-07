# 通过占位的形式，完成拼接
name = "莫克科技"
message = "未来创业公司的名称是：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据分析，上海第%s期，毕业平均工资是：%s" %(class_num, avg_salary)
print(message)

name = "上海莫克"
setup_year = 2023
stock_price = 19.99
message = "%s，成立于：%d，今天的股价是：%f " %(name, setup_year, stock_price)
print(message)