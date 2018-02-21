'''
    图像二值化 演示
'''
import cv2
import numpy as np

# 读入图片
# img = cv2.imread('screenshot5.png')
img = cv2.imread('../../classic_boxes/2018-01-25-20-43-02.png')

# 判断图片是否正确读入
if img is None:
    print("请检查图片路径")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 阈值下界
lowerb = (12, 65, 189)
# 阈值上界
upperb = (21, 135, 255)

# 图像二值化
mask = cv2.inRange(img, lowerb, upperb)

cv2.namedWindow("mask", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.imwrite("bin-chess-hsv.png", mask)