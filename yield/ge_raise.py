# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:41
"""


def ge1():
    try:
        yield 0
    except Exception as e:
        print(e)
    yield 1
    yield 2
    yield 4


if __name__ == '__main__':
    g = ge1()

    print(next(g))
    g.throw(Exception, "over")
    print(next(g))
    g.throw(Exception, "over")
