# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:44
"""

from itertools import chain

ls = range(10)

dic = {
    '1': 1,
    '3': 1,
    '2': 2
}

for value in chain(ls, dic, [12, 3, 45, ]):
    print(value)


def chain_1(*args, **kwargs):
    for i in args:
        for j in i:
            yield j


for value in chain_1(ls, dic, [12, 3, 4, 5]):
    print(value)


def chain_2(*args, **kwargs):
    for i in args:
        yield from i


for value in chain_2(ls, dic, [1, 23, 4, 5, 6]):
    print(value)
