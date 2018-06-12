#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 一、 selenium 设置cookie，只会得到当前域名，如果要获取多个子域名下的cookie，需要分别进行访问获取，并且进行合并
# 例如：
import json

from selenium import webdriver

# 火狐
driver = webdriver.Firefox()

driver.get('http://www.baidu.com')
cookies = driver.get_cookies()

# 把需要获取cookie的域名进行访问，并且将多个域名的cookie进行合并保存
driver.get('http://passport.baidu.com')
cookies.extend(driver.get_cookies())

# 应用时，最简单的就是讲 domain 设置为 顶级域名：
file = 'baidu_cookies_update.txt'
with open(file, 'r') as f:
    cookies = json.load(f)
    for cookie in cookies:
        cookie['domain'] = '.baidu.com'
        driver.add_cookie(cookie)