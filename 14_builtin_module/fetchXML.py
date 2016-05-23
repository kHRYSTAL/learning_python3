#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: fetch yahoo
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: fetchXML.py
@time: 16/5/24 上午6:59
"""

from urllib import request,parse
from collections import OrderedDict

def fetch_xml(url):
    Dict = OrderedDict()
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        Dict['Status'] = f.status+ " " + f.reason
        for k, v in f.getheaders():
            Dict[k] = v
        Dict['Data'] = f.read().decode('utf-8')



print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))



#urllib.error.HTTPError: HTTP Error 401: Unauthorized









def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass