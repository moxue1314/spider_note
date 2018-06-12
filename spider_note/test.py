#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
def xmlchar_2_cn(s):
    def convert_callback(matches):
        char_id = matches.group(1)
        try:
            return chr(int(char_id))

        except:
            return char_id

    ret = re.sub("&#(\d+)(;|(?=\s))", convert_callback, s)

    return ret

print(xmlchar_2_cn('&#25105;&#26159;&#27004;&#20027;&#30340;&#20799;&#23376;'))
