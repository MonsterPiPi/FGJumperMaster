# -*- coding: utf-8 -*- 
import numpy as np
import cv2



# 初始化灰度图的画布
def createGrayscaleCanvas(width, height, color=255):
    canvas = np.ones((height, width), dtype="uint8")
    canvas[:] = color
    return canvas

# 判断灰度值是否合法
def is_gvalue_legal(gvalue):
    
    return not (gvalue < 0 or gvalue > 255)

#  读入灰度值
#  如果符合要求的话, 就生成对应的背景. 不合法就要求重新输入. 
def read_gvalue():
    # 是否读取成功
    read_done = False
    gvalue = None

    while not read_done:
        
        gvalue_str  = input("请输入灰度值: ")
        gvalue = int(gvalue_str)
        read_done = is_gvalue_legal(gvalue)
        
        if not read_done:
            print("温馨提示, 数值范围越界, 灰度图取值范围在0到255区间")
    return gvalue

gvalue = read_gvalue()

canvas = createGrayscaleCanvas(500, 500, color=gvalue)
cv2.imshow("canvas", canvas)

print("按任意按键结束程序")
cv2.waitKey(0)

cv2.destroyAllWindows()