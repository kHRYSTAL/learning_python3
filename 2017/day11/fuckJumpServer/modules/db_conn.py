#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: db_conn.py
# @time: 17/8/9 下午6:38

from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from conf import settings

engine = create_engine(settings.ConnParams, echo=True)
SessionCls = sessionmaker(bind=engine)

session = SessionCls()
