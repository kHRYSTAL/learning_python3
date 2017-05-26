#!/usr/bin/env python3
#-*-coding:utf-8 -*-
'''

和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd,list(range(10)))))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A' ,'','  ',' B',None])))

####列出所有素数

def _ood_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _ood_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

# for i in primes():
#     if i < 100:
#         print(i)
#     else:
#         break


##找出1到1000内所有回数

def is_palindrome(n):
    n = str(n)
    return n[:] == n[::-1]

print(list(filter(is_palindrome,range(1,1000))))
