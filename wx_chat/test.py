#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import asyncio
import time
import random
from random import randint

import requests
import re
# Create your views here.

'''
获取二维码，并在自己网站上显示
:param request:
:return:
'''
# CTIME=time.time()
# response=requests.get(
#     url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&lang=zh_CN&_=%s' %CTIME
# )
# print(response.text)
# v=re.findall('uuid = "(.*)";',response.text)
# global QCODE
# QCODE=v[0]

async def print_num(n,sem):
    with await sem:
        print(f'{n}:1')
        await asyncio.sleep(random.randint(3,6))
        print(f'{n}:2')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n}:3')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n}:4')
        await asyncio.sleep(random.randint(3, 6))
        print(f'{n}:5')
if __name__ == '__main__':
    sem = asyncio.Semaphore(2)

    loop=asyncio.get_event_loop()
    tasks=[]
    for i in range(4):
        # print(i)
        tasks.append(print_num(i,sem))
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()



