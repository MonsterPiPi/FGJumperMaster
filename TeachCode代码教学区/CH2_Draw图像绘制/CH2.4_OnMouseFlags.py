# -*- coding: utf-8 -*- 
'''
CTRL + 鼠标左键， 移动鼠标，绘制一个系列圆圈

'''
import cv2  
import numpy as np  
  

# CTRL + 鼠标左键， 移动鼠标，绘制一个系列圆圈
def draw_circle(event,x,y,flags,param): 
    # 判断事件是否为 Left Button Double Clicck 
    print(flags)
    print(cv2.EVENT_FLAG_LBUTTON | cv2.EVENT_FLAG_CTRLKEY)
    if event == cv2.EVENT_MOUSEMOVE and flags == (cv2.EVENT_FLAG_LBUTTON | cv2.EVENT_FLAG_CTRLKEY ):  
        cv2.circle(img,(x,y),20,(255,0,0),-1)
        

# 创建一个黑色图像，并绑定窗口和鼠标回调函数  
img = np.zeros((512,512,3), np.uint8)  
cv2.namedWindow('image')
# 设置鼠标事件回调
cv2.setMouseCallback('image',draw_circle)  
  
while(True):  
    cv2.imshow('image',img)  
    if cv2.waitKey(20) == ord('q'):  
        break  
cv2.destroyAllWindows()

# 保存图片
cv2.imwrite("MousePaint01.png",  img)
