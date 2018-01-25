# -*- coding: utf-8 -*- 
import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# 读入灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 将灰度图转换为三通道的BGR格式
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# 拼接的图像之间必须是相同的尺寸, 宽度, 高度, 通道数.
stack_img = np.hstack((img, gray))

# 在名字叫做 image_win的窗口下展示图像
cv2.imshow('image', stack_img)
# 检测按下的按钮
print("请按任意键关闭窗口")
key_pressed = cv2.waitKey(0)
print("Key Pressed : {}  == {}".format(key_pressed, chr(key_pressed)))
# cv2.destroyAllWindows()
cv2.destroyWindow('image')