import time
from threading import Thread


# 共享全局变量通信
# 共享全局变量不使用于多进程编程，使用与多线程

def product(a):
    a = a + 10
    print(a)


def consume(a):
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = 11
    p = Thread(target=product, args=(a,))
    c = Thread(target=consume, args=(a,))
    c.start()
    p.start()
    p.join()
    c.join()
