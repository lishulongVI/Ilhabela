# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/28 下午11:09
"""
# memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切 片。

# memoryview.cast 的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容 字节不会随意移动。

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

print(numbers)

memv = memoryview(numbers)

print(memv)

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4

print(memv_oct.tolist())

print(numbers)


"""
array('h', [-2, -1, 0, 1, 2])
<memory at 0x105679948>
-2
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
[254, 255, 255, 255, 0, 4, 1, 0, 2, 0]
array('h', [-2, -1, 1024, 1, 2])

"""