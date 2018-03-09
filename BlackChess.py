#-*- coding: UTF-8 -*-
'''
寻找棋子chess的位置

* 首先根据颜色阈值进行寻找
* 如果没有找到的话就通过使用模板匹配找到棋子的位置
'''

import cv2
import numpy as np
from  FGVisonUtil import FGVisionUtil as vutils


def getChessFootByTempMatch(img, template=None, offset=(0,-5)):
    '''
        利用模板匹配寻找棋子的位置
        img: 待要匹配的图片
        template： 模板
        offset： 偏移量 (模板底部中心再往上偏移一些才是棋子的位置)
    '''
    if template is None:
        # 读入预设的模板
        template = cv2.imread('little_chess.png')
        # 判断模板是否读取正确
        if template is None:
            print("ERROR: 请检查模板文件路径")
            exit()

    # 获取模板的高度跟宽度
    tmp_height, tmp_width,_= template.shape
    # 进行模板匹配
    res = cv2.matchTemplate(img, template, method=cv2.TM_CCOEFF)
    # 获取最大匹配与最小匹配的值与坐标
    # 因为采用的匹配方式是 cv2.TM_CCOEFF 所以最大值位置是我们想要的棋子位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 棋子底部中心位置
    (x, y) = max_loc
    (delta_x, delta_y) = offset
    chess_posi = (int(x + tmp_width/2 + delta_x), int(y + tmp_height + delta_y))

    return chess_posi


def getChessFootMask(img):
    '''
        利用HSV阈值获取棋子的掩模
    '''
    # 先转换为HSV格式的图片
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 阈值下界
    lowerb = (104, 33, 58)
    # 阈值上界
    upperb = (136, 121, 104)

    # 图像二值化
    mask = cv2.inRange(img_hsv, lowerb, upperb)
    # 闭运算， 去除棋子头部的黑洞
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9,9)), iterations=6)

    return mask

def getChessFootByColor(img):
    '''
        利用颜色检索棋子位置
    '''
    MIN_CHESS_WIDTH = 65
    MAX_CHESS_WIDTH = 80

    MIN_CHESS_HEIGHT = 200
    MAX_CHESS_HEIGHT = 230


    chess_mask = getChessFootMask(img)
    image, contours, hier = cv2.findContours(chess_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    
    contours = vutils.contours_filter(contours, minHeight=MIN_CHESS_HEIGHT, maxHeight=MAX_CHESS_HEIGHT, minWidth=MIN_CHESS_WIDTH, maxWidth=MAX_CHESS_WIDTH)

    if len(contours) == 1:
        # 刚好匹配到目标棋子
        (x, y, w, h)= cv2.boundingRect(contours[0])
        # 返回棋子坐标
        return (int(x+w/2), int(y+h))
    else:
        return None

def getChessFootPosi(img):
    '''
        寻找棋子chess的位置
    '''
    posi = getChessFootByColor(img)
    # 先使用颜色阈值方案
    if posi is not None:
        return posi    
    else:
        # 备选方案使用模板匹配
        return getChessFootByTempMatch(img)


if __name__=='__main__':
    if __name__ == '__main__':
        from glob import glob
    # 待测试的游戏截图， 否放置在./input文件夹下
    img_paths = glob('./input/*.png')

    for path in img_paths:
        img_name = path.split('/')[-1]

        img = cv2.imread(path)
        
        canvas = img.copy()

        chess_mask = getChessFootMask(img)
        canvas = cv2.cvtColor(chess_mask, cv2.COLOR_GRAY2BGR)

        chess_posi = getChessFootPosi(img)
        cv2.circle(canvas, chess_posi, 10, (0,0, 255), thickness=-1)

        cv2.imwrite('./output/chess/'+img_name, np.hstack((img, canvas)))
