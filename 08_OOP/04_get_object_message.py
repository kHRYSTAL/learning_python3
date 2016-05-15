#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 获取对象信息
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 04_get_object_message.py
@time: 16/5/15 下午8:21
"""




'当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？'

#type

print(type(123))
print(type('str'))
print(type(None))

#如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))

#但是type()函数返回的是什么类型呢？
# 它返回对应的Class类型。如果我们要在if语句中判断，
# 就需要比较两个变量的type类型是否相同

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type(123))

#判断基本数据类型可以直接写int，str等，
# 但如果要判断一个对象是否是函数怎么办？
# 可以使用types模块中定义的常量

import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


#使用isinstance()

class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(d,Animal))
print(isinstance(d,Husky))

#判断是不是指定多种中的一种
print(isinstance([1,2,3],(list,tuple)))
print(isinstance(d,(Husky,Animal)))




#使用dir()获得一个对象的所有属性和方法


##实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100


d = MyDog()

print(len(d))

#仅仅把属性和方法列出来是不够的，
# 配合getattr()、setattr()以及hasattr()，
# 我们可以直接操作一个对象的状态

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x**2

obj = MyObject()

print(hasattr(obj,'x'))#有属性x吗
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)#设置一个属性y,默认值19
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)

'''
如果试图获取不存在的属性，会抛出AttributeError的错误：

>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
可以传入一个default参数，如果属性不存在，就返回默认值：

>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
'''

print(hasattr(obj,'power'))
print(getattr(obj,'power'))

fn = getattr(obj,'power')
print(fn())
#调用fn()与调用obj.power()是一样的



'''
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

sum = obj.x + obj.y
就不要写：

sum = getattr(obj, 'x') + getattr(obj, 'y')
一个正确的用法的例子如下：

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''
def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass