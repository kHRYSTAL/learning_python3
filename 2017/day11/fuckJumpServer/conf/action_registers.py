#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: action_registers.py
# @time: 17/8/9 下午2:35
from modules import views

actions = {
    'start_session': views.start_session,
    # 'stop': views.stop_server,
    'syncdb': views.syncdb,
    'create_users': views.create_users,
    'create_groups': views.create_groups,
    'create_hosts': views.create_hosts,
    'create_bindhosts': views.create_bindhosts,
    'create_remoteusers': views.create_remoteusers,

}

if __name__ == '__main__':
    pass