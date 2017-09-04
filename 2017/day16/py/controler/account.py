#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: account.py
# @time: 17/9/4 下午2:49


def handle_index():
    from model import model
    f = open('view/index.html', mode='rb')
    data = f.read()
    v = model.selectInDatabase()  # 从model层查询数据库
    data = data.replace(bytes('@replace', encoding='utf-8'), bytes(v, encoding='utf-8'))
    f.close()
    return [data, ]


def handle_date():
    pass


if __name__ == '__main__':
    pass
