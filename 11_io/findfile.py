#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: test.py
@time: 16/5/17 下午11:12
"""
import os

def findFile(path,key):
    result = []
    #列出目录下指定后缀名的文件
    resultFiles = [os.path.join(path, x) for x in os.listdir(path) if
                   os.path.isfile(os.path.join(path, x)) and key in x]
    #列出目录下的目录 用于递归
    dictPaths = [os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    if dictPaths == []:
        return resultFiles
    else:
        for i in dictPaths:
            result += resultFiles
        return result

def saveResult(path,keys,files):
    with open(r'findfile.txt','w',encoding='utf-8') as f:
        f.write('Path:' + path + '\tKey:' )
        for key in keys:
            f.write(key + ' ')
        f.write('\n')
        f.write('==================  %d   Results found.==================\n' % len(files))
        for i in files:
            f.write(i + '\n')





def main():
    path=input("Please input the path:")
    keys=input("Please input the key:").split(',')
    files=[]
    for key in keys:
        files=files+findFile(path,key)
    saveResult(path,keys,files)

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    pass