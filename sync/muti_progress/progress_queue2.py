import time
from threading import Thread


# 共享全局变量通信
# 共享全局变量不使用于多进程编程，使用与多线程

def product(a):
    for i in range(10):
        a[i] = i+1


def consume(a):
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = {}
    p = Thread(target=product, args=(a,))
    c = Thread(target=consume, args=(a,))

    p.start()
    c.start()
    p.join()
    c.join()
