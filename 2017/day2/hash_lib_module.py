#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: hashlib 模块
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: hash_lib_module.py
# @time: 17/6/5 下午2:14
"""
用于加密相关操作 3.x 里代替了md5和sha模块 主要提供SHA1 SHA224 SHA256 SHA384 SHA512 MD5算法
"""

import hashlib

m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())
m.update(b'It\'s me')
print(m.hexdigest())
# m.update(b'It\'s been a long time since we spoken')
# print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'HelloIt\'s me')
print(m2.hexdigest())

s = hashlib.sha1()
s.update(b'HelloIt\'s me')
print(s.hexdigest())

# 中文md5 需要encode
m3 = hashlib.md5()
m3.update('天王盖地虎'.encode(encoding='utf-8'))
print(m3.hexdigest())
print("\n===========================\n")

"""
hmac 内部创建 key 和 内容(value) 再进行处理然后再加密
"""

import hmac

h = hmac.new(b'Hello')  # key 必须为byte
h.update('天王盖地虎'.encode('utf-8'))  # 加密内容
print(h.digest())
print(h.hexdigest())
