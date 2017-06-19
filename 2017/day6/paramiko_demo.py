#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: paramiko_demo.py
# @time: 17/6/18 下午11:30


import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不再know_host的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器 不安全的 因为是明文的
ssh.connect(hostname='c1.salt.com', port=22, username='khrystal', password='123')

# 执行命令
# 标准输入 标准输出, 标准错误 standard
stdin, stdout, stderr = ssh.exec_command('df')

# 获取命令结果 为bytes类型
res, err = stdout.read(), stderr.read()
result = res if res else err
"""
三元运算符 如果res不为空 输出res 否则输出err
不能协程 stdout.read() if stdout.read() else stderr.read()
这样会导致 stdout读两遍 输出给result的值为第二次为空的
"""

print(result.decode())

ssh.close()
