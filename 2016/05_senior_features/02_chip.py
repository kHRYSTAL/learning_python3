#!/usr/bin/env python3
#-*- coding:utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前三个元素
print([L[0],L[1],L[2]])

r = []
n = 3
for i in range(3):
    r.append(L[i])

print(r)

#切片
print(L[0:3])

#从1开始 到3结束
print(L[1:3])

#从倒数第二个开始
print(L[-2:])
#从倒数第三个开始 取倒数第三个和第二个
print(L[-3:-1])

L = list(range(100))
print(L)

#取前十个
print(L[:10])
print(L[0:10])
#取后十个
print(L[-10:])
#11-20
print(L[11:20])
#取前十个 每两个取一个
print(L[0:10:2])
#每5个取一个
print(L[::5])

D = L[:]
print(D==L)


#tuple
T = tuple(range(6))
print(T)
print(T[:3])

#str
S = 'ABCDEFG'
print(S[:3])
print(S[::2])

