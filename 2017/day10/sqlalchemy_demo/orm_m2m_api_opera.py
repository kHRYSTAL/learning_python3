#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: orm_m2m_api_opera.py
# @time: 17/8/7 下午3:53
import sqlalchemy
from sqlalchemy.orm import sessionmaker

import sqlalchemy_many_2_many as m2m

Session_class = sessionmaker(bind=m2m.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# 插入数据
# b1 = m2m.Book(name='learn python', pub_date='2017-08-07')
# b2 = m2m.Book(name='learn Django', pub_date='2014-08-07')
# b3 = m2m.Book(name='learn DDD', pub_date='2013-08-07')
#
# a1 = m2m.Author(name='kHRYSTAL')
# a2 = m2m.Author(name='Jack')
# a3 = m2m.Author(name='Matt')
#
# b1.authors = [a1, a3]  # 设置book关联数据 实际上这些关联关系会存储到作者与书的关系表中
# b3.authors = [a1, a2, a3]
#
# Session.add_all([b1, b2, b3, a1, a2, a3]) # 注意 添加顺序可能和列表顺序不同
#
# Session.commit()

# 查询数据
author_obj = Session.query(m2m.Author).filter(m2m.Author.name == 'kHRYSTAL').first()
# 反查获取作者的书
print(author_obj.books)

book_obj = Session.query(m2m.Book).filter(m2m.Book.name == 'learn python').first()
print(book_obj.name)
# 反查获取书的作者
print(book_obj.authors)


# 删除书中的一个作者 关联关系会自动删除
# book_obj.authors.remove(author_obj)
# Session.commit()
