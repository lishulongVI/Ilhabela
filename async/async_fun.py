# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/25 下午9:57
"""

import asyncio


def callback(k):
    print('callback', k)


def stop_loop(loop):
    loop.stop()


def call_time(k, loop):
    print('sss', loop.time())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_soon(callback, 2)
    loop.call_later(3, callback, 2)
    loop.call_later(4, callback, 2)
    print(now)
    loop.call_at(now + 2, call_time, 2, loop)
    loop.call_at(now + 3, call_time, 1, loop)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()
