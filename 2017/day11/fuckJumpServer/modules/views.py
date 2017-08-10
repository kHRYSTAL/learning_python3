#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: todo 命令行功能实现 审计记录表未创建
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: views.py
# @time: 17/8/9 下午2:36
from models import models_v2
from modules.db_conn import engine, session
from modules.utils import print_err, yaml_parser


def auth():
    """ start session中用户认证操作 """
    count = 0
    while count < 3:
        username = input("\033[32;1mUsername:\033[0m").strip()
        if len(username) == 0:
            continue
        password = input("\033[32;1mPassword:\033[0m").strip()
        if len(password) == 0:
            continue
        user_obj = session.query(models_v2.UserProfile).filter(models_v2.UserProfile.username == username,
                                                               models_v2.UserProfile.password == password).first()
        if user_obj:
            return user_obj
        else:
            print("wrong username or password, you have %s more chances." % (3 - count - 1))
            count += 1
    else:
        print_err("too many attempts.")


def welcome_msg(user):
    WELCOME_MSG = '''\033[32;1m
    ------------- Welcome [%s] login fuckJumpServer-------------
    \033[0m''' % user.username
    print(WELCOME_MSG)


def start_session(argvs):
    """ 执行登录操作 """
    print('going to start sesssion ')
    user = auth()  # 用户认证
    if user:
        welcome_msg(user)
        print(user.bind_host)
        print(user.host_groups)
        exit_flag = False
        while not exit_flag:
            if user.bind_host:
                print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' % len(user.bind_host))  # 显示堡垒机用户直接关联的主机个数
            for index, group in enumerate(user.host_groups):
                print('\033[32;1m%s.\t%s (%s)\033[0m' % (index, group.name, len(group.bind_hosts)))  # 显示堡垒机用户关联的组

            choice = input("[%s]:" % user.username).strip()
            if len(choice) == 0:
                continue
            if choice == 'z':  # 如果输入z 则显示直接关联主机列表
                print("------ Group: ungroupped hosts ------")
                for index, bind_host in enumerate(user.bind_host):
                    print("  %s.\t%s@%s(%s)" % (index,
                                                bind_host.remote_user.username,
                                                bind_host.host.hostname,
                                                bind_host.host.ip,
                                                ))
                print("----------- END -----------")
            elif choice.isdigit():  # 如果是整数, 显示对应顺序的主机组中的主机列表
                choice = int(choice)
                if choice < len(user.host_groups):
                    print("------ Group: %s ------" % user.host_groups[choice].name)
                    for index, bind_host in enumerate(user.host_groups[choice].bind_hosts):
                        print("  %s.\t%s@%s(%s)" % (index,
                                                    bind_host.remote_user.username,
                                                    bind_host.host.hostname,
                                                    bind_host.host.ip,
                                                    ))
                    print("----------- END -----------")
                    # todo 连接远程主机 使用demo的paramiko 并记录数据库即可!
                    # # host selection
                    # while not exit_flag:
                    #     user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                    #     if len(user_option) == 0: continue
                    #     if user_option == 'b': break
                    #     if user_option == 'q':
                    #         exit_flag = True
                    #     if user_option.isdigit():
                    #         user_option = int(user_option)
                    #         if user_option < len(user.groups[choice].bind_hosts):
                    #             print('host:', user.groups[choice].bind_hosts[user_option])
                    #             print('audit log:', user.groups[choice].bind_hosts[user_option].audit_logs)
                    #             ssh_login.ssh_login(user,
                    #                                 user.groups[choice].bind_hosts[user_option],
                    #                                 session,
                    #                                 log_recording)
                else:
                    print("no this option..")


def syncdb(argvs):
    """ 创建所有表 """
    print("Syncing DB....")
    models_v2.Base.metadata.create_all(engine)  # 创建所有表结构


def create_users(argvs):
    """根据yml文件创建堡垒机user表中的数据"""
    if '-f' in argvs:
        user_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>", quit=True)

    source = yaml_parser(user_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = models_v2.UserProfile(username=key, password=val.get('password'))
            # if val.get('groups'):
            #     groups = session.query(models_v2.Group).filter(models_v2.Group.name.in_(val.get('groups'))).all()
            #     if not groups:
            #         print_err("none of [%s] exist in group table." % val.get('groups'), quit=True)
            #     obj.groups = groups
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            # # print(obj)
            session.add(obj)
        session.commit()


def create_hosts(argvs):
    """根据yml文件创建host表中的数据"""
    if '-f' in argvs:
        hosts_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>", quit=True)
    source = yaml_parser(hosts_file)  # 解析yml文件为对象
    if source:
        # print(source)
        for key, val in source.items():
            print(key, val)
            obj = models_v2.Host(hostname=key, ip=val.get('ip'), port=val.get('port') or 22)  # 创建一行host数据
            session.add(obj)
        session.commit()


def create_remoteusers(argvs):
    """根据yml文件创建remote_user表中的数据"""
    if '-f' in argvs:
        remoteusers_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>", quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = models_v2.RemoteUser(username=val.get('username'), auth_type=val.get('auth_type'),
                                       password=val.get('password'))
            session.add(obj)
        session.commit()


def create_groups(argvs):
    """根据yml文件创建Group表中的数据"""
    if '-f' in argvs:
        group_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>", quit=True)
    source = yaml_parser(group_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = models_v2.HostGroup(name=key)
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            #
            # if val.get('user_profiles'):
            #     user_profiles = common_filters.user_profiles_filter(val)
            #     obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()


def create_bindhosts(argvs):
    """根据yml文件创建BindHost表中的数据"""
    if '-f' in argvs:
        bindhosts_file = argvs[argvs.index("-f") + 1]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>", quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key, val in source.items():
            # print(key,val)
            host_obj = session.query(models_v2.Host).filter(models_v2.Host.hostname == val.get('hostname')).first()
            assert host_obj  # 断言是否存在这个主机, 如果没有抛出异常不向下执行
            for item in val['remote_users']:
                print(item)
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-passwd':
                    remoteuser_obj = session.query(models_v2.RemoteUser).filter(
                        models_v2.RemoteUser.username == item.get('username'),
                        models_v2.RemoteUser.password == item.get('password')
                    ).first()
                else:
                    remoteuser_obj = session.query(models_v2.RemoteUser).filter(
                        models_v2.RemoteUser.username == item.get('username'),
                        models_v2.RemoteUser.auth_type == item.get('auth_type'),
                    ).first()
                if not remoteuser_obj:  # 如果RemoteUser表不存在bindhost.yml文件中的remoteUser, 抛出异常
                    print_err("RemoteUser obj %s does not exist." % item, quit=True)
                bindhost_obj = models_v2.BindHost(host_id=host_obj.id, remoteuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)
                # for groups this host binds to
                if source[key].get('groups'):
                    # select * from HostGroup where name in (bjgroup, shgroup);
                    group_objs = session.query(models_v2.HostGroup).filter(
                        models_v2.HostGroup.name.in_(source[key].get('groups'))).all()
                    assert group_objs  # 断言
                    bindhost_obj.host_groups = group_objs
                # for user_profiles this host binds to
                if source[key].get('user_profiles'):
                    userprofile_objs = session.query(models_v2.UserProfile).filter(models_v2.UserProfile.username.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs  # 断言
                    print("userprofiles:", userprofile_objs)
                    bindhost_obj.user_profiles = userprofile_objs
                    # print(bindhost_obj)
        session.commit()
