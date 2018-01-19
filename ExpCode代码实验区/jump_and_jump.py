# -*- coding: utf-8 -*- 
import numpy as np
import cv2


# Init Video Capture
cap = cv2.VideoCapture(1)


# 获取手机上的截图
def getPhoneScreenshot(cap):
    # 旋转角度
    rotate_degree = 90
    # 从Video Capture中读取图片
    ret, frame = cap.read()
    # 判断图像是否获取成功
    if not ret:
        print("图像获取失败")
        return None
    
    # 图片镜像
    cv2.flip(frame, -1)
    # 获取图像的行数与列数 channels 通道=3
    (rows,cols,channels) = frame.shape
    # 获取旋转矩阵
    M = cv2.getRotationMatrix2D((cols/2,rows/2), rotate_degree, 1)
    # 旋转图片
    dst = cv2.warpAffine(frame, M, (cols,rows))
    return dst
