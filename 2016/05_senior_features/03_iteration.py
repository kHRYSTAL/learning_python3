#!/usr/bin/env python3
#-*-coding:utf-8 -*-

#迭代即(按顺序)每次取出一个值
#java中无序迭代很麻烦 如hashmap 需要用到Map.Entry或Iterator
# python可以很简单实现

L = list(range(10))
for i in L:
   # print(L[i])
    pass
'''
list这种数据类型虽然有下标，
但很多其他数据类型是没有下标的，
但是，只要是可迭代对象，无论有无下标，都可以迭代
'''

d = {'a':1,'b':2,'c':3,'d':False}
for key in d:
  #  print(key)
    pass

'''
默认情况下，dict迭代的是key。如果要迭代value
，可以用for value in d.values()，如果要同时迭代key和value，
可以用for k, v in d.items()。
'''

for value in d.values():
    # print(value)
    pass

print(d.items())

for key,value in d.items():
    # print(key,value)
    pass

for ch in 'ABC':
    # print(ch)
    pass

##判断是否是可迭代对象
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance(L,Iterable))
print(isinstance(123,Iterable))

'''
如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
'''

print(enumerate(L))
#enumerate 可以生成下标索引
for i, value in enumerate(L):
    #print(i, value)
    pass

for i, value in enumerate(d):
    print(i, value)