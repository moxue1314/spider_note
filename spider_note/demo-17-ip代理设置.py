#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
s=requests.Session
# 1、requests的 proxies设置，网络访问的代理ip的顺序
s.proxies = {
    'http': '127.0.0.1:8888',
    'https':  '127.0.0.2:9999'
}

    # 网络访问的时候：
    # http://www.baidu.com ：  优先找到 8888
    # https://www.baidu.com ： 优先找到  9999

    # 现在的版本不是这样，设置代理，在不清楚访问的服务器是http协议还是https的时候，或者说2个协议都需要进行访问时，
    # 代理设置应该如下
s.proxies = {
    'https': '127.0.0.1:8888',
    'http': '127.0.0.1:8888',
}

#--------------------------
import requests

if __name__ == '__main__':
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.proxies = {
        'http': '115.218.126.161:9000'
    }
    r = s.get('http://www.baidu.com')
    print(r.text)