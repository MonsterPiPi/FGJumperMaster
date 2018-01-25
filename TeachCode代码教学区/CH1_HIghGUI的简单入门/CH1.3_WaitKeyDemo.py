# -*- coding: utf-8 -*- 
import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
# 这里我们只是演示导入 并不会展示图像

cv2.imshow('image',img)
# 等待按键摁下 最多1s钟
key_pressed = cv2.waitKey(5000)
print("有按键摁下或者已超时")
if key_pressed >= 0:
    print("Key Pressed : {}  == {}".format(key_pressed, chr(key_pressed)))
else:
    print("等待超过5s钟自动执行")

# 关闭所有窗口
cv2.destroyAllWindows()



'''
输出

scorpion@tl ~/D/f/Image> python WaitKeyDemo.py 
有按键摁下或者已超时
等待超过5s钟自动执行

scorpion@tl ~/D/f/Image> python WaitKeyDemo.py 
有按键摁下或者已超时
Key Pressed : 115  == s
'''