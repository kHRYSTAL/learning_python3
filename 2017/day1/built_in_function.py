#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: built_in_function.py
# @time: 17/5/29 上午12:32

# region 字符串转代码
# str = '''
# def test():
#     print("hello")
# test()
# '''
# exec(str)
# endregion

# region 字符串转表达式
# res = eval("1+2")
# print(res)
# endregion

# region dict 转化为字典
# d = dict(x=1, y=2, z=3)
# print(d)
# endregion

# region 过滤 filter 是迭代器
# res = filter(lambda n: n > 5, range(10))
# print(res)
# for i in res:
#     print(i)
# endregion

# region map 处理函数的元素 是迭代器
# res = map(lambda n: n*n, range(10))
# print(res)
# for i in res:
#     print(i)

# 相当于
# res = [(lambda i: i*i)(i) for i in range(10)]
# print(res)

# res = [i*i for i in range(10)]
# print(res)
# endregion

# region reduce 相邻两个元素之间处理 得到的结果为下次执行函数的x
import functools

# 累加
# res = functools.reduce(lambda x, y: x+y, range(10))
# print(res)
# 阶乘
# res = functools.reduce(lambda x, y: x*y, range(1, 10))
# print(res)
# endregion

# region frozenset 不可变集合 集合本身是可变的
# res = frozenset([1, 2, 3, 4, 5])
# endregion

# region globals 返回整个文件的全局变量(key)和变量的值value 但不能打印函数的局部变量
# print(globals())


# endregion

# region 打印函数内部所有变量
# def test():
#     local_var = 333
#     print(locals())
#
# test()
# print(globals().get('local_var'))  # 返回None
# endregion

# region str repr 转字符串
'''
__repr__的目标是准确性
__str__的目标是可读性
容器的__str__使用包含了对象的__repr__
可以看出repr中print结果刻意保留引号来表示其为str类型，
而后面一个也在精度上显示更多，对应的str方法则更注重可读性，去掉不重要的内容。
当然这个并不是一定的，有的时候如果类中__str__方法没有定义则会默认采用__str__=__repr__。
'''
# obj = 'hello'
# print(str(obj))
# print(repr(obj))
# print(str(1.0/7.0))
# print(repr(1.0/7.0))
# endregion

# region slice 切片
# d = list(range(20))
# print(d)
# print(d[slice(2, 5)])
# endregion

# region sorted 排序
# a = {6: 2, 8: 0, 1: 4, -5: 6}  # 字典无顺序
# print(a)
# print(sorted(a))  # 默认排序key
# print(sorted(a.items()))
# # 按value排序
# print(sorted(a.items(), key=lambda x: x[1]))
# endregion

# region zip 拉链 一一对应组合 按数量少的原则组成元组元素列表, 超出的抛弃
# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
# c = list(zip(a, b))
# print(c)
# endregion

# region import 按字符串导入包名
# __import__('time')
# endregion

if __name__ == '__main__':
    pass
