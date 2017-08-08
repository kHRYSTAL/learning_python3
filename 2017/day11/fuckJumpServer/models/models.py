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
from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# 声明基类
Base = declarative_base()
