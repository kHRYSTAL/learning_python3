#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 序列化
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 04_serialize.py
@time: 16/5/17 下午11:31
"""

'''
在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：

d = dict(name='Bob', age=20, score=88)
可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
'''

'''
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
'''

import pickle
import os
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)#转储
'''
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
if not os.path.exists('dump.txt'):
    f = open('dump.txt','wb')#把序列化后的二进制对象写入dump.txt
    pickle.dump(d,f)
    f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
'''
if os.path.exists('dump.txt'):
    f = open('dump.txt','rb')
    d = pickle.load(f)
    f.close()
    d['name'] = 'Matt'

print(d)

'''
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
#pickle是序列化成bytes json是序列化成str

JSON类型	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	    int或float
true/false	True/False
null	    None
'''

import json
d = dict(name='Bob',age=20,score=99)
print(d)
if not os.path.exists('jsondump.txt'):
    with open(r'jsondump.txt', 'w', encoding='utf-8') as f:
        json.dump(d,f)

if os.path.exists('jsondump.txt'):
    with open(r'jsondump.txt','r',encoding='utf-8') as f:
        print(json.loads(f.read()))


#对象序列化

#光这样是不行的 因为student本身不是一个可序列化对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(s):
    return {
        'name':s.name,
        'age':s.age,
        'score':s.score
    }


s = Student('Bob', 20, 88)

print(json.dumps(s,default=student2dict))


#不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：

print(json.dumps(s, default=lambda x: x.__dict__))
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


'''
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例
'''

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])



json_str = '{"age": 26, "score": 100, "name": "Bob"}'

loads = json.loads(json_str, object_hook=dict2student)
print(loads,'\n',loads.name,loads.age,loads.score)


'''
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，
我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass