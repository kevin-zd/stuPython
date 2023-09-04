class Test:
    def _init_(self):
        self.word = "hello"
        self._num = 100

def func():
    return ('Hello')
def _private_func():
    return ('bytedance')

if __name__ == '_main_':
    test = Test()
    print(test.word)
    print(test.num)
    print(func())
    print(_private_func())