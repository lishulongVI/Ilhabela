# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/22 下午10:54
"""

result = {}


def calculate(name):
    t = 0
    number = []
    while True:
        x = yield
        print(name, x)
        if not x:
            break
        t += x
        number.append(x)

    return t, number


def mid(key):
    while True:
        result[key] = yield from calculate(key)
        print('key ok', key)


if __name__ == '__main__':
    dic = {
        'bul moon2': [11, 22, 33, 44],
        'bul moon1': [1, 2, 3, 4]
    }

    for k, v in dic.items():
        m = mid(key=k)
        m.send(None)
        for i in v:
            m.send(i)
        m.send(None)

    print(result)
