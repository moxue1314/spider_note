#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'


# 简单请求示例
import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    async with async_timeout.timeout(10):
        # response = await session.get(url)
        async with session.get(url) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.baidu.com')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

#---------------------------------------------

# sem 示例
import random
import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(random.random())
    return x + y


async def print_sum(x, y, sem):
    # 这里控制并发的任务数
    async with sem:
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
# 控制并发数
sem = asyncio.Semaphore(5)
loop.run_until_complete(asyncio.gather(*[print_sum(i, i + 1, sem) for i in range(100)]))
loop.close()