#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
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
                    print('##########host_groups:', group_objs)
                    bindhost_obj.host_groups = group_objs
                # for user_profiles this host binds to
                if source[key].get('user_profiles'):
                    userprofile_objs = session.query(models_v2.UserProfile).filter(models_v2.UserProfile.username.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs # 断言
                    print("userprofiles:", userprofile_objs)
                    bindhost_obj.user_profiles = userprofile_objs
                    # print(bindhost_obj)
        session.commit()
