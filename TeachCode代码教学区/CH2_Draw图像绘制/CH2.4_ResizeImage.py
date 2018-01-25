# -*- coding: utf-8 -*- 
import cv2
import numpy as np

def imgResize(img, ratio = 1):
    height, width = img.shape[:2]
    res = cv2.resize(img,(int(ratio*width), int(ratio*height)), interpolation = cv2.INTER_CUBIC)
    return res



huaji = cv2.imread("20180126huaji.jpg")
cv2.imwrite("smallhuaji.png",imgResize(huaji, 0.2))
