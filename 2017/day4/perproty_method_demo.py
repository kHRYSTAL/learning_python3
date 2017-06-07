#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 属性方法例子
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: perproty_method_demo.py
# @time: 17/6/7 下午5:39


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        """
        调取航空公司api
        """
        print('checking flight %s status' % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print('flight got canceled...')
        elif status == 1:
            print('flight is arrived...')
        elif status == 2:
            print('flight has departured already')
        else:
            print('cannot confirm the flight status..., please check later')

    @flight_status.setter
    def flight_status(self, status):
        status_dict = {
            0: 'canceled',
            1: 'arrived',
            2: 'departured',
        }
        print("\033[31;1m%s Has changed the flight status to %s\033[0m" % (self.flight_name, status_dict.get(status)))

    @flight_status.deleter
    def flight_status(self):
        print('status got romved...')


f = Flight('CA980')
f.flight_status

f.flight_status = 2

del f.flight_status
