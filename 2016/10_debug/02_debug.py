#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 调试代码
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 02_debug.py
@time: 16/5/17 下午4:07
"""
#调试方法一:打印
def foo(s):
    n = int(s)
    print('>>>n = %d' % n)
    return 10/n

def main():
    foo('0')

#main()
#用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。

#调试方法二:断言

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

#main()
'''
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError
'''

'''
程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

$ python3 -O err.py##################
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
关闭后，你可以把所有的assert语句当成pass来看。
'''

#调试方法三:logging

import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
#print(10/n)
'''
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
'''


#调试方法四:pdb

# s = '0'
# n = int(s)
# print(10/n)

#执行python3 -m pdb err.py ,l查看代码 n单步执行 p+变量名 查看变量
#q退出程序


#调试方法五:pdb.set_trace() 设置断点
#c 继续执行
import pdb

s = '0'
n = int(s)
#pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass