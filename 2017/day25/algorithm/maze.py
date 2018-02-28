#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: maze.py
# @time: 18/2/28 下午7:13

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),  # 右
    lambda x, y: (x - 1, y),  # 左
    lambda x, y: (x, y - 1),  # 上
    lambda x, y: (x, y + 1),  # 下
]


def mpath(x1, y1, x2, y2):
    """
    :param x1: 起点x
    :param y1: 起点y
    :param x2: 终点x
    :param y2: 终点y
    :return:
    """
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]  # curNode 为两个元素的元组
        if curNode[0] == x2 and curNode[1] == y2:
            # 到达终点
            print('到达终点路径为:', stack)
        for dir in dirs:  # 遍历方向
            nexNode = dir(*curNode)  # 元祖解包
            if maze[nexNode[0]][nexNode[1]] == 0:
                # 找到了下一个可移动的位置
                stack.append(nexNode)
                # 标记已经走过的位置
                maze[nexNode[0]][nexNode[1]] = -1  # 标记已经走过防止死循环
                break  # 跳出当前循环, 以nextNode 作为curNode继续向下走
        else:  # 四个方向都没找到
            maze[curNode[0]][curNode[1]] = -1  # 死路一条需要回退
            stack.pop()  # 回退

mpath(1, 1, 8, 8)
