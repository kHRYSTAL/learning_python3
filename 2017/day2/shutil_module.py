#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: shutil 模块测试
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: shutil_module.py
# @time: 17/6/2 下午4:31

import shutil

f1 = open('README.md', encoding='utf8')
f2 = open('README_temp.md', 'w', encoding='utf8')

# 拷贝文件
# shutil.copyfileobj(f1, f2)
f1.close()
f2.close()


# 拷贝文件和权限
# shutil.copy('README.md', 'README_temp_copy.md')

# 拷贝文件和状态信息
# shutil.copy2('README.md', 'README_temp.md')

# shutil.copytree('原目录', '新路径')

# 删除目录
# shutil.rmtree()

# 仅拷贝文件的权限
# shutil.copymode('README.md', 'README_temp.md')

# 拷贝文件的状态信息
# shutil.copystat('README.md', 'README_temp.md')


shutil.make_archive('arch_name', 'zip', r'/Users/kHRYSTAL/PycharmProjects/learning_python3/2017/day2')

