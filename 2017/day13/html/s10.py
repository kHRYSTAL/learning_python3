#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: s10.py
# @time: 17/8/21 上午12:31

import requests

# 1首先登陆任何页面，获取cookie

i1 = requests.get(url="http://dig.chouti.com/help/service")

# 2用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "86手机号",
        'password': "密码",
        'oneMonth': ""
    },
    cookies=i1.cookies.get_dict()
)

# 3点赞（只需要携带已经被授权的gpsd即可）
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=8589523",
    cookies={'gpsd': gpsd}
)
print(i3.text)
