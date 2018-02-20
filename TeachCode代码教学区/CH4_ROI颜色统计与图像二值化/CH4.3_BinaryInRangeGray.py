'''
    灰度图的图像二值化 演示
'''
import cv2
import numpy as np

# 读入图片
img = cv2.imread('dao_roi.png')
# 判断图片是否正确读入
if img is None:
    print("请检查图片路径")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 阈值下界
lowerb = (30)
# 阈值上界
upperb = (80)

# 图像二值化
mask = cv2.inRange(gray, lowerb, upperb)

cv2.namedWindow("mask", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('mask', mask)
cv2.imwrite('dao-bin.png', mask)
cv2.waitKey(0)