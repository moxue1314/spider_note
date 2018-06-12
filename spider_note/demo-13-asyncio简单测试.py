#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import random

import time

__author__ = 'Terry'

async def print_num(n, sem):
    async with sem:
        print(f'{n} : 1')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n} : 2')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n} : 3')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n} : 4')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n} : 5')

if __name__ == '__main__':
    # 初始化，控制协程并发的数量
    sem = asyncio.Semaphore(5)

    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(2000):
        tasks.append(print_num(i, sem))
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()