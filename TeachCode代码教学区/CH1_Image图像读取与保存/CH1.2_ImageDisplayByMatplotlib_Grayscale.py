# -*- coding: utf-8 -*- 
import numpy as np
import cv2
# 引入Python的可视化工具包 matplotlib
from matplotlib import pyplot as plt



def print_img_info(img):
    print("================打印一下图像的属性================")
    print("图像对象的类型 {}".format(type(img)))
    print(img.shape)
    print("图像宽度: {} pixels".format(img.shape[1]))
    print("图像高度: {} pixels".format(img.shape[0]))
    # GRAYScale 没有第三个维度哦， 所以这样会报错
    # print("通道: {}".format(img.shape[2]))
    print("图像分辨率: {}".format(img.size))
    print("数据类型: {}".format(img.dtype))

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)


# 将色彩空间转变为灰度图并展示
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 打印图片信息
# print_img_info(gray)

# 打印图片的局部
# print("打印图片局部")
# print(gray[100:105, 100:105])


# plt.imshow(gray)
# 需要添加colormap 颜色映射函数为gray
plt.imshow(gray, cmap="gray")

# 隐藏坐标系
plt.axis('off')
# 展示图片

plt.show()
# 你也可以保存图片， 填入图片路径就好
# plt.savefig("cat_gray_01.png")