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
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USE_FILE = BASE_DIR + '/docker.txt'


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('cost time: %s' % (stop_time - start_time))

    return wrapper


def exec_docker():
    with open(USE_FILE, 'r') as f:
        for line in f:
            if re.match('docker.*?', line):
                dispatch_docker(line)


@timer
def dispatch_docker(command):
    print('exec line', command)
    output = os.popen(command)
    print(output.read())


exec_docker()
