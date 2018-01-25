# -*- coding: utf-8 -*- 
'''
初始化一个空白的画布
并指定画布的颜色
'''

import cv2
import numpy as np

# 初始化一个空画布 300×300 三通道 背景色为黑色 
canvas_black = np.zeros((300, 300, 3), dtype="uint8")
cv2.imshow("canvas_black", canvas_black)

# 初始化一个空画布 300×300 三通道 背景色为白色 
canvas_white = np.ones((300, 300, 3), dtype="uint8")
canvas_white *= 255

cv2.imshow("canvas_white", canvas_white)


'''
初始化一个彩色的画布 - cv2版本
此函数使用 cv2.split 非常耗时 所以只有在需要的时候才能做到。 否则用Numpy索引。

'''
def InitCanvasV1(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    
    # 将原来的三个通道抽离出来， 分别乘上各个通道的值
    (channel_b, channel_g, channel_r) = cv2.split(canvas)
    # 颜色的值与个通道的全1矩阵相乘
    channel_b *= color[0]
    channel_g *= color[1]
    channel_r *= color[2]

    # cv.merge 合并三个通道的值
    return cv2.merge([channel_b, channel_g, channel_r])

'''
初始化一个彩色的画布 - numpy版本
使用numpy的索引　赋值
'''
def InitCanvasV2(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    # Blue 
    canvas[:,:,0] = color[0]
    # Green
    canvas[:,:,1] = color[1]
    # Red
    canvas[:,:,2] = color[2]

    return canvas

'''
初始化终极版本

熟练掌握 numpy 才可以提高工作效率哦
'''
def InitCanvasV3(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

# 初始化一个彩色的画布
canvas_color = InitCanvasV2(300, 300, color=(100, 20, 50))
cv2.imshow("canvas_color", canvas_color)

# 等待e键按下 关闭所有窗口
while cv2.waitKey(0) != ord('e'):
    continue
cv2.destroyAllWindows()
