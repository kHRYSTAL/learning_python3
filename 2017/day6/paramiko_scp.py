#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用paramiko实现scp功能
# scp是基于ssh的ftp功能
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: paramiko_scp.py
# @time: 17/6/18 下午11:37

import paramiko

"""
建立一个传输通道 这里的connect为一个实例
"""
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='khrystal', password='123')

# 传输操作在client里定义
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/README.md', '/tmp/README_CN.md')

sftp.get('remove_path', 'local_path')

transport.close()

