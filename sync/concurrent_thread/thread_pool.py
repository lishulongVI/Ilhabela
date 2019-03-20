from concurrent.futures import ThreadPoolExecutor

# 线程池的应用
# 1、主线程中方可以获取某一个线程的状态，或者某一个任务的状态，和返回值 。当一个线程完成的时候 主线程能知道

# 2、futures 可以让多线程和多进程编码接口一致
import time
from datetime import datetime


def read(date):
    time.sleep(date)
    print('readed //',date)
    return date


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=1)
    print(datetime.now())
    t1 = pool.submit(read, 1)
    # Cancel the future if possible.
    #
    #     Returns True if the future was cancelled, False otherwise. A future
    #     cannot be cancelled if it is running or has already completed.

    t2 = pool.submit(read, 2)
    # 当线程池中的资源不足，挂起的任务可以进行取消，其他的不能取消
    print(t2.cancel())
    # 判断任务是否执行完成
    # print(t1.done())
    # print(t2.done())
    # time.sleep(5)

    # 获取执行结果
    print(t1.result())
    # print(t2.result())

    #

    print(datetime.now())
    time.sleep(32)
