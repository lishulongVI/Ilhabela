# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/4/19 下午1:40
"""
import aiohttp
import asyncio

url = ''
import time


async def sleep():
    time.sleep(1)


async def fetch(
        url="https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp"):
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            async with session.get(url) as res:
                asyncio.sleep(1)
                # print('url status', res.status)
                print(await res.text())


async def fetch1(
        url="https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp"):
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(force_close=True, enable_cleanup_closed=True)) as session:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            # print('url status', res.status)
            asyncio.sleep(1)
            return await res.text()


from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/hello')
async def zsh(request):
    # loop = asyncio.get_event_loop()
    # tasks = [fetch1() for iK in range(10)]
    q = await fetch1()
    asyncio.sleep(1)
    # loop.run_until_complete(asyncio.wait(tasks))
    return json({'Hello': q})


if __name__ == '__main__':
    app.run(debug=True, port=3900)
    # t = time.time()s
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(fetch())
    #
    # t1 = time.time()
    # print(t1 - t)
