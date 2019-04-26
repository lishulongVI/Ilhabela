# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/4/26 下午5:22
"""

import datetime
import gevent
from gevent import monkey

#
# 存在http 请求的时候要 patch
monkey.patch_socket()


#
# # patches stdlib (including socket and ssl modules) to cooperate with other greenlets

def g(i):
    gevent.sleep(1)
    if i == 2:
        raise Exception
    return i


a = datetime.datetime.now()

b = gevent.joinall([
    gevent.spawn(g, 1),
    gevent.spawn(g, 1),
    gevent.spawn(g, 2),
    gevent.spawn(g, 1),
    gevent.spawn(g, 1),
    gevent.spawn(g, 1),
])

for bb in b:
    if not bb.exc_info:
        print(bb.value)

print((datetime.datetime.now() - a).total_seconds())
