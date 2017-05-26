#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
'''

i = ord('A')
print(i)
i = ord('中')
print(i)
i = chr(66)
print(i)
i = chr(25991)
print(i)

i = '\u4e2d\u6587'
print(i)

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
i = 'ABC'.encode('ascii')
print(i)
#解码
print(i.decode('ascii'))
i = '中文'.encode('utf-8')
print(i)
print(i.decode('utf-8'))

i = 'ABC'
print(len(i))
i = '中文'
print(len(i))#打印字符串长度
print(len(i.encode('utf-8')))#打印字节长度


#字符串格式化
print('Hello,%s'%'world')
print('Hi,%s,you have $%d'%('Michael',100000))
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)

#转译'%'
print('growth rate: %d %%' % 7)
