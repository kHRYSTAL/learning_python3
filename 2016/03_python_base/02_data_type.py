#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#整数
a = 1
b = 100
c = -8080
d = 0

#16进制
0xff00
0xa5b4c3d2

#浮点数
1.23
3.14
-9.01

# 科学计数法
1.23e9
12.3e8
1.2e-5

#字符串
'abc'
"xyz"

"I'm \"OK\""

print('I\'m \"OK\"')
#打印制表,换行"\"
print("\\\t\\")
print("\\\n\\")

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

#Boolean

print(3>2)
print(3>5)
print(True and True)
print(True and False)
print(True or False)
print(5>3 or 1 >3)

#非运算
not True
print(not 1 > 2)

age = 25
if age >= 18:
    print('adult')
else:
    print('teenager')

#空值
None
print(None)

##变量
'''
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：

int a = 123; // a是整数类型变量
a = "ABC"; // 错误：不能把字符串赋给整型变量
和静态语言相比，动态语言更灵活，就是这个原因。

请不要把赋值语句的等号等同于数学的等号。比如下面的代码：
'''

a = 123
print(a)
a = 'ABC'
print(a)

#常量

#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.1415926
#除法
print(10 / 3)
print(9/3)
print(10//3)
#求余
print(10%3)

print(r'Hello,"Bart"')#r的作用:防止字符转译
print(r'''Hello,
Lisa!''')
print(r"\t\t")


'''
注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
'''