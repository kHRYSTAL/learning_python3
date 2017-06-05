#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: xml_module_create.py
# @time: 17/6/5 下午12:13

import xml.etree.ElementTree as ET

new_xml = ET.Element('person_info_list')
person_info = ET.SubElement(new_xml, 'person_info', attrib={'enrolled': 'yes'})
age = ET.SubElement(person_info, 'age', attrib={'checked': 'no'})
sex = ET.SubElement(person_info, 'sex')
name = ET.SubElement(person_info, 'name')
name.text = 'kHRYSTAL'
age.text = '23'
person_info2 = ET.SubElement(new_xml, 'person_info', attrib={'enrolled': 'yes'})
age = ET.SubElement(person_info2, 'age')
name = ET.SubElement(person_info2, 'name')
name.text = 'yyg'
age.text = '19'


et = ET.ElementTree(new_xml)
# 第三个参数为声明是否为xml格式
et.write('xml_create_test.xml', encoding='utf-8', xml_declaration=True)

ET.dump(new_xml)
