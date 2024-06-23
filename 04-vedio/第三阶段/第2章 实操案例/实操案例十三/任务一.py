"""
    @project: stuPython
    @Author：Murk
    @file： 任务一.py
    @date：2024/6/2 14:54
    @Desc: 编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
"""
class Instrument():
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')

class Pinao(Instrument):
    def make_sound(self):
        print('钢琴在演奏')

class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

# 演奏的函数
def play(instrument):
    instrument.make_sound()

class Bird():
    def make_sound(self):
        print('小鸟在唱歌')

if __name__ == '__main__':
    play(Erhu())
    play(Pinao())
    play(Violin())
    play(Bird())