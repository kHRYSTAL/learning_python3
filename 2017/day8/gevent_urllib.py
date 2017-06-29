#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: urllib_demo.py
# @time: 17/6/27 下午10:34

from urllib import request
import gevent
from gevent import monkey
import time

"""
经过log判断 实际还是串行的, urllib进行io操作时,
gevent 检测不到进行了io操作 因此不会遇到阻塞跳转,需要给urllib打monkey补丁
"""

# 把当前程序的所有io阻塞操作单独做上标记, 遇到阻塞就switch spawn包裹的函数
monkey.patch_all()

"""
在这里 相当于读取urllib内部的io操作做上标记
"""


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    # file = open('url.html', 'wb')
    # file.write(data)
    # file.close()
    print('%d bytes received from %s.' % (len(data), url))


# f('http://www.jianshu.com/p/ebac88cdf9d6')
# 串行爬取网页
urls = ['http://www.python.org',
        'http://www.jianshu.com/p/ebac88cdf9d6',
        'http://github.com']

start_time = time.time()
for url in urls:
    f(url)

print("串行", time.time() - start_time)  # 6秒


# 协程爬取网页
start_time = time.time()
# joinall的意思是批量执行并加入当前程序所在线程
gevent.joinall([
    gevent.spawn(f, 'http://www.python.org'),
    gevent.spawn(f, 'http://www.jianshu.com/p/ebac88cdf9d6'),
    gevent.spawn(f, 'http://github.com')
])
print("协程:", time.time() - start_time)  # 2秒
