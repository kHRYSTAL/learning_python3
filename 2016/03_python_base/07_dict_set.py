#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#dict 字典 类似Java HashMap
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
print(d)
d['Adam'] = 67
print(d)

#如果使用这种方式获取value
#如果key不存在就会报错
#所以要加判断
print('Tomas' in d)
if 'Tomas' in d:
    print(d['Tomas'])
else:
    print('not find Tomas')

#第二种方式 类似Java
d.get('Tomas')
print(d.get('Tomas'))

print(d.get('Tomas',-1))

#删除key
d.pop('Bob')
print(d)

#list 不能作为dict的key 因为list可变
#key = [1,2,3]
#d[key] = "a list"
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

'''

#set 集合 类似HashSet 可以理解为只有key没有value的dict
#因为只有key 所以set不是重复的
#以set([data...])声明

s = set([1,2,3])
print(s)

s = set([1,2,3,3,3,2])
print(s)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
#删除
s.remove(4)
print(s)

#交集 并集
s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)

print(s1 | s2)

#str是不变对象，而list是可变对象
a = 'abc'
b = a.replace('a','A')
print(b)
print(a)

a1 = {'first':(1,2,3),'sec':(1,[2,3])}
print(a1)
get = a1.get('sec')
print(get)
get[1][0] = 4

print(a1)

#由于key要求是能够进行哈希的 list可变 不能设为集合中的对象
#a2 = set([(1,2,3),(1,[2,3])])
#print(a2)

#zip函数 将两个或多个有序序列按顺序一一对应 返回一个zip对象
ts = zip(['A','B','C'],['1','2','3'])
print(ts)
print(type(ts))
for x in ts:
    print(x)
