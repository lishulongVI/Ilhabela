# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:44
"""


def g1(ite):
    yield ite


def h1(ite):
    yield from ite


for value in g1([1, 23, 4, ]):
    print(value)

for value in g1(range(10)):
    print(value)

for v in h1(range(10)):
    print(v)
