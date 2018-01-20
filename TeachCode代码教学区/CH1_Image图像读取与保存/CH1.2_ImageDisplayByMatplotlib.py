# -*- coding: utf-8 -*- 
import numpy as np
import cv2
# 引入Python的可视化工具包 matplotlib
from matplotlib import pyplot as plt

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# plt.imshow(img)
# 直接绘制 ndarray 颜色很诡异
# 原因是opencv读取到的图片是BGR格式的，Matplotlib按照RGB格式解析的
# 所以我们需要将颜色空间转换
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# 隐藏坐标系
plt.axis('off')
# 展示图片
plt.show()
