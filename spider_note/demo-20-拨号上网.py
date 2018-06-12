#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import subprocess

import time
import win32ras

from a6.common.control_helper import call_until_success, RetryException, RetryOvertimesException

__author__ = 'Terry'

'''
    拨号
'''
def wait_connect_proc_exit(proc):
    errCode = proc.poll()
    if errCode is not None:
        return errCode
    else:
        raise RetryException()

bohao_count = 0

def re_connect(rasEntryName, user, pwd):
    global bohao_count
    bohao_count += 1
    path = os.getenv("WINDIR")
    if not path:
        raise ConnectionError
    path = path + "\\system32"
    if not os.path.exists(path + "\\rasdial.exe"):
        raise ConnectionError
    cmd = '%s\\cmd /c  %s\\rasdial "%s" /disconnect  &&  %s\\rasdial "%s" %s %s' % (path, path, rasEntryName, path, rasEntryName, user, pwd)
    # cmd = 'cmd /c  rasdial "%s" /disconnect  &&  rasdial "%s" %s %s' % (rasEntryName, rasEntryName, user, pwd)
    proc = subprocess.Popen(cmd, shell=True)
    try:
        errCode = wait_connect_proc_exit(proc)
    except RetryOvertimesException:
        raise ConnectionError()
    proc.terminate()
    if errCode:
        errinfo = win32ras.GetErrorString(errCode)
        if errCode in [651, 678, 691, 628]:
            time.sleep(30)
            print("reconnect error %s[%s], sleep 30 sec and retry" % (errinfo, errCode))
            raise RetryException()
        elif errCode in [718, 720]:
            time.sleep(1)
            print("reconnect error1 %s[%s], sleep 1 sec and retry" % (errinfo, errCode))
            raise RetryException()
        elif errCode in [692]:
            time.sleep(5)
            print("reconnect error2 %s[%s], sleep 5 sec and retry" % (errinfo, errCode))
            raise RetryException()
        elif errCode in [623]:
            print("reconnect error3 %s[%s], stop" % (errinfo, errCode))
            raise Exception()
        else:
            print("reconnect not handle error %s[%s], 30 sec wait" % (errinfo, errCode))
            time.sleep(30)
            raise RetryException()
    print("re_connect ok %s" % bohao_count)

    return True

if __name__ == '__main__':
    re_connect('test_bh', '用户名', '密码')
