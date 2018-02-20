'''
    提取跳一跳背景
    基于一个前提 峰值处于背景所在的分布内
'''
import cv2
import numpy as np
from FGVisonUtil import FGVisionUtil as vutils

def fitBGRBValue(rgb_value, addWeight=0):
    '''
        rgb值 添加或者减去一个值，并确保数值范围在合理区间内 0 - 255
    '''
    MIN_VALUE = 0
    MAX_VALUE = 255
    for i in range(len(rgb_value)):
        if rgb_value[i] + addWeight < MIN_VALUE:
            rgb_value[i] = MIN_VALUE
        elif rgb_value[i] + addWeight > MAX_VALUE:
            rgb_value[i] = MAX_VALUE
        else:
            rgb_value[i] += addWeight

def findCurveBoundary(array, start, win_size=4):
    '''
        给定一个切入点， 获取该点所在颜色分布
    '''
    zero_threshold = 300
    bin_num = len(array)
    leftb = start
    rightb = start
    print(start)
    while leftb >= 0 and array[leftb] > zero_threshold:
        leftb -= 1
    
    while rightb < bin_num and array[rightb] > zero_threshold:
        rightb += 1

    return (max(0, leftb*win_size-20), min(255, rightb*win_size+25))

def getMaxCurveBoundary(array, win_size=4):
    '''
        找到背景色的边界， 默认占比最大的颜色分布为背景色的颜色分布
    '''
    zero_threshold = 10
    segments = []
    bin_num = len(array)

    binIdx = 0
    while binIdx < bin_num:
        if array[binIdx] < zero_threshold:
            #print('next %d'%(binIdx))
            pass
        else:
            # 找到一个区域
            segment = [binIdx, binIdx, array[binIdx]]
            binIdx += 1
            while binIdx < bin_num and array[binIdx] > zero_threshold:
                segment[1] = binIdx
                segment[2] += array[binIdx]
                binIdx += 1
            segments.append(segment)           
        binIdx += 1
    
    # 从segments列表中寻找面积最大的（segment[2]）
    max_segment = max(segments, key=lambda s:s[2])
    return (max(0,max_segment[0]*win_size), min(255,max_segment[1]*win_size))
    
def getBackBGRBoundary(img, win_size=4):
    '''
        获取背景图片的 RGB边界阈值
    '''
    
    back_img = np.hstack((img[:,0:100], img[:,img.shape[1]-100:img.shape[1]])) # 背景取样区域 左边宽度为50的长条区域

    lowerb = np.uint8([0, 0, 0])
    upperb = np.uint8([255, 255, 255])
    bin_num = 256 / win_size
    for cidx in range(3):
        cHist = cv2.calcHist([back_img], [cidx], None, [bin_num], [0, 256])
        (leftIdx, rightIdx) = getMaxCurveBoundary(cHist.reshape((len(cHist))), win_size=win_size)
        lowerb[cidx] = leftIdx
        upperb[cidx] = rightIdx
    return (lowerb, upperb)

def getBackBinImg(img):
    '''
        获取背景的二值化图像
    '''
    (lowerb, upperb) = getBackBGRBoundary(img, win_size=1)
    mask = cv2.inRange(img, lowerb, upperb)
    return mask

def getShadowBinImg(img):
    '''
        获取盒子阴影的二值化图像
    '''
    win_size = 1

    (back_lowerb, back_upperb) = getBackBGRBoundary(img, win_size=1)
    shadow_middle = np.uint8(back_lowerb/2 + back_upperb/2)
    fitBGRBValue(shadow_middle, -70) # 影子颜色分布的其中一个值
    
    lowerb = np.uint8([0, 0, 0])
    upperb = np.uint8([255, 255, 255])
    bin_num = 256 / win_size
    for cidx in range(3):
        cHist = cv2.calcHist([img], [cidx], None, [bin_num], [0, 256])
        (leftIdx, rightIdx) = findCurveBoundary(cHist.reshape((len(cHist))), int(shadow_middle[cidx]/win_size), win_size=win_size)
        lowerb[cidx] = leftIdx
        upperb[cidx] = rightIdx

    mask = cv2.inRange(img, lowerb, upperb)
    return mask

def getChessBinImg(img):
    '''
        获取棋子的二值化图像。
        颜色阈值是之前我们在CH4.2中统计得到的。
    '''
    # 阈值下界
    lowerb = (50, 36, 36)
    # 阈值上界
    upperb = (104, 80, 80)
    mask = cv2.inRange(img, lowerb, upperb)
    # 闭运算， 去除棋子头部的黑洞
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9,9)), iterations=6)
    return mask

def getBoxBinImg(img):
    '''
        获取盒子的二值化图像
    '''
    back_mask = getBackBinImg(img)
    shadow_mask = getShadowBinImg(img)
    chess_mask = getChessBinImg(img)

    mask_tmp = cv2.bitwise_or(back_mask, shadow_mask)
    mask_tmp = cv2.bitwise_or(mask_tmp, chess_mask)
    box_mask = cv2.bitwise_not(mask_tmp)

    (height, width) = box_mask.shape
    # 去除上部的无关信息
    box_mask[0:300] = 0
    box_mask[height-300:height] = 0

    # 简单腐蚀
    kernel = np.ones((3,3))
    box_mask = cv2.erode(box_mask, kernel, iterations=1)
    # 闭运算， 去除黑洞
    kernel = np.ones((3,3))
    box_mask = cv2.morphologyEx(box_mask, cv2.MORPH_CLOSE, kernel,iterations=2)
    return box_mask

def getChessFootPosi(img):
    MIN_CHESS_WIDTH = 65
    MAX_CHESS_WIDTH = 80

    MIN_CHESS_HEIGHT = 200
    MAX_CHESS_HEIGHT = 230


    chess_mask = getChessBinImg(img)
    image, contours, hier = cv2.findContours(chess_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
    contours = vutils.contours_filter(contours, minHeight=MIN_CHESS_HEIGHT, maxHeight=MAX_CHESS_HEIGHT, minWidth=MIN_CHESS_WIDTH, maxWidth=MAX_CHESS_WIDTH)
    rects = []
    for c in contours:
        (x, y, w, h)= cv2.boundingRect(c)
        
        rects.append((x,y,w,h))
    
    return rects,contours

if __name__ == "__main__":
    img = cv2.imread("screenshot4.png")

    # mask = getChessBinImg(img)
    # cv2.imwrite('s4_binchess.png', mask)

    box_mask = getBoxBinImg(img)
    cv2.imwrite('s4_binbox.png', box_mask)
    ''''
    img = img[600:1200]
    (lowerb, upperb) = getBackBGRBoundary(img, win_size=4)
    print('Lower Boundary')
    print(lowerb)
    print('Upper Boundary')
    print(upperb)
    cv2.namedWindow('mask', flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

    # 图像二值化
    mask = cv2.inRange(img, lowerb, upperb)
    cv2.imshow('mask', mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''