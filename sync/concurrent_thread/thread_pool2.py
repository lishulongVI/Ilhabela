from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED

# 线程池的应用
# 1、主线程中方可以获取某一个线程的状态，或者某一个任务的状态，和返回值 。当一个线程完成的时候 主线程能知道

# 2、futures 可以让多线程和多进程编码接口一致
import time
from datetime import datetime


def read(date):
    time.sleep(date)
    print('read //', date)
    return date


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=1)
    print(datetime.now())
    date = [1, 2, 3, 4, 5]
    # 方式1
    all_task = [pool.submit(read, i) for i in date]
    # wait(all_task, return_when=FIRST_COMPLETED)  #执行完第一个就进入主线程
    wait(all_task)  # 搞完所有的线程才回进如主线程
    print('wait ?')

    # for future in as_completed(all_task):
    #     print(future.result())
    # # 方式2
    # result = pool.map(read, date)
    # for i in result:
    #     print(i)
