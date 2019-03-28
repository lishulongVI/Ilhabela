# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/28 下午10:18
"""
# 切片

s = ['这是我的测试1', '这是我的测试2', '这是我的测试3']

# 间隔1个
print(s[::2])

# 倒叙
print(s[::-1])

print(s[::1])
# 倒序列隔一个
print(s[::-2])

print(s[2:3])
# 给切片赋数值
# TypeError: 'str' object does not support item assignment s 为str
# TypeError: can only assign an iterable
# s[2:3] = 1
s[2:3] = [2]
print(s)

del s[2:5]
print('delete....')
print(s)
s[2:5] = ['wo']

print(s)


"""
['这是我的测试1', '这是我的测试3']
['这是我的测试3', '这是我的测试2', '这是我的测试1']
['这是我的测试1', '这是我的测试2', '这是我的测试3']
['这是我的测试3', '这是我的测试1']
['这是我的测试3']
['这是我的测试1', '这是我的测试2', 2]
delete....
['这是我的测试1', '这是我的测试2']
['这是我的测试1', '这是我的测试2', 'wo']
"""
