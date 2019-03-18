import threading
from threading import Lock

lock = Lock()


def consume():
    lock.acquire()
    k = list(range(10000))
    for i in k:
        with open('a.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))
    lock.release()

if __name__ == '__main__':
    from threading import Thread

    t1 = Thread(target=consume, name='t1')
    t2 = Thread(target=consume, name='t2')
    t3 = Thread(target=consume, name='t3')
    t4 = Thread(target=consume, name='t4')
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
