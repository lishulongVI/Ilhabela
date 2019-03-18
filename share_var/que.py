import time
from queue import Queue
import threading


def product(queue: Queue):
    for i in range(1000):
        queue.put(i)


def consume(queue: Queue):
    while True:
        k = queue.get()
        print(k, queue.qsize(), threading.current_thread().name)
        time.sleep(0.1)


if __name__ == '__main__':
    que = Queue(maxsize=1000)

    from threading import Thread

    Thread(target=product, args=(que,), name='t1', daemon=True).start()
    Thread(target=consume, args=(que,), name='t2', daemon=True).start()
    Thread(target=consume, args=(que,), name='t3', daemon=True).start()
    que.join()

    print('end.....')
