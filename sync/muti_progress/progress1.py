# gil 消耗cpu的操作 使用多进程编程
# 对io 操作来说 使用多线程编程，进程切换代价高于 线程切换
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time


# 对于耗费cpu的 密集型计算 多进程比多线程好


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # 20  消耗128.60890364646912
    # 4  end... 135.17767071723938
    # 8  end... 125.89682006835938
    # with ProcessPoolExecutor(8) as pool:
    #     tasks = [pool.submit(fib, i) for i in range(21, 45)]
    #     a = time.time()
    #     print('start...', a)
    #     for f in as_completed(tasks):
    #         print(f.result())
    #     print('end...', time.time() - a)
    with ThreadPoolExecutor(8) as pool:
        tasks = [pool.submit(fib, i) for i in range(21, 45)]
        a = time.time()
        print('start...', a)
        for f in as_completed(tasks):
            print(f.result())
        print('end...', time.time() - a)
