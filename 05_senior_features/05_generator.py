#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
'''

L = [x*x for x in range(10)]
print(L)

G = (x*x for x in range(10))
print(G)

'''
generator保存的是算法
可以从第一个元素开始，推算出后续任意的元素
就是generator
'''
#如果生成器没有next的值 会出现StopIteration错误
# for x in range(10):
#     print(next(G))

for n in G:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

#上面的函数和generator仅一步之遥。
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
'''
这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

'''
理解方式 yield就是生成 生成后结束,在调用next()后从yield处继续执行
'''
F = fib(6)
print(F)
for x in F:
    print(x)

def odd():
    print('step 1') #第一次next输出
    yield 1         #第一次生成 生成后中断 等待next
    print('step 2')       #调用next输出
    yield(3)              #第二次生成 生成后中断 等待next
    print('step 3')       #第三次next输出
    yield(5)              #第三次生成 生成后中断 再次next没有生成停止迭代代码

'''
但是用for循环调用generator时，
发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，
返回值包含在StopIteration的value中：
'''

g = fib(6)

while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#杨辉三角

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break