#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(100))

'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
'''
print(fact(1000))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in fact
  ...
  File "<stdin>", line 4, in fact
RuntimeError: maximum recursion depth exceeded in comparison
#递归超过栈最大值
'''
#尾递归优化
# 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含#[表达式]。

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
#print(fact(1000))依旧栈溢出

def test(num, src, dst, rest):
        if num < 1:
                print(False)
        elif num == 1:
                print("%s -> %s" % (src, dst))
        elif num > 1:
                test(num - 1, src, rest, dst)
                test(1, src, dst, rest)
                test(num - 1, rest, dst, src)
test(3,'A','B','C')