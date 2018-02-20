import cv2
import numpy as np



# 获取旋转矩阵
rotateMatrix = cv2.getRotationMatrix2D((100, 200), 90, 1.0)

np.set_printoptions(precision=2,suppress=True)
print(rotateMatrix)

'''
输出结果

[[   0.    1. -100.]
 [  -1.    0.  300.]]

'''