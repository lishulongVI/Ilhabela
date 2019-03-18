from share_var.gloable import lis
from share_var.gloable_demo import change
import threading


def consume():
    while True:
        if len(lis) > 0:
            print(lis.pop(), threading.current_thread().name)


if __name__ == '__main__':
    from threading import Thread

    t1 = Thread(target=change, name='t1')
    t2 = Thread(target=consume, name='t2')
    t3 = Thread(target=consume, name='t3')
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
