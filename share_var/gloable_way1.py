from share_var import gloable
import threading


def consume():
    for i in gloable.lis:
        with open('aab.txt', 'a+') as file:
            file.write('{},{}\n'.format(i, threading.current_thread().name))


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
