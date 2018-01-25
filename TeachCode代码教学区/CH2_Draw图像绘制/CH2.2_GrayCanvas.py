# -*- coding: utf-8 -*- 
import numpy as np
import cv2



# 初始化灰度图的画布
def createGrayscaleCanvas(width, height, color=255):
    canvas = np.ones((height, width), dtype="uint8")
    canvas[:] = color
    return canvas



canvas = createGrayscaleCanvas(500, 500, color=125)

cv2.imshow("canvas", canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()