# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:29
"""


def ge1():
    # try:
    #     yield 'hello yield1'
    # except GeneratorExit as e:
    #     pass
    #     # print(e)

    try:
        yield 1
    except Exception as e:
        pass
    yield 2
    yield 3


if __name__ == "__main__":
    # for i in ge1():
    #     print(i)
    g1 = ge1()
    print(next(g1))
    g1.close()
    print('end。。')
