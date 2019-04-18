# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/4/18 上午11:08
"""
import aiohttp
import asyncio

url = ''
import time


async def fetch(
        url="https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp"):
    for i in range(10):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                # print('url status', res.status)
                print(await res.text())


async def fetch1(
        url="https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp"):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            # print('url status', res.status)
            print(await res.text())


if __name__ == '__main__':
    t = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch())

    t1 = time.time()
    print(t1-t)

    loop = asyncio.get_event_loop()
    tasks = [fetch1() for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - t1)
