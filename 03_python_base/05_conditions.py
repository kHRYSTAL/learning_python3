#!/usr/bin/env python3
# -*-coding utf-8 -*-

age = 20;
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

age = 3

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 10
if x:
    print('True')

# s = input('birth:')
# try:
#     birth = int(s)
# except ValueError:
#     print('not year!')
#     exit()
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5

BMI =round(weight/(height**2),2)
print("BMI is",BMI)

if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('过于肥胖')