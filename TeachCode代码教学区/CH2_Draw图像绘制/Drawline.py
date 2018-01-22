import cv2
import numpy as np


# 预设几种颜色 B
COLOR_MAP = {
    "green": (0, 255, 0),
    "red": (0, 0, 255)
}


'''
初始化一个彩色的画布
颜色为BGR色彩空间
'''
def InitCanvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((width, height, 3), dtype="uint8")
    
    # 将原来的三个通道抽离出来， 分别乘上各个通道的值
    (channel_b, channel_g, channel_r) = cv2.split(canvas)
    # 颜色的值与个通道的全1矩阵相乘
    channel_b *= color[0]
    channel_g *= color[1]
    channel_r *= color[2]

    # cv.merge 合并三个通道的值
    return cv2.merge([channel_b, channel_g, channel_r])

# 初始化一个空画布 300×300 三通道 背景色为黑色 
canvas = InitCanvas(300, 300)


# pt1 线段起始点， pt2 线段终止点
# 在画布canvas上， 从(0，0） 到(300,300) 绘制一根绿色直线
cv2.line(canvas, pt1=(0, 0), pt2=(300, 300), color=COLOR_MAP["green"])
# 显示画布
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 颜色变为红色 BGR
red = (0, 0, 255)
# 绘制一根红色的线  宽度为3
cv2.line(canvas, (300, 0), (0, 300), COLOR_MAP["red"], 3)
cv2.imshow("Canvas", canvas)

cv2.imwrite("draw_line.png", canvas)

cv2.waitKey(0)


