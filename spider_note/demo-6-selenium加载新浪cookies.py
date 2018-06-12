#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time

from selenium.webdriver.common.by import By

__author__ = 'Terry'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# 火狐
driver = webdriver.Firefox()

# 设置窗口大小
driver.set_window_size(1366, 768)
# 页面的加载超时时间
driver.set_page_load_timeout(30)
# script脚本的超时时间
driver.set_script_timeout(30)

driver.get('https://m.weibo.cn/')

file = 'sina_cookies.txt'
with open(file, 'r') as f:
    # txt = f.read()
    # cookies = json.loads(txt)
    cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.get('https://m.weibo.cn/')

driver.quit()

