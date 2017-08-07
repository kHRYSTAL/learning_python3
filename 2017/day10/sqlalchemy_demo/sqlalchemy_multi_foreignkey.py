#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 单个表多外键关联, 外键对应的是另一个表的同一个字段的情况
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: sqlalchemy_multi_foreignkey.py
# @time: 17/8/7 下午2:24


from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    """
    消费表 包含外键账单地址id和收货地址id 两个id都是外键关联address表id
    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    billing_address_id = Column(Integer, ForeignKey("address.id"))  # 外键关联address表id
    shipping_address_id = Column(Integer, ForeignKey("address.id"))  # 外键关联address表id
    # 由于是多外键, address在反查customer时分不清使用的是哪个id, 因此需要指明通过哪个id反查
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[billing_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
