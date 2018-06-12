#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

__author__ = 'Terry'

"""
    需求：
    登录 微博手机版
    2.1 获取前50条微博的标题
    2.2 点击消息，往 新浪新闻 发送 3条消息，消息内容随意！


    1、抓包
    2、拷贝上节课实现的sina微博手机版登录的代码
    3、获取50条博客，是访问 friends 页面，根据计算页码数，进行分页获取
    4、发送消息：
        查找到核心请求 https://m.weibo.cn/msgDeal/sendMsg?
            fileId	null   ： 不理会
            uid	2028810631   ： 查找，定位到：https://m.weibo.cn/msg/index?format=cards
            content	啊收手四达大厦  ： 自己定义的消息内容
            st	  acc368   ： 查找，定位到：https://m.weibo.cn/ 请求的resposne中， "st":"acc368"
    5、测试后，发现直接发送 sendMsg 会 -99 错误，需要先打开聊天室：
        https://m.weibo.cn/msg/chat?uid=2028810631
    6、sendMsg 发送，需要修改 s.headers['Referer']
"""

import requests
import re
import urllib3

urllib3.disable_warnings()


def visit_start(s):
    url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
    s.get(url)


def visit_login(s, user, pwd):
    url = 'https://passport.weibo.cn/sso/login'
    data = {
        'username': user,
        'password': pwd,
        'savestate': '1',
        'r': 'http://m.weibo.cn/',
        'ec': '0',
        'pagerefer': '',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'mainpageflag': '1',
        'hff': '',
        'hfp': ''
    }
    headers = {
        'Connection': 'keep-alive',
        'Origin': 'https://passport.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    r = s.post(url, data=data, headers=headers)


def visit_index(s):
    url = 'https://m.weibo.cn/'
    r = s.get(url)
    encoding = re.search(b'<meta.*?charset="(.*?)">', r.content, re.RegexFlag.S | re.RegexFlag.M).group(1)
    r.encoding = encoding
    text = r.text
    st = re.search(r'"st":"(.*?)",', text, re.RegexFlag.S).group(1)

    t = '随时随地发现新鲜事'
    if t in text:
        print('登录成功')
    else:
        print('登录失败')

    return st


def visit_friends(s):
    url = 'https://m.weibo.cn/feed/friends?version=v4'
    r = s.get(url)
    json_data = r.json()
    card_group = json_data[0]['card_group']

    for card in card_group[1:6]:
        mblog = card['mblog']
        print('博主：', mblog['source'])
        print('标题：', mblog['user']['screen_name'])
        print('内容：', mblog['text'][:10])


def visit_friends_by_url(s, url, is_first=False):
    r = s.get(url)
    json_data = r.json()
    next_cursor = json_data[0]['next_cursor']
    card_group = json_data[0]['card_group']
    # 第一个内容页面， 第一条记录不需要获取，是特殊的类似
    #   {
    # 		'mod_type': 'mod/clientTopTips',
    # 		'scheme': 'https://weibo.cn/appurl?scheme=sinaweibo%3A%2F%2Fsearchall%3Fq%3D%E5%89%8D%E4%B8%A4%E8%83%8E%E5%9D%87%E5%A4%AD%E6%8A%98%26luicode%3D20000174%26lfid%3Dhotword%26featurecode%3D20000320&luicode=20000174&lfid=hotword&featurecode=20000320',
    # 		'text': '前两胎均夭折'
    # 	}
    if is_first:
        screen_names = [card['mblog']['user']['screen_name'] for card in card_group[1:]]
    else:
        screen_names = [card['mblog']['user']['screen_name'] for card in card_group]

    return next_cursor, screen_names


def get_num_blog(s, num=0):
    # 得到需要访问的页码数
    if num == 0:
        page_num = 1
    else:
        # 向上取整
        page_num = math.ceil(num / 20)

    # 下一页的关键key
    next_cursor = ''
    # 所有的标题的列表
    all_screen_names = []

    # 根据页面进行循环
    for i in range(page_num):
        # 当访问第一页内容时， url 是特定的
        if i == 0:
            url = 'https://m.weibo.cn/feed/friends?version=v4'
            is_first = True
        # 当访问后续的内容时， url 变化，变化的key是 next_cursor， 从上一个页码的response返回的json中获取
        else:
            url = 'https://m.weibo.cn/feed/friends?version=v4&page=1&next_cursor=' + str(next_cursor)
            is_first = False

        # 根据拼接好的url， 进行访问对应的页面，获取博文信息
        next_cursor, screen_names = visit_friends_by_url(s, url, is_first)

        # 将获取到的页面的博文标题添加到 all_screen_names 列表中
        all_screen_names.extend(screen_names)

    # 截取需要的条数
    return all_screen_names[:num]


def visit_msg_index(s):
    url = 'https://m.weibo.cn/msg/index?format=cards'
    r = s.get(url)
    json_data = r.json()
    return json_data[0]['card_group']


def send_msg_by_uid(s, uid, st, msg):
    url = 'https://m.weibo.cn/msgDeal/sendMsg?'
    data = {
        'fileId': 'null',
        'uid': uid,
        'content': msg,
        'st': st
    }
    s.headers['Referer'] = 'https://m.weibo.cn/msg/chat?uid=' + str(uid)
    r = s.post(url, data=data)

    json_data = r.json()
    if json_data['ok'] == 1:
        print('私信发送成功')
    else:
        print('私信发送失败')


def visit_msg_chat(s, uid):
    url = 'https://m.weibo.cn/msg/chat?uid=' + str(uid)
    r = s.get(url)


if __name__ == '__main__':
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.proxies = {'https': '127.0.0.1:8888'}
    s.headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    visit_start(s)

    user = '51508690@qq.com'
    pwd = 'mumu2018'
    visit_login(s, user, pwd)

    st = visit_index(s)

    # visit_friends(s)

    screen_names = get_num_blog(s, 50)
    print(len(screen_names))
    print(screen_names)

    msg_group = visit_msg_index(s)

    msg = '测试发送数据1'
    for group in msg_group:
        if group.get('user') and group['user']['screen_name'] == '新浪新闻':
            uid = group['user']['id']
            visit_msg_chat(s, uid)
            send_msg_by_uid(s, uid, st, msg)

