#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = 'Terry'


import execjs
"""
    不需要理解js算法，直接在python中调用
"""
js = '''
function createGuid() {
	return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
}

function get(){
    var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
    return guid;
}
'''
ctx = execjs.compile(js)
b = ctx.call('get')
print(b)


"""
    使用python实现js的算法
"""
def  createGuid():
    return hex(int((1 + random.random()) * 0x10000)).replace('0x', '')[1:]

def get():
    return createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid()

print(get())