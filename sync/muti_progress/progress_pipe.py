import time

from multiprocessing import Pipe, Process


def product(pipe):
    pipe.send('send product')


def consume(pipe):
    time.sleep(2)
    print(pipe.recv())


def fe(a):
    print('result', a)


# pipe 实现进程间通信
# pipe性能高于queue


if __name__ == "__main__":
    # 仅仅适用于两个进程间的通信
    rece, send = Pipe()
    p = Process(target=product, args=(send,))
    c = Process(target=consume, args=(rece,))
    p.start()
    c.start()
    p.join()
    c.join()
