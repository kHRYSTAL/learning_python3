#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: zip_module.py
# @time: 17/6/2 下午5:15

import zipfile

# 压缩
z = zipfile.ZipFile('zip_file_name', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('zip_file_name', 'r')
z.extractall() # 可设置解压地址
z.close()

if __name__ == '__main__':
    pass