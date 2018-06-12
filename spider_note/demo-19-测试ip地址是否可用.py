#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.mysql_handle import get_many, get_one, delete
import requests

__author__ = 'Terry'

def visit_baidu(ip, port):
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.proxies = {
        'https': f'{ip}:{port}',
        'http': f'{ip}:{port}',
    }

    try:
        r = s.get('https://www.qidian.com', timeout=5)
        return True
    except:
        return False

def check_ip(id=0):
    while True:
        row = get_one(f'select id, ip, port from ips where id >{id} limit 1')
        b = visit_baidu( row.get('ip'), row.get('port'))
        if b:
            print('ip是OK:', row.get('ip'))
        else:
            id = row.get('id')
            delete(f'delete from ips where id={id}')
            print(f'删除id为：{id} 的记录')

if __name__ == '__main__':
    check_ip()