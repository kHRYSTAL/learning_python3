#!/usr/bin/env python3
#-*- coding:utf-8 -*-

print(list(range(1,11)))

L = []
for x in range(1,11):
    L.append(x**2)
print(L)

print([x**2 for x in range(1,11)])

#生成式for循环后可加判断
print([x**2 for x in range(1,11) if x%2 == 0])

#可嵌套循环
print([ m+n for m in 'ABC' for n in 'XYZ'])

import os
#列出当前目录所有文件名
print([d for d in os.listdir(".")])


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,"=",v)

print([k+"="+v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']

print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)