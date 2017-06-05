#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: xml_module.py
# @time: 17/6/5 上午11:51
import xml.etree.ElementTree as ET

tree = ET.parse('xml_test.xml')
root = tree.getroot()
print(root.tag)


# 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)

# 只遍历year节点
for node in root.iter('year'):
    print(node.tag, node.text)
