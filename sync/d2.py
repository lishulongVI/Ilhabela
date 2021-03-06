from threading import Lock

a = 0

lock = Lock()


def add():
    global a
    # global lock
    for i in range(1000000):
        lock.acquire()
        a += 1
        lock.release()


def desc():
    global a
    # global lock
    for i in range(1000000):
        lock.acquire()
        a -= 1
        lock.release()


if __name__ == '__main__':
    """
    锁会影响性能
    锁可能会引起死锁。资源竞争
    """
    from threading import Thread

    t1 = Thread(target=add, name='add')
    t2 = Thread(target=desc, name='desc')

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(a)
