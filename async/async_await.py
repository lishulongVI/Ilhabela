# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午11:38
"""


async def cacule(l):
    return l + 1


async def calculate(l):
    res = await cacule(l)
    return res


if __name__ == '__main__':
    c = calculate(12)
    # next(c)  # sys:1: RuntimeWarning: coroutine 'calculate' was never awaited
    c.send(None)
