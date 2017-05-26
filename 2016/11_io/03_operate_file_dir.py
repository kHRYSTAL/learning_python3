#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 操作文件和目录
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 03_operate_file_dir.py
@time: 16/5/17 下午8:39
"""
import os
print(os.name)

#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

print(os.uname())
#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


#环境变量
print(os.environ)
#获取某个环境变量的值
print(os.environ.get('PATH'))


'''
操作文件和目录

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''

#查看当前目录绝对路径
print(os.path.abspath('.'))

#在某个目录(当前目录)下创建一个新目录
if not os.path.exists(os.path.join(os.path.abspath('.'),'testdir')):
    os.makedirs(os.path.join(os.path.abspath('.'),'testdir'))

#删掉一个目录
os.rmdir(os.path.join(os.path.abspath('.'),'testdir'))


'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

part-1/part-2
而Windows下会返回这样的字符串：

part-1\part-2
'''

'''
同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
'''

'''
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
'''

#os.rename('test.txt', 'test.py')
#os.rename('test.py', 'test.txt')

#删掉文件
# 删掉文件:
#os.remove('test.py')

'''
但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
'''

#过滤文件
#列出所有根目录下文件

L = [x for x in os.listdir('/') if not os.path.isdir(x)]
print(L)


#列出当前目录下所有后缀为py的文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(L)

#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。














def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass