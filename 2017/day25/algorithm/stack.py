#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: check kuohao
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: stack.py
# @time: 18/2/16 下午4:42

"""
栈 后进先出
append压栈
pop出栈
栈的应用————括号匹配问题

                括号匹配问题: 给一个字符串, 其中包含小括号 中括号 大括号
                求该字符串中的括号是否匹配

                例如:
                    ()()[]{} 匹配
                    ([{()}]) 匹配
                    [](  不匹配
                    [(]) 不匹配

"""


def check_kuohao(s):
    stack = []
    for char in s:
        # 判断字符是否属于集合, 集合比列表快
        if char in {'(', '[', '{'}:
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

print(check_kuohao("()()[]{}"))
print(check_kuohao("[(])"))
