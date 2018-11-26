import threading
import time
class Mythread(threading.Thread):

    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print('{} has started.'.format(self.number))
        self.func(*self.args)
        print('{} has finished'.format(self.number))


def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)

# for i in range(4):
#     t = Mythread(target=sleeper,
#                  name='thread {}'.format(i+1),
#                  args=(3, 'thread {}'.format(i+1)))
#     t.start()

threads_list = []

for i in range(50):
    t = Mythread(number=i+1, func=double, args=[i, 3])
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()
