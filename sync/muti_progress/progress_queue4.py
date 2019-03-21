import time

from multiprocessing import Pool


# mutiprocessing 中的queue不能用于pool 线程池

# poll中的进程间通信需要使用manager中的queue

def product(que):
    que.put(1000)
    time.sleep(2)
    return 'hahahas'


def consume(que):
    time.sleep(2)
    print(que.get())


def fe(a):
    print('result', a)


if __name__ == "__main__":
    from multiprocessing import Manager

    que = Manager().Queue(10)
    p = Pool(2)
    p.apply_async(product, args=(que,), callback=fe)
    p.apply_async(consume, args=(que,))
    # p.close()
    # p.join()
    time.sleep(100)
