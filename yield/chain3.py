# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:54
"""


def g1(gen):
    yield from gen


if __name__ == '__main__':
    # g1  委托生成器  gen 子生成器
    # yeild from 会和 委托生成器 建立双向通道
    g = g1()
    g.send(range(10))
