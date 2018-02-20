'''
    数学形态学 腐蚀 erorsion
'''
import cv2
import numpy as np

# 读入灰度图
img = cv2.imread("dao-bin.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建 核
kernel = np.ones((5,5), np.uint8)
# 腐蚀
erorsion_img = cv2.erode(img, kernel, iterations=3)

cv2.imwrite('dao_erorsion_k5_iter3.png', np.hstack((img, erorsion_img)))