"""
    @project: stuPython
    @Author：Murk
    @file： 3-7 第三方模块的安装及使用.py
    @date：2024/5/4 07:56
    @Desc: 
"""
import sys
import time
import urllib.request
import math
import schedule

print(sys.getsizeof(24))
print(sys.getsizeof(28))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print('-'*6+'time的使用'+'-'*6)
print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)

def job():
    print('hahha')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)