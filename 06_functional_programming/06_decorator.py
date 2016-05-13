#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def now():
    print('2016-05-13')

f = now
print(f)
print(type(f))
f()
print(now.__name__)
print(f.__name__)

'''
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():' % func.__name__)
        return func(*args,**kwargs)
    return wrapper

'''
观察上面的log，因为它是一个decorator，
所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
'''
@log
def now():
    print('2016-05-13')
print(now.__name__)
#@语法相当于把now=now 变成now = log(now)
print('############')
now()
'''
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
写出来会更复杂。比如，要自定义log的文本：
'''

def log(text):
    def decorator(func):
        def wrapper(*args ,**kwargs):
            print(text,"%s():" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-05-13')

print(now.__name__)
print(now)
now()

'''
此时now.__name__变成了wrapper 因为经过装饰之后 原来的函数经过wrapper包裹
'''

'''
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
，所以，一个完整的decorator的写法如下：
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args ,**kwargs):
        print("call %s():" % func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print("2015-05-14")

print(now)
print(now.__name__)
now()




def log(text=None):
    if not callable(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('begin %s :%s()' % (text,func.__name__))
                ret = func(*args,**kwargs)
                print('end %s :%s()' % (text,func.__name__))
                return ret
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kwargs):
            print('begin %s()' % (text.__name__))
            ret = text(*args, **kwargs)
            print('end %s()' % (text.__name__))
            return ret
        return wrapper

@log
def f1():
    pass


@log('execute')
def f2():
    pass

if __name__ == '__main__':
    f1()
    f2()



