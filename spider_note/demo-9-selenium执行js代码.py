#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'


from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

driver.execute_script('alert("haha!");')

print('over')

driver.quit()