#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: db_handler.py
# @time: 17/5/31 下午3:06

import json, time, os
from conf import settings


def file_db_handler(conn_params):
    """
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    """
    print('file db:', conn_params)
    return file_execute


def db_handler():
    """
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:
    """
    conn_params = settings.DATABASE
    if conn_params['engins'] == 'file_storage':
        return file_db_handler(conn_params)


def file_execute(sql, **kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])
    print(sql, db_path)
    sql_list = sql.split('where')
    print(sql_list)  # e.g. select * from table where account = 1234
    if sql_list[0].startswith('select') and len(sql_list) > 1:  # has where cause
        column, val = sql_list[1].strip().split('=')
        if column == 'account':
            account_file = '%s/%s.json' % (db_path, val)  # path/1234.json
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val)
    elif sql_list[0].startswith('update') and len(sql_list) > 1: # has where cause
        column, val = sql_list[1].strip().split('=')
        if column == 'account':
            account_file = '%s/%s.json' % (db_path, val)
            if os.path.isfile(account_file):
                account_data = kwargs.get('account_data')
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                return True
