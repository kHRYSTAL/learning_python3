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
@file: 01_file_read_write.py
@time: 16/5/17 下午7:59
"""
'''
读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
'''
try:
    f = open('test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()


#等价方法

with open('test.txt', 'r') as f:
    print(f.read())
   # print(f.readlines())

'''
这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
'''

'''
file-like Object

像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''

#读取二进制文件
with open('test.jpg','rb') as f:
    print(f.read())


#读取gbk编码文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

#读取编码不规范文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

#写文件
# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')

# 'r'    open for reading (default)
# 'w'    open for writing, truncating the file first
# 'x'    open for exclusive creation, failing if the file already exists
# 'a'    open for writing, appending to the end of the file if it exists
# 'b'    binary mode
# 't'    text mode (default)
# '+'    open a disk file for updating (reading and writing)
# 'U'    universal newlines mode (deprecated)




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass