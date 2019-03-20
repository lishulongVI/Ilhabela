# semaphore 是用于控制进入数量的锁


import threading
import time
import datetime
from threading import Semaphore


class Read(threading.Thread):
    def __init__(self, semaphore):
        super().__init__()
        self.semaphore = semaphore

    def run(self):
        time.sleep(2)
        print('Reading....', datetime.datetime.now())
        self.semaphore.release()


class Write(threading.Thread):
    def __init__(self, semaphore):
        super().__init__()
        self.semaphore = semaphore

    def run(self):
        q = []
        for i in range(20):
            self.semaphore.acquire()
            r = Read(self.semaphore)
            r.start()
            q.append(r)
        for i in q:
            i.join()


if __name__ == '__main__':
    a = datetime.datetime.now()
    s = Semaphore(1)
    w = Write(s)
    w.start()
    w.join()
    print(datetime.datetime.now() - a)
