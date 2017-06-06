#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: docker_exec.py
# @time: 17/6/5 下午10:15

import re
import os

with open('docker.txt', 'r') as f:
    for line in f:
        if re.match('docker.*?', line):
            print('exec line', line)
            output = os.popen(line)
            print(output.read())




