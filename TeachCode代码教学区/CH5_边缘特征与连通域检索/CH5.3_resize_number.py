import numpy as np
import cv2
from glob import glob


img_paths = glob('./number_raw/*.png')

# 新的维度为10×20
new_dimension = (15, 25)

for img_path in img_paths:
    # 读入灰度图
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    img_name = img_path.split('/')[-1]
    # 缩放
    resized = cv2.resize(img, new_dimension)
    # 二值化图片
    ret,thresh = cv2.threshold(resized,10,255,0)

    cv2.imwrite('./number_bin/'+img_name,thresh)

