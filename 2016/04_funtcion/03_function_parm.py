#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def power(x):
    return x**2
print(power(2))

def power(x,n):
    # s = 1
    # while n > 0:
    #     n = n - 1
    #     s = s * x
    # pass
    return x**n

print(power(2,3))
# 定义了新函数 旧函数失效了 没有类似方法重写的功能
#print(power(2))
#python具有默认参数功能
def power(x, n=2):
    return x**n;

print(power(5))
print(power(2,8))
'''
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
'''

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah','F')
enroll('Bob','F',6)
enroll('Matt','F',6,'Tianjin')

###########坑 默认参数有值时 调用空函数
def add_end(L=[]):
    L.append('End')
    return L
#正常情况下
print(add_end([1,2,3]))
#有问题情况
print(add_end())
print(add_end())#['End', 'End']
'''原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！'''

#解决办法
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end())
print(add_end())
'''
分析有问题的情况:原因是默认参数变量L指向内存中可变对象[] 假设内存地址为0x1f
调用空參函数 L.append('End') 即0x1f上的对象变为['End'],第二次调用
传递进来的L指向的还是这块内存对象 即['End']

没问题情况: L指向不可变对象None 假设内存地址为0x1f 第一次调用改变内存地址指向[],执行append,结束
第二次调用 L指向不可变对象None 指向[]执行append 结束
'''


'''###可变参数 java void sum(int...arr)'''
#通常情况
def calc(numbers):
    s = 0;
    for n in numbers:
        s = s + n**2
    return s

print(calc([1,2,3]))#list
print(calc((1,2,3)))#tuple
print(calc(set([1,2,3,3,3,])))#set
'''
#可变参数情况 会将参数组成为Tuple
'''
def calc(*numbers):
    s = 0;
    print(type(numbers))
    for n in numbers:
        s = s + n**2
    return s

print(calc(1,2,3))
#print(calc([1,2,3]))
# unsupported operand type(s) for ** or pow(): 'list' and 'int'
nums = [1, 2, 3]
print(calc(nums[0],nums[1],nums[2]))

##*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*nums))


'''##关键字参数: **key表示'''
'''可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。'''

def person(name, age, **kw):
    print('name:', name,'age:',age,'other:',kw)

person('Matt',25)

person('Matt',25,city='Tianjin',like='coding')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Matt',25,city=extra['city'],job=extra['job'])
#简化写法
##**extra表示把这个dict元素变为关键字参数传递
##在函数调用时组成dict
person('Matt',25,**extra)

##内部检查
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


'''##命名关键字参数'''
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name,age, * ,city,job):
    print(name,age,city,job)


#由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
#person('Matt',25,123,321,city='Tianjin',job=None)
# person() takes 2 positional arguments but 4 positional arguments (and 2 keyword-only arguments) were given

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数可以有缺省值(类似默认参数)，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Matt',25,job=None)

'''使用命名关键字参数时，要特别注意，如果没有可变参数，
就必须加一个*作为特殊分隔符。如果缺少*，
Python解释器将无法识别位置参数和命名关键字参数：'''
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass



'''##参数组合'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

args = (1, 2, 3, 4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
f2(*args,**kw)

'''
小结

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''