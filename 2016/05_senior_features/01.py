#!/usr/bin/env python3
#-*- coding:utf-8-*-

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n+2

print(L)
L = []

for i in range(1,99,2):
    L.append(i)
print(L)

print(list(range(1,99,2)))
print(list(range(0,100))[1::2])

L=[x*2+1 for x in range(50)]
print(L)