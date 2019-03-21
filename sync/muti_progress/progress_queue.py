import time
from multiprocessing import Process
from multiprocessing import Queue


def product(que):
    for i in range(10):
        que.put(i)
        time.sleep(1)


def consume(que):
    time.sleep(1)
    while True:
        data = que.get()
        print(data)
    pass


if __name__ == "__main__":
    que = Queue(10)
    p = Process(target=product, args=(que,))
    c = Process(target=consume, args=(que,))

    p.start()
    c.start()
    p.join()
    c.join()
