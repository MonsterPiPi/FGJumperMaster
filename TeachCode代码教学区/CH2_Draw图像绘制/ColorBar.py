'''
滑块调色板 - v1 比较傻的版本
'''
import cv2
import numpy as np


def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow('image')

# 函数原型
# createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# 解释
# 在window‘iamge’ 上创建一个滑动条，起名为Channel_XXX， 设定滑动范围为0-255, 
# onChange事件回调 啥也不做
cv2.createTrackbar('Channel_Red','image',0,255,nothing)
cv2.createTrackbar('Channel_Green','image',0,255,nothing)
cv2.createTrackbar('Channel_Blue','image',0,255,nothing)

print("进入RGB滑块实验， 键盘摁e退出程序")

while(True):
    cv2.imshow('image',img)
    # 程序跳出判断 最多等待1毫秒
    k = cv2.waitKey(1)
    if k == ord('e'):
        break
    
    # 更新RGB的值
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('Channel_Red','image')
    g = cv2.getTrackbarPos('Channel_Green','image')
    b = cv2.getTrackbarPos('Channel_Blue','image')

    img[:] = [b,g,r]


cv2.destroyAllWindows()