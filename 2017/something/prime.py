#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: prime.py
# @time: 19/4/3 下午6:11

import math

product = 7140229933


def func_get_prime_multiplier(n, onlyOne=True):
    primes = filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, n + 1))
    for x in primes:
        if math.modf(n / x)[0] == 0.0 and is_prime(int(math.modf(n / x)[1])):
            print(x, n // x)
            if onlyOne:
                break
    else:
        print('None')


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


# question 1
print('#1')
func_get_prime_multiplier(product, True)

# question 2
print('#2')
for i in range(6541367000, 6541367999):
    print('10位数为:', i)
    func_get_prime_multiplier(i, False)
