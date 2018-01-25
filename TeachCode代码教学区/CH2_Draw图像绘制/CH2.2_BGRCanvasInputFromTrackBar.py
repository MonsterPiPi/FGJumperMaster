# -*- coding: utf-8 -*- 
'''
滑块调色板 - V2 利用回调更新窗口图像
'''

import cv2
import numpy as np


# 创建一个空白画布
canvas = np.zeros((300,512,3), np.uint8)
# 色块的颜色
color = (0, 0, 0)

# 更新图像，并且刷新windows
def updateImage():
    global canvas
    global color

    canvas[:] = color
    
    cv2.imshow('image', canvas)

# 更新颜色
def updateColor(x):
    global color
    r = cv2.getTrackbarPos('Channel_Red','image')
    g = cv2.getTrackbarPos('Channel_Green','image')
    b = cv2.getTrackbarPos('Channel_Blue','image')

    color = (b, g, r)

    updateImage()



cv2.namedWindow('image')

# 函数原型
# createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# 解释
# 在window‘iamge’ 上创建一个滑动条，起名为Channel_XXX， 设定滑动范围为0-255, 
# onChange事件回调 啥也不做
cv2.createTrackbar('Channel_Red','image',0,255,updateColor)
cv2.createTrackbar('Channel_Green','image',0,255,updateColor)
cv2.createTrackbar('Channel_Blue','image',0,255,updateColor)

print("进入RGB滑块实验， 键盘摁e退出程序")

# 首次初始化窗口的色块
# 后面的更新 都是由getTrackbarPos产生变化而触发
updateImage()

while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()