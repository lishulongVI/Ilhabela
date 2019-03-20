# import os
# import time
# # linux exec
# pid = os.fork()
#
# print('hello')
#
# if pid == 0:
#     print(os.getpid(), os.getppid())
# else:
#     print(pid)
#
# time.sleep(2)
import multiprocessing
from multiprocessing import Process
import time


def read(h):
    time.sleep(h)
    print('read ///')
    return h


if __name__ == '__main__':
    # print(multiprocessing.cpu_count())
    # process = Process(target=read, args=(2,))
    # print(process.pid)
    #
    # process.start()
    # print(process.pid)
    # process.join()
    # print('end///')
    # print(process.pid)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # res = pool.apply_async(read, args=(2,))
    # pool.close()
    # pool.join()
    # print(res.get())

    for r in pool.imap(read, [1, 2, 3, 4]):
        print(r)

    for r in pool.imap_unordered(read, [1, 5, 3, 4]):
        print(r)
