# -*- coding: utf-8 -*- 
'''
滑块调色板 - v1 比较傻的版本
'''
import cv2
import numpy as np



# 初始化灰度图的画布
def createGrayscaleCanvas(width, height, color=255):
    canvas = np.ones((height, width), dtype="uint8")
    canvas[:] = color
    return canvas


cv2.namedWindow('image')

# 函数原型
# createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# 解释
# 在window‘iamge’ 上创建一个滑动条，起名为Channel_XXX， 设定滑动范围为0-255, 
# onChange事件回调 啥也不做
def nothing(x):
    pass
    
cv2.createTrackbar('gray_value','image',0,255,nothing)


print("进入Grayscale滑块实验， 键盘摁e退出程序")

img = None

# 每隔1ms检查更新一次。
while(True):
    
    # 程序跳出判断 最多等待1毫秒
    k = cv2.waitKey(1)
    # 如果key是e键就退出程序
    if k == ord('e'):
        break
    
    # 获取当前滑条的值
    gvalue = cv2.getTrackbarPos('gray_value','image')
    # 创建新的画布
    img = createGrayscaleCanvas(500, 500, color=gvalue)
    # 显示更新后的图片
    cv2.imshow('image',img)

cv2.destroyAllWindows()