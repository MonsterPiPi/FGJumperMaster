'''
    绘制BGR彩图的统计直方图 V1
'''
from matplotlib import pyplot as plt
import numpy as np
import cv2

# 读入图片
img = cv2.imread('little_chess.png')
if img is None:
    print("图片读入失败, 请检查图片路径及文件名")
    exit()


# Matplotlib预设的颜色字符
bgrColor = ('b', 'g', 'r')

# print(list(enumerate(bgrColor)))

for cidx, color in enumerate(bgrColor):
    # cidx channel 序号
    # color r / g / b
    cHist = cv2.calcHist([img], [cidx], None, [256], [0, 256])
    # 绘制折线图
    plt.plot(cHist, color=color)  


# 设定画布的范围
plt.xlim([0, 256])

# 显示画面
plt.show()