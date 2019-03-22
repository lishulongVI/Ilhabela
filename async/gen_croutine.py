# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午11:50
"""
import inspect


def gen1():
    yield 1
    return 'hello'


if __name__ == '__main__':
    ge = gen1()

    print(inspect.getgeneratorstate(ge))
    next(ge)
    print(inspect.getgeneratorstate(ge))
    try:
        next(ge)
    except Exception as e:
        pass
    # next(ge)
    print(inspect.getgeneratorstate(ge))
    # next(ge)
