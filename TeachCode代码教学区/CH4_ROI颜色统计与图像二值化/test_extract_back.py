from extract_back import *
from glob import glob
import cv2
import numpy as np


# 获取图片列表
img_path_list = glob('/home/scorpion/Desktop/FGJumperMaster/samples/label/*.png')
# 生成迭代器
img_path_iter = iter(img_path_list)

def getImgName(img_path):
    '''
        从路径名称中提取文件名
    '''
    # 'samples/unlabel/2018-01-25-22-19-42.png' ->  '2018-01-25-22-19-42.png'
    return img_path.split('/')[-1]

def nextImg(img_path_iter):
    '''
        使用迭代器， 遍历数组
    '''
    try:
        # 迭代器 下一个路径
        img_path = next(img_path_iter)
        
        img = cv2.imread(img_path)
        if img is None:
            print('END')
            exit()

        # img = img[600:1200]
        # mask = getBackBinImg(img)
        # cv2.imwrite('./test_binback/'+getImgName(img_path), mask)

        # shadow_mask = getShadowBinImg(img)
        # cv2.imwrite('./test_binshadow/'+getImgName(img_path), shadow_mask)
        chess_mask = getChessBinImg(img)
        
        
        chess_mask = cv2.cvtColor(chess_mask, cv2.COLOR_GRAY2BGR)
        rects,contours = getChessFootPosi(img)

        
        for rect in rects:
            (x, y, w, h) = rect
            cv2.rectangle(chess_mask, (x, y), (x+w, y+h), (0, 255, 0), 5)

        cv2.drawContours(chess_mask, contours, -1, (0,0,255), 3)
        
        cv2.imwrite('./test_chess/'+getImgName(img_path), chess_mask)


        # box_mask = getBoxBinImg(img)
        # cv2.imwrite('./test_binbox/'+getImgName(img_path), box_mask)
        
        # box_noback = cv2.bitwise_and(img, img, mask=box_mask)
        # cv2.imwrite('./test_box/'+getImgName(img_path), box_noback)

        return True
    except StopIteration:
        print("遍历结束")
        return False

    
while nextImg(img_path_iter):
    pass