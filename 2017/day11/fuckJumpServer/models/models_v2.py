#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 数据库表ORM对象
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: models.py
# @time: 17/8/8 下午7:03

import sqlalchemy
from sqlalchemy import Table, Enum, Column, Integer, String, DATE, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# 用于枚举字段声明
from sqlalchemy_utils import ChoiceType

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# 声明基类
Base = declarative_base()


# region 多对多关系表
# 远程主机与远程主机账户
# host_m2m_remoteuser = Table('host_m2m_remoteuser', Base.metadata,
#                             Column('host_id', Integer, ForeignKey('host.id')),
#                             Column('remoteuser_id', Integer, ForeignKey('remote_user.id')))

class BindHost(Base):
    """
    远程机器与远程用户与属组的关系
    远程机器可以包含多个远程用户
    保存关联关系, 2列需要联合唯一
    ip              remote_user
    192.168.1.11    web
    192.168.1.11    mysql
    """
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('host_id', 'group_id', 'remoteuser_id', name='_host_group_remoteuser_uc'),)
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    # group_id = Column(Integer, ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    # host能够通过bind_hosts反查当前类 再从当前类获取remote_user和group
    host = relationship('Host', backref='bind_hosts')
    # host_group = relationship('HostGroup', backref='bind_hosts')
    remote_user = relationship('RemoteUser', backref='bind_hosts')

    def __repr__(self):
        return '<%s -- %s -- %s>' % (self.host.ip, self.remote_user.username, self.host_group.name)


# 堡垒机账户与bindhost多对多关系表, 这样在堡垒机账户就能获取他自己的bindhost对象
# 通过bindhost就能获取到指定的远程账户 ip地址 只对应没有属组的host
user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                          Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                          Column('bindhost_id', Integer, ForeignKey('bind_host.id')))

# bindhost表与group表的多对多关系表 由于存在机器可能不属于组, 单个存在, 因此 要把bindhost中的group单独分割成一个关系表
bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup', Base.metadata,
                               Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                               Column('hostgroup_id', Integer, ForeignKey('host_group.id')))

# 堡垒机账户与属组多对多关系表 可以先获取属组 再通过属组获取bindhost
user_m2m_hostgroup = Table('user_m2m_hostgroup', Base.metadata,
                           Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                           Column('hostgroup_id', Integer, ForeignKey('host_group.id')))


# endregion

class Host(Base):
    """远程主机表"""
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)  # 主机名称其实可以不唯一
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    # 与多对多关系表关联 建立与RemoteUser类的关系 反查远程账户
    # remote_users = relationship('RemoteUser', secondary=host_m2m_remoteuser, backref='hosts')

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    """主机组表"""
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    # 反查绑定的主机, 主机可以反查属组列表
    bind_hosts = relationship('BindHost', secondary='bindhost_m2m_hostgroup', backref='host_groups')

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    """远程主机表中的账户"""
    __tablename__ = 'remote_user'
    # 联合唯一 , 即多个字段联合组成一个唯一值不允许重复 name表示联合唯一的键 value为字段的hash值
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password', name='_user_passwd_uc'),)
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(128))  # 这里可以优化加密, 目前按照明文存储
    AuthTypes = [
        ('ssh-passwd', 'SSH/Password'),  # 第一个是真正存到数据库的, 第二个是显示给用户看的
        ('ssh-key', 'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))

    def __repr__(self):
        return self.username


class UserProfile(Base):
    """堡垒机保存的账户 即连接堡垒机时登录的账号"""
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))

    # userprofile能够获取bindhost对象 bindhost能够通过user_profiles反查获取user_profile 只针对没有属组的主机
    bind_host = relationship('BindHost', secondary='user_m2m_bindhost', backref='user_profiles')
    # userprofile能够获取可操作主机的属组, 属组能够反查获取哪些user可以具有这个属组
    host_groups = relationship('HostGroup', secondary='user_m2m_hostgroup', backref='user_profiles')

    def __repr__(self):
        return self.username
