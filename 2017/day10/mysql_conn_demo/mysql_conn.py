#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: mysql_conn.py
# @time: 17/8/3 下午11:47
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='yyg1990918', db='awesome')

# 创建游标
cursor = conn.cursor()

# # 执行SQL 并返回影响行数
# effect_row = cursor.execute("select * from users")
# print('effect_row', effect_row)
#
# print(cursor.fetchone())  # 获取一条, 获取后游标在第一条
#
# print(cursor.fetchall())  # 此时不会在打印第0条的数据


# 批量执行

data = [('13iu7812973', '123456', '3@qq.com', 0, 'Jack', 'http://1.jpg', '1464888787.88908'),
        ('98123123sad23123', '123456', '4@qq.com', 0, 'Pato', 'http://1.jpg', '1464888787.88908')]

# 执行多条语句 many是以事务执行的 需要提交
cursor.executemany("insert into users (id, passwd, email, admin, name, image, created_at)"
                   " VALUES (%s, %s, %s, %s, %s, %s, %s)", data)
conn.commit()


effect_row = cursor.execute("select * from users")
print(cursor.fetchall())



