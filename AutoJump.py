'''
    跳一跳 自动跳跃程序

    TODO 程序结束的判断 再玩一局
'''
import cv2
import numpy as np
from ADBHelper import ADBHelper
from BlackChess import getChessFootPosi
from NextJumpPlat import getNextJumpPlatCenter
from FGVisonUtil import FGVisionUtil as vutil
import datetime
import math

def distance2time(distance):
    '''
        距离与延迟时间不完全成正比，需要添加惩罚项
    '''
    ratio = 2.0
    # 0.4 -> 
    w1 = 0.025
    w2 = 1.5
    w3 = 1.8
    # 事件必须是整数类型
    return int(distance * ratio - w1*math.pow(distance,3/2) + w2*math.pow(distance, 1/2) + w3*math.pow(distance, 1/4))



debug = True
# 初始话ADBHelper 传入手机分辨率
adb = ADBHelper(1080, 1920)
# 声明窗口NextCenterFinder 展示图像处理过程
cv2.namedWindow('NextCenterFinder', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

while True:
    # 获取手机截图
    img = ADBHelper.getScreenShotByADB()
    # 获取棋子的位置
    chess_posi = getChessFootPosi(img)
    # 获取下一跳中心的位置
    center_posi,canvas = getNextJumpPlatCenter(img)
    
    
    
    # 计算距离
    distance = vutil.cal_distance(chess_posi, center_posi)
    # 折算延迟
    delay = distance2time(distance)

    rc = ADBHelper.pressOnScreen((500, 500), delay=delay)
    if rc:
        print("成功点击 并延时 3s")
        if debug == True:
            # 保存日志  注意需要创建文件路径
            img_name =  f"{datetime.datetime.now():%Y-%m-%d-%H-%M-%S-%f.png}"
            cv2.imwrite('./output/AutoJump/screenshot/'+img_name, img)
            # 绘制底座位置
            cv2.circle(canvas, chess_posi, 10, (255,255,255), thickness=-1)
            cv2.imshow('NextCenterFinder', canvas)
            cv2.imwrite('./output/AutoJump/log/'+img_name, canvas)


    key = cv2.waitKey(3000)

    if key == ord('q'):
        print("Exit")
        break

cv2.destroyAllWindows()