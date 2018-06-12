#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import parse_qsl

__author__ = 'Terry'


def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
        "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t') if len(s.strip().split('\t'))>1 else [s.strip(), '']) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.1' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[-1] and ':' in headers_raw_l[0]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)

def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")

def print_url_params_new(url_params):
    l = parse_qsl(url_params.strip(), 1)
    print("{\n    " + "',\n    ".join(map(lambda s: "'"+s[0]+"': '"+s[1], l)) + "',\n}")

if __name__ == '__main__':
    text_fiddler = '''
fileId	null
uid	2028810631
content	3333
st	acc368
    '''

    print_dict_from_copy_headers(text_fiddler)


    url_params = 'tpl=mn&apiver=v3&tt=1522120193242&class=login&gid=047897E-B6A8-4FD1-841B-23C1952428DB&loginversion=v4&logintype=dialogLogin&traceid=&callback=bd__cbs__ma4ta7'
    # print_url_params_new(url_params)