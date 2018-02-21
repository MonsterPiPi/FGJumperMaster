'''
    跳一跳 自动跳跃程序

    二者连在一起， 当前是个大盒子， 下一跳是个小盒子的时候， 最顶上的并不是下一跳
'''
import cv2
import numpy as np
from ADBHelper import ADBHelper
from BlackChess import getChessFootPosi
from NextJumpPlat import getNextJumpPlatCenter
from FGVisonUtil import FGVisionUtil as vutil
import datetime


def distance2time(distance):
    '''
        距离与延迟时间不完全成正比，需要添加惩罚项
    '''
    ratio = 1.7
    # 0.4 -> 
    punish = 0.00037
    
    # 事件必须是整数类型
    return int(distance * ratio - punish*distance*distance)




adb = ADBHelper(1080, 1920)

cv2.namedWindow('NextCenterFinder', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

while True:

    img = ADBHelper.getScreenShotByADB()
    # 获取棋子的位置
    chess_posi = getChessFootPosi(img)
    # 获取下一跳中心的位置
    center_posi,canvas = getNextJumpPlatCenter(img)

    cv2.imshow('NextCenterFinder', canvas)
    # 保存日志
    img_name =  f"{datetime.datetime.now():%Y-%m-%d-%H-%M-%S-%f.png}"
    cv2.imwrite('./output/AutoJump/screenshot/'+img_name, img)
    cv2.imwrite('./output/AutoJump/log/'+img_name, canvas)

    # 计算距离
    distance = vutil.cal_distance(chess_posi, center_posi)
    # 折算延迟
    delay = distance2time(distance)

    rc = ADBHelper.pressOnScreen((500, 500), delay=delay)
    if rc:
        print("成功点击 并延时 3s")
    key = cv2.waitKey(3000)

    if key == ord('q'):
        print("Exit")
        break

cv2.destroyAllWindows()