# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午11:38
"""
import types
# from collections import Awaitable


@types.coroutine
def cacule(l):
    yield l + 1


async def calculate(l):
    res = await cacule(l)
    print(res)
    return res


if __name__ == '__main__':
    c = calculate(12)
    # next(c)  # sys:1: RuntimeWarning: coroutine 'calculate' was never awaited
    c.send(None)

