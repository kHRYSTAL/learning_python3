#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: collections是Python内建的一个集合模块，提供了许多有用的集合类。

@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 02_collections.py
@time: 16/5/23 下午2:54
"""

#namedtuple
from collections import namedtuple, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x,p.y)

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])


#deque

'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
from collections import deque

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

#defaultdict
from collections import defaultdict

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])

'''
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''

#OrderDict

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict
#d是无序的
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

#od是有序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)




from collections import OrderedDict


#FIFI dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            '''
            od.popitem() -> (k, v), return and remove a (key, value) pair.
            Pairs are returned in LIFO order if last is true or FIFO order if false.
            也就是说，如果last=false，就返回最先进入的元素。

            '''
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)



#Counter 计数器

c = Counter()#dict子类 值为空时返回0

for ch in 'programming':
    c[ch] = c[ch] + 1

dd = defaultdict(lambda : 0)

for ch in 'programming':
    dd[ch] = dd[ch] + 1


print(c)
print(dd)

'''
collections模块提供了一些有用的集合类，可以根据需要选用。
'''



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass