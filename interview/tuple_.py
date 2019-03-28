# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/28 下午9:44
"""

import os

# 可以用于没有字段名的记录  不可变的

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

ts = [('name', 'li'), ('age', 20), ('address', 'tokyo')]

for k, v in ts:
    print(k, v)

# 元组拆包
a, c = os.path.split('/Users/lishulong/Desktop/github/Ilhabela/README.md')
print(a, c)

a, b, c, *d = range(20)
print(a, b, c, d)

a, b, *c, d = range(20)
print(a, b, c, d)

"""
name li
age 20
address tokyo
/Users/lishulong/Desktop/github/Ilhabela README.md
0 1 2 [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
0 1 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] 19
"""

# collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有
# 名字的类——这个带名字的类对调试程序有很大帮助。

#  创建一个具名元组需要两个参数
from collections import namedtuple

g = namedtuple('Goods', ['name', 'image_key', 'sku', 'price'])
g_a = g(name='adidas', image_key='iamge_key', sku=100, price=499)
print(g_a.name)

print(g._fields)

print(g_a._asdict())

for k, v in g_a._asdict().items():
    print(k, v)
