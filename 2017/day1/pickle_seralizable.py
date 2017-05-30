#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage:  pickle 用于处理序列化 可处理函数对象的序列化
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: pickle_seralizable.py
# @time: 17/5/30 上午1:32

import pickle


# func 函数块的内存地址运行完就被释放因此需要写到反序列化代码里(只保留函数名 没有函数块) 否则读不出来
def func(name):
    print('hello', name)


info = {
    'name': 'khrystal',
    'age': 22,
    'func': func
}

with open('pickle.txt', 'wb') as f:
    # f.write(pickle.dumps(info))
    pickle.dump(info, f)  # 两个语句意义相同

if __name__ == '__main__':
    pass
