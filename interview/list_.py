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

"""
123
[11, 12, 13, 14, 15, 16, 17, 18, 19]
[11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

"""
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
"""

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'X'

print(weird_board)

"""
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
[['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
"""

t = (1, 2, [30, 40])

# TypeError: 'tuple' object does not support item assignment
try:
    t[2] += [50, 60]
except Exception as e:
    print(e)

print(t)

"""
'tuple' object does not support item assignment
(1, 2, [30, 40, 50, 60])
"""

t[2].extend([5, 6])

print(t)
"""
(1, 2, [30, 40, 50, 60, 5, 6])
"""

fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits, reverse=False))
print(sorted(fruits, reverse=True))
print(sorted(fruits, reverse=True, key=lambda x: len(x)))
print(sorted(fruits, reverse=True, key=len))
