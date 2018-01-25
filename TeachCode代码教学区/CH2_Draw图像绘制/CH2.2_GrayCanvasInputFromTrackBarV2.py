# -*- coding: utf-8 -*- 
'''
滑块调色板 - v2 回调函数
'''
import cv2
import numpy as np



# 初始化灰度图的画布
def createGrayscaleCanvas(width, height, color=255):
    canvas = np.ones((height, width), dtype="uint8")
    canvas[:] = color
    return canvas

# 更新画布
def updateImg(gvalue):
    
    img = createGrayscaleCanvas(500, 500, color=gvalue)
    # 显示更新后的图片
    cv2.imshow('image',img)


cv2.namedWindow('image')    
# 初始化画布
updateImg(0)

cv2.createTrackbar('gray_value','image',0,255,updateImg)


print("进入Grayscale滑块实验， 键盘摁e退出程序")

img = None
# 接收按键事件， 判断是否退出
while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()