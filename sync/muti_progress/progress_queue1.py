import time
from multiprocessing import Process
from multiprocessing import Queue


# 共享全局变量通信
# 共享全局变量不使用于多进程编程，使用与多线程

def product(a):
    a[1] = 2


def consume(a):
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = {}
    p = Process(target=product, args=(a,))
    c = Process(target=consume, args=(a,))

    p.start()
    c.start()
    p.join()
    c.join()
