#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: utils.py
# @time: 17/8/9 下午2:45
import yaml
# 官方要求导入
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_err(msg, quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(yml_filename):
    """ yaml文件解析 """
    # yml_filename = "%s/%s.yml" % (settings.StateFileBaseDir,yml_filename)
    try:
        yaml_file = open(yml_filename, 'r')
        data = yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)
