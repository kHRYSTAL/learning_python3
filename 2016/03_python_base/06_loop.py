#!/usr/bin/env python3
# -*-coding:utf-8 -*-

names = ['Michael','Bob','Tracy']
for name in names:
    print(name)

sum = 0;
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

l = list(range(5))
print(l)


s = 0
for x in range(101):
    s = s + x
print(s)


sum = 0
n = 99;
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Bart','Lisa','Adam']

for name in L:
    print("Hello,",name,"!")
