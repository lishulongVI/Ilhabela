a = 0


def add():
    global a
    for i in range(1000000):
        a += 1


def desc():
    global a
    for i in range(1000000):
        a -= 1


if __name__ == '__main__':
    from threading import Thread

    t1 = Thread(target=add, name='add')
    t2 = Thread(target=desc, name='desc')

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(a)
