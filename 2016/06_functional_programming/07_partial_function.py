#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import functools

print(int('12345'))

#10为二进制 转化为10进制
print(int('10',base=2))
print(int('12345',base=8))


def int2to10(x,base=2):
    return int(x,base)

print(int2to10('1111111'))

#改变给定参数名参数默认值 生成新的函数
int2to10 = functools.partial(int,base = 2)
print(int2to10('111111'))

#调用时还可以再修改
print(int2to10('11111',base=10))

'''
实际上固定了int()函数的关键字参数base，也就是：

int2('10010')
相当于：

kw = { 'base': 2 }
int('10010', **kw)
'''

'''
实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
相当于：

args = (10, 5, 6, 7)
max(*args)
'''

max2 = functools.partial(max,10)
print(max2(4,5,6))

'''
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''