#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 生成验证码
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: identifying_code.py
@time: 16/5/24 下午4:05
"""
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))



# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')



'''
如果运行的时候报错：

IOError: cannot open resource
这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：

'/Library/Fonts/Arial.ttf'
要详细了解PIL的强大功能，请请参考Pillow官方文档：

https://pillow.readthedocs.org/
'''









def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass