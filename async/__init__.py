# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午11:37
"""

import requests


def kkk(i):
    print(i)
    print(i, requests.get('http://127.0.0.1:3900/hello').text)


from multiprocessing.pool import ThreadPool

pool = ThreadPool(500)
pool.map(kkk, range(500))
