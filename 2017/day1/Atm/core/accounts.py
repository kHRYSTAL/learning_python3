#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: accounts.py
# @time: 17/5/31 下午3:04
import json
import time
from core import db_handler
from conf import settings


def load_current_balance(account_id):
    """
    :return account balance and other basic info
    :param account_id:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("select * from account where account=%s" % account_id)
    return data


def dump_account(account_data):
    """
    after updated transaction or account data, dump it to file db
    :param account_data:
    :return:
    """
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'], account_data=account_data)
    return True

if __name__ == '__main__':
    pass
