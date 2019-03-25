# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/3/25 下午11:22
"""

import aiohttp
import asyncio

url = ''


async def fetch(
        url="https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp"):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('url status', res.status)
            print(await res.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch())
