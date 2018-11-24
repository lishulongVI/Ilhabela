# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/11/24 上午9:56
"""

li = [1, 2, 3, 4, 5, 6, 7]

# 切片会返回一个新的列表

print(li[::])
print(li[::-1])
# 取偶数位置  0 2，4
print(li[::2])
print(li[1::2])

print(li[100:])

print(li[0:100])

# TypeError: can only assign an iterable
# li[len(li):] = 1
li[len(li):] = [1]
print(li)

li[:0] = [1, 2]
print(li)

li[::2] = [0] * 5

print(li)

li[:3] = []

print(li)

del li[:3]
print(li)
del li[::2]
