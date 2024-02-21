"""
    @project: stuPython
    @Author：Murk
    @file： 4.4 循环中的 break、continue 语句及 else 子句.py
    @date：2024/2/21 16:52
    @Desc: 
"""
"""
break 语句将跳出最近的一层 for 或 while 循环。
for 或 while 循环可以包括 else 子句。
在 for 循环中，else 子句会在循环成功结束最后一次迭代之后执行。
在 while 循环中，它会在循环条件变为假值后执行。
无论哪种循环，如果因为 break 而结束，那么 else 子句就 不会 执行
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print(' -------- continue 语句，同样借鉴自 C 语言，以执行循环的下一次迭代来继续：-------')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)