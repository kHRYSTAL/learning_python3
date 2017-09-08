#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: grep_docker_ip.py
# @time: 17/9/7 下午4:54


import json

data = None

with open('/etc/info4docker', 'r') as f:
    data = f.read()

data = json.loads(data)

print(data['LOCAL_IP'])
