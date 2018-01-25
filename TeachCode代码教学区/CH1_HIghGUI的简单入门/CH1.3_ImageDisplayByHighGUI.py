# -*- coding: utf-8 -*- 
import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win', cv2.WINDOW_NORMAL)
# 在名字叫做 image_win的窗口下展示图像
cv2.imshow('image_win',img)
# 检测按下的按钮
print("请按任意键关闭窗口")
key_pressed = cv2.waitKey(0)
print("Key Pressed : {}  == {}".format(key_pressed, chr(key_pressed)))
# cv2.destroyAllWindows()
cv2.destroyWindow('image_win')