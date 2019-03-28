# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/28 下午9:38
"""

x = '123'

d = [x for x in range(10)]

print(x)

# python2 和python3的不同之处



ak = [x for x in range(20) if x > 10]

print(ak)

print(list(filter(lambda x: x > 10, range(20))))
