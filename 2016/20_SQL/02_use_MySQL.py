#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 02_use_MySQL.py
@time: 16/5/26 下午8:23
"""
'''
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。
'''

'''
安装


可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。

安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，
把数据库默认的编码全部改为UTF-8。
MySQL的配置文件默认存放在/etc/my.cnf
或者/etc/mysql/my.cnf

http://dev.mysql.com/downloads/mysql/5.6.html
'''
#修改my.cnf 不知道什么原因 不支持utf8mb4
'''
安装MySQL驱动

由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：

$ pip install mysql-connector-python --allow-external mysql-connector-python
'''
'''
192:etc kHRYSTAL$ pip install mysql-connector-python --allow-external mysql-connector-python
DEPRECATION: --allow-external has been deprecated and will be removed in the future. Due to changes in the repository protocol, it no longer has any effect.
Collecting mysql-connector-python
  Could not find a version that satisfies the requirement mysql-connector-python (from versions: )
No matching distribution found for mysql-connector-python
192:etc kHRYSTAL$ pip install mysql-connector-python-rf --allow-external mysql-connector-python
#3.5.1貌似还没有mysql-connector 可以使用pymysql


'''
'''
There is an outstanding bug with the way it is packaged on PIP. here are the details: http://bugs.mysql.com/bug.php?id=76063

You can use following commands to install mysql-connector as mentioned on same link :

wget https://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.3.zip
unzip mysql-connector-python-2.0.3.zip
cd mysql-connector-python-2.0.3
python setup.py install
'''



import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='yyg1990918',db='test',charset='utf8')
cursor = conn.cursor()

#创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)

print('Cursor.close',cursor.close())
conn.close()






def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass