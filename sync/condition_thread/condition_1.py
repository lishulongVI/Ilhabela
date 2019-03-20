import threading
from threading import Lock


# 条件变量  用于复杂的线程同步
# 当前无法实现你一下我一下 怎么实现呢 引入condition

class Consume(threading.Thread):
    def __init__(self, lock: Lock):
        super().__init__(name='consume')
        self.lock = lock

    def run(self):
        for i in range(100):
            self.lock.acquire()
            print(threading.current_thread().name, ":", i)
            self.lock.release()


class Product(threading.Thread):
    def __init__(self, lock: Lock):
        super().__init__(name='Product')
        self.lock = lock

    def run(self):
        for j in range(100):
            self.lock.acquire()
            print(threading.current_thread().name, ":",  j)
            self.lock.release()


if __name__ == '__main__':
    locks = Lock()
    c = Consume(locks)
    p = Product(locks)

    p.start()
    c.start()

    c.join()
    p.join()
