'''
    绘制灰度图的统计直方图
    -----------------------
    首先我们将图片读入为img, 然后转换为灰度图gray.
    然后将gray 用numpy的ravel函数变为一维的扁平数组, 输入到plt.hist 中.
    了解更多查看numpy.ravel -文档
    最终我们得到灰度图的统计图.
'''

from matplotlib import pyplot as plt
import numpy as np
import cv2


# img = cv2.imread('little_chess.png')
img = cv2.imread('dao_roi.png')
if img is None:
    print("图片读入失败")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
	1Darray: 一维数组　这里通过gray.ravel()，把灰度图变为一维数组．
	bins: 统计分隔区间　如果是256 就是分成256份统计, 你可以修改这个值, 看不同的统计效果
	range: 统计数值的空间
'''

plt.hist(gray.ravel(), bins=256, range=[0, 256])
plt.show()