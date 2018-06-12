#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
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

driver.get('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

print('打开首页成功')

time.sleep(3)

# 根据 xpath 查找对象
ele_username = driver.find_element_by_xpath('//input[@id="loginName"]')
# 根据css选择器查找
# ele_username1 = driver.find_element_by_css_selector('#loginName')
# 根据 id 查找
# ele_username2 = driver.find_element_by_id('loginName')
# 根据 a 标签的 文本内容进行查找
# driver.find_element_by_link_text('a标签中的文本内容')
# 使用 By
# ele_username3 = driver.find_element(By.XPATH, '//input[@id="loginName"]')

ele_username.clear()
ele_username.send_keys('51508690@qq.com')

ele_pwd = driver.find_element_by_id('loginPassword')
ele_pwd.clear()
ele_pwd.send_keys('mumu2018')

ele_login = driver.find_element_by_id('loginAction')
ele_login.click()

# 20 秒是最长等待时间，  0.5 秒是间隔轮询时间
# 等待 xpath 查找的元素目标加载完成
WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//a[@data-text="消息"]')))

time.sleep(1)

ele_msg = driver.find_element_by_xpath('//a[@data-text="消息"]')
ele_msg.click()

WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/msg/chat?uid=2028810631"]')))

ele_sina_new = driver.find_element_by_xpath('//a[@href="/msg/chat?uid=2028810631"]')
ele_sina_new.click()

WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'J-textarea')))
time.sleep(1)

ele_msg_textarea = driver.find_element_by_class_name('J-textarea')
ele_msg_textarea.clear()
ele_msg_textarea.send_keys('你好，新浪!')

time.sleep(2)

ele_send = driver.find_element_by_class_name('action-write-msg')
ele_send.click()
