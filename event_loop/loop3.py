# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/23 上午12:42
"""

# 事件循环 + 回调 + epoll （io多路复用）

# asyncio 是python用于解决异步io编程的一整套方案

# 应用： tornado gevent twisted  scrapy  django channels

# tornado 协程+事件循环 实现高并发 实现web服务器 可直接部署  nginx + tornado  使用数据源的时候不能直接使用我们传统 的包

# django + flask 传统阻塞io的编程模型，部署的时候 wsgi gunicorn = nginx
import time
# # 同步阻塞的接口
import asyncio


async def get_result(url):
    print('to get html…')
    await asyncio.sleep(2)
    print('end get html..')
    return 'hello'



if __name__ == '__main__':
    t = time.time()
    loop = asyncio.get_event_loop()
    ger = asyncio.ensure_future(get_result('hellos'))
    loop.run_until_complete(ger)
    print(ger.result())
    print(time.time() - t)
