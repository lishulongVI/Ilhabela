# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/11/24 上午9:41
"""

'''
"Sequence", "MutableSequence",

魔法函数 构成了 序列的学医
'''

from collections.abc import MutableSequence


class SequenceClazz(MutableSequence):
    def __len__(self):
        pass

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __getitem__(self, index):
        pass

    def insert(self, index, value):
        pass


# + += extend
a = [1, 2]
c = a + [3, 4]
print(c)

# iadd
a += [3, 4]
print(a)

# 拆箱？
a += (3, 4)
print(a)

a.extend(c)
print(a)
