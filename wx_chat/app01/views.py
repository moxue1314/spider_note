import json

from django.http import HttpResponse
from django.shortcuts import render
import time
import requests
import re
# Create your views here.
CTIME=None
TIP=1
ALL_COOKIE_DICT={}
TICKET_DICT={}
def login(request):
    '''
    获取二维码，并在自己网站上显示
    :param request:
    :return:
    '''
    global CTIME
    CTIME=time.time()
    response=requests.get(
        url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&lang=zh_CN&_=%s' % CTIME
    )
    v=re.findall('uuid = "(.*)";',response.text)
    global QCODE
    QCODE=v[0]
    return render(request,'login.html',{'qrcode':QCODE})


def check_login(request):
    '''
    监听用户是否已经扫码
    监听用户是否已经点击确定
    :param request:
    :return:
    '''
    global TIP
    ret = {'code':408,'data':None}
    r1 = requests.get(
        url='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=%s&r=205412088&_=%s' %(QCODE,TIP,CTIME)
    )
    if 'window.code=408' in r1.text:
        print('无人扫码')
        return HttpResponse(json.dumps(ret))
    elif 'window.code=201' in r1.text:
        ret['code']=201
        avatar = re.findall("window.userAvatar = '(.*)';", r1.text)[0]
        ret['data']=avatar
        TIP=0
        return HttpResponse(json.dumps(ret))
    elif 'window.code=200' in r1.text:
        # 用户点击确认登录，
        """
        window.code=200;
        window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AYKeKS9YQnNcteZCfLeTlzv7@qrticket_0&uuid=QZA2_kDzdw==&lang=zh_CN&scan=1494553432";
        window.redirect_uri="https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AYKeKS9YQnNcteZCfLeTlzv7@qrticket_0&uuid=QZA2_kDzdw==&lang=zh_CN&scan=1494553432";
        """
        ALL_COOKIE_DICT.update(r1.cookies.get_dict())
        redirect_uri=re.findall('window.redirect_uri="(.*)";',r1.text)[0]
        redirect_uri=redirect_uri+'&fun=new&version=v2'

        #获取凭证
        r2=requests.get(url=redirect_uri)
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(r2.text,'html.parser')
        for tag in soup.find('error').children:
            TICKET_DICT[tag.name]=tag.get_text()
        ALL_COOKIE_DICT.update(r2.cookies.get_dict())
        ret['code']=200
        print(ret)
        print('123')
        return HttpResponse(json.dumps(ret))


