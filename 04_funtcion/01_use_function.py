#!/usr/bin/env python3
# -*- coding:utf-8 -*-

i = abs(100)
print(i)

i = abs(-20)
print(i)

i = abs(12.34)
print(i)

# i = abs(1,2)
# print(i)
# Traceback (most recent call last):
#   File "01_use_function.py", line 13, in <module>
#     i = abs(1,2)
# TypeError: abs() takes exactly one argument (2 given)


# i = abs('a')
# print(i)
# Traceback (most recent call last):
#   File "01_use_function.py", line 21, in <module>
#     i = abs('a')
# TypeError: bad operand type for abs(): 'str'


i = max(1,2)
print(i)

i = max(2,3,1,-5)
print(i)

#force transform
i = int('123')
print(i)
i = int(12.34)
print(i)
i = str(100)
print(i)
i = bool(1)
print(i)
i = bool('')
print(i)

'''
函数名其实就是指向一个函数对象的引用，
完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
'''

i = abs
print(i(-1))

n1 = 255
n2 = 1000
n3 = 12.34
print(str(hex(n1)))
print(str(hex(n2)))
print(str(float.hex(n3)))


