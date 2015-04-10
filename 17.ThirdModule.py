#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------常用第三方模块------------------------------'
#需要先安装PIL，参考印象笔记

print u'--------------------- 1. 图像处理：PIL -----------------------------'
import Image

print u'--------------------- 1.1 获得尺寸、缩放、另存为 ----------------------'
# 打开一个jpg图像文件
im = Image.open('20150407102729.jpg')
# 获得图像尺寸
w, h = im.size
print (w, h)
# 缩放到50%:
im.thumbnail((w/2, h/2))
# 把缩放后的图像用jpeg格式保存:
im.save('./testdir/thumbnail.jpg', 'jpeg')

print u'--------------------- 1.2 模糊效果 ----------------------'
import Image, ImageFilter

img = Image.open('20150407102729.jpg')
img2 = img.filter(ImageFilter.BLUR)
img2.save('./testdir/blur.jpg', 'jpeg')

print u'--------------------- 1.3 绘图：生成验证码 ----------------------'#注：运行为通过
import Image, ImageDraw, ImageFont, ImageFilter
import random

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
#可以根据操作系统提供字体的绝对路径，如Arial.ttf
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)

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
image.save('code.jpg', 'jpeg');