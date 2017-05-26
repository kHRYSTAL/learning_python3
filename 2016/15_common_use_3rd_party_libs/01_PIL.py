#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
PIL功能非常强大，但API却非常简单易用。

@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 01_PIL.py
@time: 16/5/24 下午3:41
"""
'''
先安装pip：
sudo easy_install pip
然后安装PIL：
sudo -H pip install Pillow
最后导入Image模块：
import PIL.Image
或者
from PIL import Image
'''

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpeg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpeg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass