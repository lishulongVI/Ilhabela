# semaphore 是用于控制进入数量的锁


import threading

import time
import datetime


class Read(threading.Thread):
    def run(self):
        time.sleep(2)
        print('Reading....', datetime.datetime.now())


class Write(threading.Thread):
    def run(self):
        q = []
        for i in range(20):
            r = Read()
            r.start()
            q.append(r)
        for i in q:
            i.join()


if __name__ == '__main__':
    a = datetime.datetime.now()
    w = Write()
    w.start()
    w.join()
    print(datetime.datetime.now() - a)
