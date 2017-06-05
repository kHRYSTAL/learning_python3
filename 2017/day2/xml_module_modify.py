#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: xml_module_modify.py
# @time: 17/6/5 下午12:05


import xml.etree.ElementTree as ET
tree = ET.parse('xml_test.xml')
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    # 新增属性
    node.set('updated', 'yes')

tree.write('xml_test.xml')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output.xml')