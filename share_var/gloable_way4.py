import threading


def consume4():
    k = list(range(10000))
    for i in k:
        with open('a.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))


def consume3():
    k = list(range(10000))
    for i in k:
        with open('a.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))


def consume1():
    k = list(range(10000))
    for i in k:
        with open('a.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))


def consume():
    k = list(range(10000))
    for i in k:
        with open('a.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))


if __name__ == '__main__':
    from threading import Thread

    t1 = Thread(target=consume, name='t1')
    t2 = Thread(target=consume1, name='t2')
    # t3 = Thread(target=consume3, name='t3')
    # t4 = Thread(target=consume4, name='t4')
    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
