#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''

def f(x):
    return x**2

#list中的每个函数都将调用f函数 最终生成一个迭代器
r = map(f,list(range(10)))

print(type(r))
print(type({}))

print(list(r))
'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''

L = []
for n in list(range(10)):
    L.append(f(n))
print(L)

print(list(map(str ,list(range(10)))))


'''
reduce
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，

##这个函数必须接收两个参数###，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add,list(range(10))))
print(sum(list(range(10))))


#################通过map,reduce将数字字符串转换为数字
def f(x,y):
    return x * 10 + y

def charTonum(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(reduce(f,map(charTonum,'12345')))

##################

def str2int(x):
    def f(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(f,map(char2num,x))

print(str2int('23456'))


def str2int(x):
    return reduce(lambda x,y:x*10+y,map(charTonum,x))

print(str2int('1234'))

###########
L = ['adam', 'LISA', 'barT']
print(list(map(lambda x:x.capitalize(),L)))
###########
def prod(*arg):
    return reduce(lambda x,y:x * y,arg)

print(prod(1,2,3,4))

print(pow(10,2))

s = '123.456'
print(s.find('.'))
print(len(s))

def str2float(s):
    if '.' in s:
        index = s.find('.')
        length = len(s)
        s.replace('.','')
        return reduce(lambda x,y:x*10+y,map(charTonum,s))/pow(10,index-length-1)

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print('123.4567')