#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: main.py
# @time: 17/5/31 上午12:11

from core import logger
from core import auth
from core import accounts
from core import transaction
from core.auth import login_required
import time

# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')

# temp account data, only saves the data in memory
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(user_data):
    print(user_data)


def transfer(user_data):
    pass


def pay_check(user_data):
    pass


def logout(user_data):
    pass


def withdraw(user_data):
    """
    print current balance and let user do the withdraw action
    :param user_data:
    :return:
    """
    account_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


@login_required
def repay(user_data):
    """
    print current balance and let user repay the bill
    :return:
    """
    account_data = accounts.load_current_balance(user_data['account_id'])
    # for k,v in account_data.items():
    #    print(k,v )
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

        if repay_amount == 'b':
            back_flag = True


def interactive(user_data):
    """
    interact with user
    :param user_data:
    :return:
    """
    menu = u'''
        ------- Oldboy Bank ---------
        \033[32;1m1.  账户信息
        2.  还款(功能已实现)
        3.  取款(功能已实现)
        4.  转账
        5.  账单
        6.  退出
        \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            print('accdata', user_data)
            # acc_data['is_authenticated'] = False
            menu_dic[user_option](user_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    """
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    """
    # 该方法会给user_data赋值
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        # 如果通过认证 将从json文件获取的用户数据赋给account_data
        user_data['account_data'] = acc_data
        interactive(user_data)
