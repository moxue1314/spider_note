#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random

import time
from lxml import etree

import requests
from requests.cookies import RequestsCookieJar

__author__ = 'Jiexun Li'

from selenium import webdriver

# 作业：
# 1. 用 selenium 登录百度，获取cookie，保存cookie
# 2. 用 requests 读取cookie,登录百度页面
# 3. 访问 百度指数，访问关键字

# ------------------------------登录百度 保存cookie------------------------------------------------------
# 火狐
# driver = webdriver.Firefox()
#
# # 设置窗口大小
# driver.set_window_size(1366, 768)
# # 页面的加载超时时间
# driver.set_page_load_timeout(10)
# # script脚本的超时时间
# driver.set_script_timeout(10)
#
# driver.get('https://www.baidu.com/')
#
# time.sleep(2)
#
# ele_login_ui = driver.find_element_by_xpath('//div[@id="u1"]/a[@name="tj_login"]')
# # driver.execute_script("window.scrollTo(0, 0);") # 将滚动条移动到指定的位置
# ele_login_ui.click()
#
# # driver.get('https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5')
# time.sleep(2)
# ele_login_button = driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
# ele_login_button.click()
# time.sleep(2)
#
# ele_username = driver.find_element_by_id('TANGRAM__PSP_10__userName')
# ele_username.clear()
# # 用户名
# ele_username.send_keys('mumuloveshine')
# ele_pwd = driver.find_element_by_id('TANGRAM__PSP_10__password')
# ele_pwd.clear()
# # 密码
# ele_pwd.send_keys('mumu2018')
#
#
# # ****登陆前输入验证码***** 在此处需设置断点
#
#
# ele_login = driver.find_element_by_id('TANGRAM__PSP_10__submit')
# ele_login.click()
#
#
# cookies = driver.get_cookies()
#
# # 把需要获取cookie的域名进行访问，并且将多个域名的cookie进行合并保存
# driver.get('http://passport.baidu.com')
# cookies.extend(driver.get_cookies())
#
# file = 'baidu_cookies_update.txt'
# with open(file, 'w') as f:
#     json.dump(cookies, f)
# driver.quit()

# ----------------------------selenium访问百度指数-------------------------------------------------------
# driver.get('http://index.baidu.com/')
# print('aaa')
# time.sleep(2)
# search_box = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div/div[2]/form/input[3]')
# search_box.clear()
# search_box.send_keys('汽车排行')
# confirm_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span/span')
# confirm_button.click()
# driver.quit()


# # ------------------------------requests 读取cookie,登录百度页面--------------------------------------------
def load_cookie(s, file):
    with open(file, 'r') as f:
        cookies = json.load(f)
        jar = RequestsCookieJar()
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])
        s.cookies = jar


USER_AGENT_LIST =[
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
]

def make_session():
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.headers = {
        'User-Agent': random.choice(USER_AGENT_LIST),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    return s

if __name__ == '__main__':
    s = requests.session()
    s.trust_env = False
    s.verify = False
    s.headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    url = 'https://www.baidu.com/'

    # r = s.get(url)
    #
    # if '推荐' in r.text:
    #     print('登录成功')
    # else:
    #     print('未登录')

    file = 'baidu_cookies_update.txt'
    load_cookie(s, file)
    r = s.get(url)

    if '推荐' in r.text:
        print('登录成功')
    else:
        print('未登录')

    # ----------------------------request访问百度指数---------------------------------------------------
    url = 'http://index.baidu.com/'


    params = {
        'tpl':'trend',
        'word':'汽车排行',
    }

    s.headers['referer'] = 'http://index.baidu.com/'

    r = s.get(url, params=params)
    r.encoding='GBK'

    if '购买记录' in r.text:
        print('访问成功')
    print(r.text)



