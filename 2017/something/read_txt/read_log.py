#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: read_log.py.py
# @time: 18/1/16 上午10:30
import re, json

log_list = []


class NginxLog(object):
    def load(self, *args):
        self.time = args[0]
        self.ip = args[1]
        self.ip_alias = args[2]
        self.curl_cmd = args[3]
        self.method = args[4]
        self.url = args[5]
        self.http_version = args[6]
        self.resp_code = args[7]
        self.resp_length = args[8]
        self.resp_cost_time = args[9]
        self.local_ip = args[10]
        self.local_code = args[11]
        self.local_cost_time = args[12]
        self.redirect_list = args[13]


class RedirectLog(object):
    def __init__(self, data_set):
        self.redirect_ip = data_set[0]
        self.redirect_code = data_set[1]


def match_normal_nginx_log(text):
    sp = re.split(r'\s+', text)
    for v in sp:
        if v == '\n' or v == '-' or v == '"-"' or v == '':
            sp.remove(v)
    return sp


with open('nginx_log', 'r', encoding='utf8') as f:
    for line in f:
        nginx_log = NginxLog()
        line_list = line.split(',')
        if len(line_list) > 2:
            # add redirect
            for redirect_text in line_list[-3: 0]:
                redirect = RedirectLog(redirect_text.split())
                nginx_log.redirect_list.append(redirect)
            new_line = line_list[0] + line_list[-2] + ',' + line_list[-1]
            nginx_log.load(*match_normal_nginx_log(new_line))
        else:
            new_line = line_list[0] + ',' + line_list[-1]
            match_normal_nginx_log(new_line)
            nginx_log.load(*match_normal_nginx_log(new_line))

        log_list.append(json.dumps(nginx_log.__dict__))


print(log_list)
