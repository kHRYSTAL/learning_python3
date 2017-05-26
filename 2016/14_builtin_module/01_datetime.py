#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 日期时间标准库
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 01_datetime.py
@time: 16/5/23 下午2:25
"""

from datetime import datetime

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2016,5,23,2,26)
print(dt)


#datetime转换为timestamp

'''
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

你可以认为：

timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是：

timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

'''

dt = datetime(2016,5,23,2,28)
ts = dt.timestamp()

print(ts)

'''
注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
'''
#ts 转换dt
t = 1429417200.0
print(datetime.fromtimestamp(t))

'''
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。

本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：

2015-04-19 12:20:00
实际上就是UTC+8:00时区的时间：

2015-04-19 12:20:00 UTC+8:00
而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：

2015-04-19 04:20:00 UTC+0:00
timestamp也可以直接被转换到UTC标准时区的时间：

>>> from datetime import datetime
>>> t = 1429417200.0
>>> print(datetime.fromtimestamp(t)) # 本地时间
2015-04-19 12:20:00
>>> print(datetime.utcfromtimestamp(t)) # UTC时间
2015-04-19 04:20:00
'''

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%a,%b %d %H:%M'))



#datetime加减

'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
from datetime import timedelta

print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2,hours=12))



#本地时间转换为UTC时间
from  datetime import timezone
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
'''

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00

print(dt)


#时区转换

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
'''

'''
小结

datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''
import re
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    a = re.match(r'(UTC)([\-|\+]\d{1,2})(\:00)', tz_str)
    tz = a.group(2)
    tz_utc = timezone(timedelta(hours=int(tz)))
    dt_tz = dt.replace(tzinfo=tz_utc)
    return dt_tz.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t1)
print(t2)




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass