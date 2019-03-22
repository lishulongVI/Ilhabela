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


if __name__ == '__main__':
    dic = {
        'bul moon2': [11, 22, 33, 44],
        'bul moon1': [1, 2, 3, 4]
    }

    m = calculate('name')
    m.send(None)
    m.send(12)
    m.send(13)
    m.send(14)
    try:
        m.send(None)
    except Exception as e:
        print(e.value)
