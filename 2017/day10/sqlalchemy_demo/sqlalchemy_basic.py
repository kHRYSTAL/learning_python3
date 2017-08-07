#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: sqlalchemy orm框架的基本使用
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: sqlalchemy_basic.py
# @time: 17/8/4 下午1:44

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import func

# 创建数据库引擎
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine("mysql+pymysql://root:yyg1990918@localhost/awesome",
                                  encoding='utf-8', echo=True)

# region 创建表
Base = declarative_base()  # 生成orm 基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name: %s>" % (self.id, self.name)


#
#
# # 向数据库中创建user表
# Base.metadata.create_all(engine)

""" 实际上数据库中会执行:
CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(32),
    password VARCHAR(64),
    PRIMARY KEY (id)
)

事实上，我们用这种方式创建的表就是基于pymysql创建方式的再封装。
"""
# endregion

# region 插入数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例


# user_obj = User(name="khrystal", password="123456")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
#
# Session.commit()  # 现此才统一提交，创建数据
# endregion

# region 查询数据
# query_user = Session.query(User).filter_by(name='khrtstal').first()
# filter_by查询的是一个列表, 且只能设置等于号 需要在尾部指明查询限制 这里是查询第一条, 还可以查询.all() 返回查询结果的列表
# filter可以设置大于小于号 等于号需要写成双等号
# query_user = Session.query(User).filter(User.id > 2).all()
# query_user = Session.query(User).filter_by(User.name == 'khrystal').first()
# 多个条件查询 可以使用多个filter()
# query_user = Session.query(User).filter(User.id > 2).filter(User.id < 4).all()
# print(query_user)
# 模糊匹配
# query_user = Session.query(User).filter_by(User.name.like("kh%")).first()

# 查询不需要commit
# endregion

# region 修改数据
# session 相当于事务
# query_user = Session.query(User).filter_by(name='khrystal').first()
# print(query_user)
# query_user.name = 'Matt'
# query_user.password = '123456'
# Session.commit()
# endregion

# region 回滚操作
# 在Session.commit()之前 修改的数据都存在于内存中 所有写操作都可以回滚 但是id不会回滚
# my_user = Session.query(User).filter_by(id=1).first()
# my_user.name = "Jack"
#
# fake_user = User(name='Rain', password='12345')
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有刚添加和修改的数据
#
# Session.rollback()  # 此时rollback一下
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# Session
# Session.commit()
# endregion

# 统计操作
# count = Session.query(User).all().count()

# 分组操作
# print(Session.query(func.count(User.name), User.name).group_by(User.name).all())


# 创建地址表 用于外键关联
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", backref="addresses")  # 关联两个对象, 并不熟数据库真实存在的, 而是orm操作存储在内存中的
    # 相当于 user = Session.query(User).filter(Address.user_id == User.id).first()
    # 这句话的意思是, 可以通过user字段获取表User关联的数据, User表可以通过addresses字段获取Address表的数据

    def __repr__(self):
        return "<Address(email_address='%s', UserName= '%s')>" % (self.email_address, self.user.name)

# Base.metadata.create_all(engine)
