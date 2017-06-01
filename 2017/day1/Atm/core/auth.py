#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: auth.py
# @time: 17/5/31 下午6:46
import time
from core import db_handler


# decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            exit('User is not authenticated.')
    return wrapper


def acc_auth2(account, password):
    """
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication, return the account object, otherwise, return None
    """
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)
    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_data'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else:  # passed the authentication
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data, log_obj):
    """
    account login func
    :param user_data: user info data, only saves in memory
    :param log_obj:
    :return:
    """
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(account, password)
        if auth:  # not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            # print('welcome')
            return auth
        retry_count += 1
    else:
        log_obj.error('account [%s] too many login attempts' % account)
        exit()


if __name__ == '__main__':
    pass
