# -*- coding: utf-8 -*- 
'''
寻找下一跳 盒子的位置

思路
    首先对背景色取样, 获取背景色颜色阈值分布与box阴影部分的
    两者分别进行二值化, 然后或操作, 接下来取反, 得到的mask就是box


    实际 因为图像采集自摄像头, 所以不均匀, 单一阈值划分雪崩, 采样来自顶部, 对上方效果很好, 但是对下方就很糟糕

    ? 分水岭算法? 自适应阈值?

    另外还是没想好如何获取 阴影区域 ? 获取并删除

    或者图像求导
'''



import cv2
import numpy as np
from matplotlib import pyplot as plt

def cal_rgb_margin(img):
    # 计算色块的 RGB 三通道的阈值

    (minB, maxB) = cal_single_margin(img, 0)
    (minG, maxG) = cal_single_margin(img, 1)
    (minR, maxR) = cal_single_margin(img, 2)

    threshold_lower = np.int32([minB, minG, minR])
    threshold_upper = np.int32([maxB, maxG, maxR])
    
    return (threshold_lower, threshold_upper)

def cal_single_margin(img, channel):
    # 柱形统计
    hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
    hist = hist.reshape((len(hist)))
    # 概率分布
    prob =  hist / hist.sum()
    # 计算颜色累计分布
    prob_accum = np.zeros_like(prob)
    prob_accum[0] = prob[0]


    # 阈值下界确定状态
    lower_status = False
    # 阈值上界确定状态
    upper_status = False

    # 概率累计分布最小值

    lower_prob = 0.05
    # 概率累计分布最大值

    upper_prob = 0.95

    # 阈值下界值
    lower_value = 0
    # 阈值上界值
    upper_value = 0


    extend_margin = 20

    for i in range(1, len(prob)):
        prob_accum[i] = prob[i] + prob_accum[i-1]
        
        # 确定阈值下界
        if not lower_status and prob_accum[i] > lower_prob:
            lower_value = i
            lower_status = True
        # 确定阈值上界
        if not upper_status and prob_accum[i] > upper_prob:
            upper_value = i
            upper_status = True

    # 拓展边界
    if lower_value - extend_margin < 0:
        lower_value = 0
    else:
        lower_value -= extend_margin
    
    if upper_value + extend_margin > 255:
        upper_value = 255
    else:
        upper_value += extend_margin

    return (lower_value, upper_value)
    
    

# 绘制灰度图的直方图
def draw_gray_hist(img_path):
    # 样例图片
    sample_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    sample_top = sample_img[0:40,:]
    cv2.imshow("top", sample_top)
    plt.hist(sample_top.ravel(), bins=256, range=[0, 256])

    plt.show()


# 绘制RGB彩图的直方图
def draw_rgb_hist(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)  
    # 获取顶部长条(只有背景图片)
    top = img[0:40, :]
    color = ('b', 'g', 'r')  
    for i, col in enumerate(color): 
        histr = cv2.calcHist([top], [i], None, [256], [0, 256])
        print(histr)
        plt.plot(histr, color=col)  
    plt.xlim([0, 256])  
    plt.show()  


# draw_rgb_hist("./samples_roi/1.png")

img_path = "./samples_roi/1.png"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)  
# 获取顶部长条(只有背景图片)
top = img[0:100, :]


'''
# 取样阴影文件, 进行阈值分隔
img = cv2.imread("./samples_roi/4.png", cv2.IMREAD_COLOR)
top = cv2.imread('./image_roi.png', cv2.IMREAD_COLOR)
'''
(threshold_lower, threshold_upper) = cal_rgb_margin(top)

print(threshold_lower)
print(threshold_upper)
# 计算MASK
# 获取背景罩层
bkground_mask = cv2.inRange(img, threshold_lower, threshold_upper)
# 对背景罩层进行 闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 7))  
bkground_mask = cv2.morphologyEx(bkground_mask, cv2.MORPH_CLOSE, kernel)  

# 获取box阴影的罩层 阴影为背景颜色的整体左移.  
shadow_mask = cv2.inRange(img, threshold_lower-60, threshold_upper-50)
# 对box阴影进行闭运算
#闭运算  
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9, 9))  
shadow_mask = cv2.morphologyEx(shadow_mask, cv2.MORPH_CLOSE, kernel)  


#mask = cv2.bitwise_not(mask)
cv2.imshow("image", img)

cv2.imshow("background_mask", bkground_mask)
cv2.imshow("shadow_mask", shadow_mask)
cv2.imshow("box_mask", box_mask)

cv2.imwrite('background_threshold.png', bkground_mask)
cv2.imwrite('shadow_mask.png', shadow_mask)
cv2.imwrite('box_mask.png', box_mask)

while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()
