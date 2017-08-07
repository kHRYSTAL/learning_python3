#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: sqlacchemy_foreignkey.py
# @time: 17/8/4 下午4:21
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy_basic import User, Address

engine = sqlalchemy.create_engine("mysql+pymysql://root:yyg1990918@localhost/awesome",
                                  encoding='utf-8', echo=True)

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
# 插入一条数据 用于连表查询

# region 插入数据
# address_obj = Address(email_address="723526676@qq.com", user_id=1)  # 生成你要创建的数据对象
#
# Session.add(address_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.commit()  # 现此才统一提交，创建数据

# endregion

# 连表查询
ret = Session.query(User, Address).filter(User.id == Address.user_id).all()
print(ret)

ret = Session.query(User).join(Address).all()  # 这种写法必须要求两个表之间有外键关联
print(ret)
