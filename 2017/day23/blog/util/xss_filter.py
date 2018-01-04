#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: xss_filter.py
# @time: 18/1/4 上午11:20


content = """
<p class='c1' id='i1'>
asassadsad<span style="font-familyLNSimSun;">asd<a>asdas</a></span>sadsad
</p>
<p>
    <strong class='c2' id='i2'>asdas</strong>
    <script>alert(123);</script>
</p>
<h2>fgdgf</h2>
"""
# 1.标签白名单
tags = ['p', 'strong']

# 2.标签(携带属性)白名单
tags = {
    'p': ['class'],  # p标签只要class属性
    'strong': ['id'],  # strong 只要 id属性
}

from bs4 import BeautifulSoup

# 以html解析字符串
soup = BeautifulSoup(content, 'html.parser')

# 遍历字符串所有标签
for tag in soup.find_all():
    # print(tag.name)
    if tag.name in tags:  # 如果在白名单,什么都不做
        pass
    else:
        tag.hidden = True  # 只隐藏标签
        tag.clear()  # 清空标签间的内容
        continue  # 删除标签后, 跳出此次循环

    input_attrs = tag.attrs  # 获取当前标签的属性, 如p:['class':'c1', 'id': 'i1']
    # print(input_attrs)
    valid_attrs = tags[tag.name]  # 获取当前标签符合白名单的属性, 如p的['class']
    """
    在列表遍历时 是不能进行插入删除操作的 会直接报错, 因为会影响到计算结果
    因此 在遍历时 应该把列表转换为迭代器list(),再进行操作 因为迭代器不会计算长度 每次next只会获取下一项
    实际上相当于拷贝了一份列表 然后对原始列表进行操作
    """
    for k in list(input_attrs.keys()):
        if k in valid_attrs:  # 如果属性在白名单中, 什么也不做, 如p中的class
            pass
        else:
            del tag.attrs[k]  # 删除这个标签不在白名单的属性, 如p中的id

content = soup.decode()  # 重新编码成html字符串
print('after')
print(content)
