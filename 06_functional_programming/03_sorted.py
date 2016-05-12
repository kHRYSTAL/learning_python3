#!/usr/bin/env python3
#-*-coding:utf-8 -*-

# print(sorted([23,3,-1,0,31,False,'a']))
# TypeError: unorderable types: str() < int()

L = [36, 5, -12, 9, -21]
print(sorted(filter(lambda x:isinstance(x,int) or isinstance(x,float),[23,3,-1,0,31,22.2,'a'])))

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

print(sorted(L,key = abs))

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))

print(sorted(L,key = str.lower,reverse = True))

#按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def getNameLower(t):
    return t[0].lower()

def getScore(t):
    return t[1]



f = lambda x:x[0].lower()

# print(sorted(L,key= lambda x:x[0].lower))
# TypeError: unorderable types: builtin_function_or_method() < builtin_function_or_method()

print(sorted(L,key = f))




print(sorted(L,key = getNameLower))
print(f(('A',75)))

print(sorted(L,key=lambda x:x[1],reverse=True))

