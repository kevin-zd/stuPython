"""
    @project: stuPython
    @Author：Murk
    @file： 3.1.2 文本.py
    @date：2024/2/21 18:00
    @Desc: 
"""
"""
除了数字 Python 还可以操作文本（由 str 类型表示，称为“字符串”）。 
这包括字符 "!", 单词 "rabbit", 名称 "Paris", 句子 "Got your back." 等等. "Yay! :)"。 
它们可以用成对的单引号 ('...') 或双引号 ("...") 来标示，结果完全相同
"""

print("'span eggs'")
print("Paris rabbit got your back :)! Yay!")

print("------ 要标示引号本身，我们需要对它进行“转义”，即在前面加一个 \。 或者，我们也可以使用不同类型的引号: ------")

print('doesn\'t')
print("doesn't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

print("------ 在 Python shell 中，字符串定义和输出字符串看起来可能不同。 print() 函数会略去标示用的引号，并打印经过转义的特殊字符，产生更为易读的输出: ------")
s = 'First line.\nSecond line.'  # \n means newline
print(s)

print("------ 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可：-------")
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("----- 字符串可以用 + 合并（粘到一起），也可以用 * 重复：-------")
print(3 * 'un' + 'ium')

print("------ 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并：-------")
print('Py' 'thon')

print("------ 拼接分隔开的长字符串时，这个功能特别实用：--------")
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

print("------ 字符串支持 索引 （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：-------")
word = 'Python'
print(word[0])         # character in position 0)
print(word[5])

print("------ 索引还支持负数，用负数索引时，从右边开始计数：----------")
print(word[-1])
print(word[-6])

print("----- 注意，-0 和 0 一样，因此，负数索引从 -1 开始。除了索引操作，还支持 切片。 索引用来获取单个字符，而 切片 允许你获取子字符串:----- ")
print(word[0:2])
print(word[0:5])

print("----- 切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：----- ")
print(word[:2])
print(word[4:])
print(word[-2:])

print("----- 注意，输出结果包含切片开始，但不包含切片结束。因此，s[:i] + s[i:] 总是等于 s：----- ")
print(word[:2] + word[2:])
print(word[:4] + word[4:])