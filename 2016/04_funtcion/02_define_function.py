#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

return None可以简写为return。
'''

# def my_abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x

#空函数 pass可以用来作为占位符
def nop():
    pass
##如果缺少pass 会有语法错误
def setAge(x):
    if x > 18:
        pass
    else:
        print("nopass")

setAge(20)
setAge(16)

#参数检查 抛出异常 类似throw Exception('')

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         return x
#     else:
#         return -x
#
# print(my_abs('a'))
##############


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)

#实际上函数返回的是单一值 一个tuple
r = move(100,100,60,math.pi/3)
print(r)

#########
def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1,x2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))


