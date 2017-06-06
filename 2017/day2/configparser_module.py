#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: configparser_module.py
# @time: 17/6/5 下午1:49

# 2.7 ConfigParser
import configparser
"""
写
"""
# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'ServerAliveInterval': '45',
#     'Compression': 'yes',
#     'CompressionLevel': 9,
#     'ForwardX11': 'yes',
# }
#
# config['bitbucket.org'] = {
#     'User': 'hg',
# }
#
# config['topsecret.server.com'] = {
#     'port': '50022',
#     'ForwardX11': 'no',
# }
#
# with open('configparser_test.ini', 'w') as configfile:
#     config.write(configfile)

"""
读
"""
config = configparser.ConfigParser()
config.read('configparser_test.ini')

print(config.defaults())
print(config.sections())
# print(config['bitbucket.org']['user'])


"""
删除节点
"""

config.remove_section('bitbucket.org')
config.write(open('configparser_test.ini', 'w'))

"""
新增节点
"""

config['bitbucket.org'] = {
    'User': 'hg',
}

with open('configparser_test.ini', 'w') as f:
    config.write(f)
