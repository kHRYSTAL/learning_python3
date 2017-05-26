#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types
#List
classmates = ['Michael','Bob','Trac']

print(classmates)
print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
#取最后一个元素
print(classmates[-1])
print(classmates[len(classmates)-1])

print(classmates[-2])
print(classmates[-3])
'''
数组越界
print(classmates[-4])
print(classmates[3])
'''

classmates.append('Adam')
print(classmates)

classmates.insert(1,'Jack')
print(classmates)

#删除指定位置元素元素,空参表示删除末尾
classmates_pop = classmates.pop()
print('pop is',classmates_pop,'list:',classmates)
pop = classmates.pop(1)
print('pop is',pop,'list:',classmates)
classmates[1] = 'Matt'
print(classmates)

#python中list同Java不同,可以包含不同类型
L = ['Apple',123,True]
print(L)

#List嵌套
s = ['python','java',['asp','php'],'scheme']
print(len(s))
print(s[2])
print(s[2][0],s[2][1])
p = ['asp','php']
s = ['python','java',p,'scheme']
print(s)

#空List
L = []
print(len(L))

########################################
#tuple元组 tuple一旦初始化就不能修改
print("######################")
t = (1,2)
print(t)

#tuple不可改变 所以代码更安全 类似Java枚举,intDef注解等
classmates = ('Michael','Bob','Tracy')
print(classmates[-1])
print(len(classmates))

#空tuple
t = ()
print(t)

#Notice: 当元组中只有一个值的时候需要加','因为括号有歧义
t = (1)
print(type(t))
if isinstance(t,int):
    print("t's type is integer")
t = (1,)
print(type(t))

if isinstance(t,tuple):
    print("t's type is tuple")


#可变tuple实际上内存指向中变的是list的内存地址 tuple存储的只是list的指向,也就是说tuple只能保证指向不变

t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 123
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

#小结

#list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。