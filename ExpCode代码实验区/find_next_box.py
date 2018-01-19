# -*- coding: utf-8 -*- 
import cv2
import numpy as np


def contours_filter(contours, minWidth=None, minHeight=None, minArea=None):
    
    newCntList = []

    for cnt in contours:
        
        rect = cv2.minAreaRect(cnt)       # 获取最小矩形区域
        area = cv2.contourArea(cnt)       # 获取contour的面积

        width = rect[1][0]
        height = rect[1][1]

        if minWidth and width < minWidth:
            continue
        if minHeight and height < minHeight:
            continue
        if minArea and area < minArea:
            continue

        newCntList.append(cnt)
    return newCntList            
    
def find_top_rectangle(rects):

    top_rect = rects[0]
    for rect in rects[1:]:
        if top_rect[1] > rect[1]:
            top_rect = rect
    
    return top_rect


def get_box_center(box):
    (x, y, w, h) = box
    cx = int(x + w / 2)
    # 取1/3处
    cy = int(y + h / 3)
    
    return (cx, cy)
    
mask = cv2.imread("./box_mask.png", 0)

#  x,y,w,h = cv2.boundingRect(mask)

kernel = np.ones((5,5),np.uint8)
mask =  cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

image, contours, hier = cv2.findContours(mask, cv2.RETR_TREE,
                cv2.CHAIN_APPROX_SIMPLE)

contours = contours_filter(contours, minHeight=50, minWidth=50)
maskrgb = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)


boxes = []

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(maskrgb,(x,y),(x+w,y+h),(0,255,0),2)
    boxes.append((x, y, w, h))
#绘制最上方的色块的矩形
top_box= find_top_rectangle(boxes)
(x, y, w, h)  = top_box
cv2.rectangle(maskrgb,(x,y),(x+w,y+h),(0, 0, 255),4)


# 绘制顶层矩形 中心点
(cx, cy) = get_box_center(top_box)
cv2.circle(maskrgb, (cx, cy), 5, color=(0, 0, 255), thickness=-1)



cv2.imshow("image", maskrgb)

while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()