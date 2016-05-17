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
@file: 02_stringio_bytesio.py
@time: 16/5/17 下午8:22
"""
'''
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。
'''

from io import StringIO

f = StringIO()#创建stringio对象

#写入内存
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())




#BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))#请注意，写入的不是str，而是经过UTF-8编码的bytes。
print(f.getvalue())


'''
f.read()是会从你设定(或者默认)的position开始读取数据，f.getvalue()会返回当前存储的数据，举个例子:

>>> f = StringIO("1\n2\n3") #f.tell() = 0
>>> f.getvalue()
'1\n2\n3'
>>> f.read()
'1\n2\n3'        #f.tell() = 5
>>> f.read()
''                # 因为position＝5开始读，没有数据，所以是''
>>> f.getvalue()
'1\n2\n3'
'''

'''
f = StringIO()
stream position也为0，而执行

f.write('Hello World')
stream position就移动到11了，因此你再执行readline时返回的依旧是空字符串，若你需要返回'Hello World'可以通过

f.seek(0)
'''



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass