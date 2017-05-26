#!/usr/bin/env python3
# -*-coding:utf-8 -*-

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#通常情况

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print(lazy_sum(1,2,3)())
print(type(f))
print(f)

print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''

##当我们调用lazy_sum()时，每次调用都会返回一个新的函数，

f1 = lazy_sum(1,2,3)
f2 = lazy_sum(1,2,3)

print(f1 == f2)

'''
注意到返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
所以，闭包用起来简单，实现起来可不容易。
'''
#eg.
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())
'''
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。#等到3个函数都返回时，它们所引用的变量i已经变成了3#，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''

'''
http://www.cnblogs.com/ma6174/archive/2013/04/15/3022548.html
'''

def count():
    def f(j):#传入的值就不会再改变了 相当于final
        def g():#把它理解为匿名内部类 类中调用了外部类参数 则外部类参数是final的
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2, f3 = count();
print(f1(),f2(),f3())

'''
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
闭包持有的外部变量不要是能够被修改或会发生变化的变量
'''