#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from requests.cookies import RequestsCookieJar

__author__ = 'Terry'

import requests


def load_cookie(s):
    file = 'sina_cookies.txt'
    with open(file, 'r') as f:
        cookies = json.load(f)
        jar = RequestsCookieJar()
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])

        s.cookies = jar


if __name__ == '__main__':
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    url = 'https://weibo.cn/?tf=5_009'

    r = s.get(url)

    if '木木2018' in r.text:
        print('登录成功')
    else:
        print('未登录')

    load_cookie(s)

    r = s.get(url)

    if '木木2018' in r.text:
        print('登录成功')
    else:
        print('未登录')

    print('完成')