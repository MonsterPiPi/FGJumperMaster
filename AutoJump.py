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


def distance2time(distance):
    '''
        距离与延迟时间不完全成正比，需要添加惩罚项
    '''
    ratio = 1.7
    # 0.4 -> 
    punish = 0.00037
    
    # 事件必须是整数类型
    return int(distance * ratio - punish*distance*distance)



debug = False

adb = ADBHelper(1080, 1920)

cv2.namedWindow('NextCenterFinder', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

while True:

    img = ADBHelper.getScreenShotByADB()
    # 获取棋子的位置
    chess_posi = getChessFootPosi(img)
    # 获取下一跳中心的位置
    center_posi,canvas = getNextJumpPlatCenter(img)

    if chess_posi is None or center_posi is None:
        break
    
    cv2.imshow('NextCenterFinder', canvas)
    
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
            cv2.imwrite('./output/AutoJump/log/'+img_name, canvas)


    key = cv2.waitKey(3000)

    if key == ord('q'):
        print("Exit")
        break

cv2.destroyAllWindows()