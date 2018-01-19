# -*- coding: utf-8 -*- 
'''
获取chess底部的中心点


'''


import cv2
import numpy as np

# 样例图片
sample_img = cv2.imread("./samples_roi/1.png")

threshold_lower = np.int32([19, 0, 0])
threshold_upper = np.int32([74, 16, 19])
mask = cv2.inRange(sample_img, threshold_lower, threshold_upper)

# cv2.imshow("Mask Source Image", mask)

#闭运算  
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9, 9))  
closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  

#开运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 7)) 
opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel) 

cv2.imshow("2.Open", opened)


# 寻找区域内的最大矩形

# 寻找当前小人所处的矩形区域 (联通域)
x,y,w,h = cv2.boundingRect(opened)

# 标注一下小人所在的矩形区域
cv2.rectangle(sample_img,(x,y),(x+w,y+h),(0,255,0),2)
# 在小人的下面点一个红点
cv2.circle(sample_img, (int(x+w/2), y+h), 5, color=(0, 0, 255), thickness=-1)


cv2.imshow("img mark", sample_img)




while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()