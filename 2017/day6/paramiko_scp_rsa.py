#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: paramiko_scp_rsa.py
# @time: 17/6/19 下午12:58

import paramiko

"""
建立一个传输通道 这里的connect为一个实例
使用rsa无需密码连接
"""
private_key = paramiko.RSAKey.from_private_key_file('/User/khrystal/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='khrystal', pkey=private_key)

# 传输操作在client里定义
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/README.md', '/tmp/README_CN.md')

sftp.get('remove_path', 'local_path')

transport.close()