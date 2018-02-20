'''
    利用minAreaRect绘制最小面积矩形并绘制
'''
import numpy as np
import cv2

# 读入黑背景下的彩色手写数字
img = cv2.imread("color_number_handwriting.png")
# 转换为gray灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 寻找轮廓
bimg, contours, hier = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 声明画布 拷贝自img
canvas = np.copy(img)

for cidx,cnt in enumerate(contours):
    minAreaRect = cv2.minAreaRect(cnt)
    # 转换为整数点集坐标
    rectCnt = np.int64(cv2.boxPoints(minAreaRect))
    # 绘制多边形
    cv2.polylines(img=canvas, pts=[rectCnt], isClosed=True, color=(0,0,255), thickness=3)

cv2.imwrite("number_minarearect_canvas.png", canvas)