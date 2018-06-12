#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from lxml import etree

# 抽屉网程序自动验证

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
#随便访问抽屉网的一个网址获取cookies
# r1 = requests.get('http://dig.chouti.com/',headers=headers)
# r1_cookies = r1.cookies.get_dict()
# print(r1_cookies)
#保存登录名和密码
post_dict = {
    "phone": '8613391575901',
    'password': 'leilei32553589',
    'oneMonth': 1
}
#利用requests.post()携带密码、headers、cookies自动登录抽屉网
# r2 = requests.post(
#     url="https://dig.chouti.com/login",
#     data=post_dict,
#     headers=headers,
#对第一次的cookies的gpsd进行授权
#     cookies=r1_cookies
# )
# print(r2.cookies.get_dict()['gpid'])
#
#自动推荐和取消推荐，必须携带cookies和headers
# r3=requests.post(
#     url='https://dig.chouti.com/link/vote?linksId=20155126',
#     cookies={'gpsd':r1_cookies['gpsd']},
#     headers=headers
# )
# print(r3.text)

#！！！！！！！！！！！！！！
#利用session可以保存cookies进行自动登录，但抽屉网还是需要headers
session=requests.Session()
### 1、首先登陆任何页面，获取cookie
i1 = session.get(url="http://dig.chouti.com/help/service",headers=headers)
print(i1.cookies.get_dict())

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2=session.post(
    url='https://dig.chouti.com/login',
    data=post_dict,
    headers=headers
)
print(i2.cookies.get_dict())

i3=session.post(
    # url='https://dig.chouti.com/link/vote?linksId=20155361',
    url='https://dig.chouti.com/vote/cancel/vote.do',
    headers=headers,
    data={'linksId': '20155361'}
)
print(i3.cookies.get_dict())
print(i3.text)
# content=i3.content.xpath()