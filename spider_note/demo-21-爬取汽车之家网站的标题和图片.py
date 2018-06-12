#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
直接requests.get(网址)将整个页面下载下来，然后用bs4或者xpath做内容筛选
'''


import requests
from bs4 import BeautifulSoup
response = requests.get(
    url='http://www.autohome.com.cn/news/'
)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,features='html.parser')
target = soup.find(id='auto-channel-lazyload-article')
li_list = target.find_all('li')
for i in li_list:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3').text # 什么类型?
        print(txt)
        img_url ='https:' + a.find('img').attrs.get('src')
        print(img_url)

        img_response = requests.get(url=img_url)
        import uuid
        file_name = str(uuid.uuid4()) + '.jpg'
        with open(file_name,'wb') as f:
            f.write(img_response.content)