"""
    @project: stuPython
    @Author：Murk
    @file： 任务二.py
    @date：2024/6/2 16:26
    @Desc: 模拟淘宝客服自动回复
"""
def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:    # if line == ''  到文件末尾退出
                break
            # 字符串的分隔
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question = input('你好，小米等你的问题：')
    while True:
        if question == 'bye':
            break
        # 开始在文件中查找
        replay = find_answer(question)
        if not replay:     # 如果回复的是False， not false --> True
            question = input('不知道你讲的啥，你可以问一下关于订单｜物流｜账单｜支付的问题（退出输入bye）：')
        else:
            print(replay)
            question = input('你好，还可以继续问关于订单的问题（退出输入bye）：')
    print('结束')