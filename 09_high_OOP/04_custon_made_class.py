#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 定制类
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 04_custon_made_class.py
@time: 16/5/16 下午9:47
"""

class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('Matt'))

'''
打印出一堆<__main__.Student object at 0x109afb190>，不好看。

怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
'''

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Matt'))

'''
但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：

>>> s = Student('Michael')
>>> s
<__main__.Student object at 0x109afb310>
这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
'''

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

#__iter__

'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环
'''

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self #实例本身就是迭代对象,返回自己
    def __next__(self):
        self.a ,self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise  StopIteration()
        return self.a

# for i in Fib():
#     print(i)

'''
__getitem__

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

>>> Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
'''

class Fib(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b = b, a+b
        return a

f = Fib()

print(f[0])
print(f[22])


'''
但是list有个神奇的切片方法：

>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]
对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
'''


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()
print(f[1:5])

'''
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

'''

'''
__getattr__

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：

class Student(object):

    def __init__(self):
        self.name = 'Michael'
调用name属性，没问题，但是，调用不存在的score属性，就有问题了：

>>> s = Student()
>>> print(s.name)
Michael
>>> print(s.score)
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'score'
错误信息很清楚地告诉我们，没有找到score这个attribute。

要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
'''

class Student(object):
    def __init__(self):
        self.name = "Matt"
    def __getattr__(self, item):
        if item=="score":
            return 99
        if item == 'age':
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
'''
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
'''

s = Student()
print(s.name)
print(s.score)
print(s.age())#返回函数


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
'''
这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

还有些REST API会把参数放到URL中，比如GitHub的API：
'''

class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))
    def users(self, name):
        return Chain('%s/%s' % (self._path, name))
    def __str__(self):
        return self._path
    __repr__ = __str__


print(Chain().users('matt').repos)

'''
__call__

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
'''

class Student(object):
    def __init__(self, name=''):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)

matt = Student('Matt')
matt()

print(callable(Student()))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))


'''
Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档。

http://docs.python.org/3/reference/datamodel.html#special-method-names
'''


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass