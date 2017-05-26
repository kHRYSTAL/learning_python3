#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 正则表达式
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 01_regex.py
@time: 16/5/23 下午1:36
"""
import re
M=['someone@gmail.com','bill.gates@microsoft.com']

pattern='(\w+.)?\w+@\w+.com'
for email in range(len(M)):
    print(re.match(pattern,M[email]).group())


pattern='(<[A-Za-z]+\s*[A-Za-z]+>)\s?\w+@\w+\.(com|org)'

print(re.search(pattern,'<Tom Paris> tom@voyager.org').group(1))















def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass