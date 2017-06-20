#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用RSA 加密免验证 需要公钥和私钥
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: ssh_rsa.py
# @time: 17/6/19 下午12:41

import paramiko

# 需要将公钥拷贝到需要连接的机器 与当前机器的私钥进行配对
# 这个路径可以是一个其他路径下的文件 只要文件中保存的是私钥就可以
private_key = paramiko.RSAKey.from_private_key_file('/Users/khrystal/.ssh/id_rsa')

# 创建SSH 对象
ssh = paramiko.SSHClient()

# 允许连接不在know_host文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器 最后一个参数为私钥连接对象
ssh.connect(hostname='c1.salt.com', port=22, username='khrystal', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')

res, err = stdout.read(), stderr.read()

result = res if res else err

print(result.decode('utf-8'))

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')

res, err = stdout.read(), stderr.read()

result = res if res else err

print(result.decode('utf-8'))

ssh.close()


