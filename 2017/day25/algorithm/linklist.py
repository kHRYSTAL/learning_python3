#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 链表实现
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: linklist.py
# @time: 18/2/27 下午2:28


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


# a = Node(10)
# b = Node(20)
# c = Node(30)
#
# a.next = b
# b.next = c

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(head.next.next.item)


def traversal(head):
    curNode = head  # 临时用指针
    while curNode.next:
        print(curNode.item)
        curNode = curNode.next
    else:
        print(curNode.item)

print(traversal(head))
