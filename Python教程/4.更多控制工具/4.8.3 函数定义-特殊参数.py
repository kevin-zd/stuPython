"""
    @project: stuPython
    @Author：Murk
    @file： 4.8.3 函数定义-特殊参数.py
    @date：2024/2/21 17:35
    @Desc: 
"""
"""
函数定义如下：

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
/ 和 * 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。关键字形参也叫作命名形参。
"""
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

print("-----第一个函数定义 standard_arg 是最常见的形式，对调用方式没有任何限制，可以按位置也可以按关键字传递参数：-----")
standard_arg(2)
standard_arg(arg=2)

print('---第二个函数 pos_only_arg 的函数定义中有 /，仅限使用位置形参：-----')
pos_only_arg(1)
# pos_only_arg(arg=1)

print("-----第三个函数 kwd_only_args 的函数定义通过 * 表明仅限关键字参数：-------")
# kwd_only_arg(3)
kwd_only_arg(arg=3)

print("----最后一个函数在同一个函数定义中，使用了全部三种调用惯例：-------")
# combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


print("========= 小结 =========")
"""
以下用例决定哪些形参可以用于函数定义：
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
说明：
    使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
    当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。
    对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。
"""
