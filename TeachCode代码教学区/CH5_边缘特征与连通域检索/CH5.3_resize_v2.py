import cv2
import numpy as np

img = cv2.imread('cat.png')
height,width,channel = img.shape


# 指定新图片的维度与插值算法（interpolation）
resized = cv2.resize(img, None, fx=1.5, fy=2)

cv2.imwrite('cat_resize_fx_fy.png', resized)