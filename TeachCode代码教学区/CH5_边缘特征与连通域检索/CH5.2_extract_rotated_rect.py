'''
    利用minAreaRect绘制最小面积矩形并绘制
'''
import numpy as np
import cv2

# 读入黑背景下的彩色手写数字
img = cv2.imread("color_number_handwriting.png")
# 转换为gray灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 寻找轮廓
bimg, contours, hier = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for cidx,cnt in enumerate(contours):
    minAreaRect = cv2.minAreaRect(cnt)
    # 转换为整数点集坐标
    # rectCnt = np.int64(cv2.boxPoints(minAreaRect))
    ((cx, cy), (w, h), theta) = minAreaRect
    
    cx = int(cx)
    cy = int(cy)
    w = int(w)
    h = int(h)
    # 获取旋转矩阵
    rotateMatrix = cv2.getRotationMatrix2D((cx, cy), theta, 1.0)
    rotatedImg = cv2.warpAffine(img, rotateMatrix, (img.shape[1], img.shape[0]))
    pt1 = (int(cx - w/2), int(cy - h/2))
    pt2 = (int(cx + w/2), int(cy + h/2))
    # 原图绘制圆形
    cv2.rectangle(rotatedImg, pt1=pt1, pt2=pt2,color=(255, 255, 255), thickness=3)
    cv2.circle(rotatedImg, (cx, cy), 5, color=(255, 0, 0), thickness=-1)
    cv2.imwrite("minarearect_cidx_{}.png".format(cidx), rotatedImg)


    # subNumImg = rotatedImg[pt1[1]:pt1[1]+h, pt1[0]: pt1[0]+w]
    # 判断长宽关系， 如果width 大于 height就进行转置。
    # cv2.imwrite("minarearect_cidx_{}.png".format(cidx), subNumImg)
