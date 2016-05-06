#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#输出一个绝对值

a = input('please input a number')
try:
    a = int(a)
except Exception:
    print("input is not a number")
    exit()


if a >= 0:
    print(a)
else:
    print(-a)