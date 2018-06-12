#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from db.mysql_handle import get_one, delete
from concurrent import futures
import urllib3
urllib3.disable_warnings()
__author__ = 'Terry'

def change_ip(s, id=None):
    if id:
        delete(f'delete from ips where id={id}')

    row = get_one('select id, ip, port from ips order by id limit 2, 1')
    id = row.get('id')
    ip = row.get('ip')
    port = row.get('port')
    s.proxies = {
        'http': f'{ip}:{port}',
        'https': f'{ip}:{port}',
    }

    return id

def visit_qidian(isss):
    while True:
        s = requests.session()
        s.trust_env = False
        s.verify = False
        s.headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/plain, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        url = 'https://www.qidian.com/'

        for _ in range(10):
            id = change_ip(s)

            try:
                r = s.get(url, timeout=5)
                r.encoding = 'utf-8'
                text = r.text
                # print(text)
                print('可用的ip:', s.proxies)
                break
            except:
                print('代理不可用，更换IP')
                change_ip(s, id)

def thread_visit():
    with futures.ThreadPoolExecutor(max_workers=1) as  executor:
        # for _ in range(10):
            executor.submit(visit_qidian, 1)

if __name__ == '__main__':
    thread_visit()