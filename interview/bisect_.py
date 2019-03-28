# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/28 下午11:00
"""
import sys
# bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素。

import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

""""
DEMO: bisect
haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
31 @ 14     | | | | | | | | | | | | | |31
30 @ 14     | | | | | | | | | | | | | |30
29 @ 13     | | | | | | | | | | | | |29
23 @ 11     | | | | | | | | | | |23
22 @  9     | | | | | | | | |22
10 @  5     | | | | |10
 8 @  5     | | | | |8 
 5 @  3     | | |5 
 2 @  1     |2 
 1 @  1     |1 
 0 @  0    0 


➊ 用特定的 bisect 函数来计算元素应该出现的位置。 ➋ 利用该位置来算出需要几个分隔符号。
➌ 把元素和其应该出现的位置打印出来。
➍ 根据命令上最后一个参数来选用 bisect 函数。
➎ 把选定的函数在抬头打印出来。
"""

import bisect
import random

SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

""""
10 -> [10]
 0 -> [0, 10]
 6 -> [0, 6, 10]
 8 -> [0, 6, 8, 10]
 7 -> [0, 6, 7, 8, 10]
 2 -> [0, 2, 6, 7, 8, 10]
10 -> [0, 2, 6, 7, 8, 10, 10]
"""
