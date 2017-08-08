#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 多对多关联
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: sqlalchemy_many_2_many.py
# @time: 17/8/7 下午3:32
"""
多对多关联
如每本书可以有多个作者
每个作者可以有多本书
这种情况下为了减少数据冗余 应建立三张表
作者表 书表 作者与书的关系表

第三张表用于主动关联前两张表
书表和作者表没有直接的关联关系
"""
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# 书与作者的关系表 这张表不应手动创建 因为我们不会去手动向这张表插入数据, 只需要在存储书的时候指明作者 或存储作者的时候指明书
# orm自己去维护这张表 谁都不用去关心 实际上这个表只是指明了book和author的关联关系 用于book反查user和user反查book
# 存储时会自动关联, 将id存储到这个表里
# 只是告诉orm去哪张表查数据
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id', Integer, ForeignKey('books.id')),
                        Column('author_id', Integer, ForeignKey('authors.id')),
                        )


# 书表
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    # 通过书与作者的关系表 在这张表里能查到authors, 在Author表能通过books查到Book表的数据
    # secondary 间接的
    authors = relationship('Author', secondary=book_m2m_author, backref='books')

    def __repr__(self):
        return self.name


# 作者表
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


engine = sqlalchemy.create_engine("mysql+pymysql://root:yyg1990918@localhost/awesome?charset=utf8",
                                  encoding='utf-8', echo=True)
Base.metadata.create_all(engine)
