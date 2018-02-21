'''
模板匹配使用示范

官方文档
https://docs.opencv.org/trunk/d4/dc6/tutorial_py_template_matching.html
'''

import cv2
from matplotlib import pyplot as plt


# 导入待匹配图片
img = cv2.imread('basic_box.png')
# 导入模板图片
template = cv2.imread('little_chess.png')
# 获取模板的高度跟宽度
tmp_height, tmp_width,_= template.shape


# 进行模板匹配
res = cv2.matchTemplate(img,template, method=cv2.TM_CCOEFF)



# 获取最大匹配与最小匹配的值与坐标
# maxloc
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 最大位置 max_loc

# 获取模板矩形区域的左上角与右下角
rect_left_upper = max_loc
rect_right_down = (max_loc[0]+tmp_width, max_loc[1]+tmp_height)
# 绘制矩形区域
cv2.rectangle(img, rect_left_upper, rect_right_down, (255, 0, 0), thickness=5)
# 绘制 max_loc的位置
cv2.circle(img, max_loc,5,(0, 0, 255), thickness=-1)

# 输出结果
cv2.imwrite('result.png', img)


# 保存返回的res矩阵
plt.imshow(res, cmap="gray")
plt.savefig('template_match_res.png')
