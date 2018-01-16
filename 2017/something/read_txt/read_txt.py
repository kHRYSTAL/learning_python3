#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: read_txt.py
# @time: 17/8/3 下午11:12

dns_list = []
ip_list = []
response_list = []

with open('dns2018-01-15.log', 'r', encoding='utf8') as f:
    for line in f:
        dns_list.append(line.split()[0])

# print(dns_list)

with open('iplist.txt', 'r', encoding='utf8') as f:
    for line in f:
        ip_list.append(line.replace('\n', ''))

# print(ip_list)

for dns in dns_list:
    for ip in ip_list:
        if ip == dns:
            response_list.append(ip)

print(response_list)




