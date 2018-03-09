#-*- coding: UTF-8 -*-
'''
    跳一跳 自动跳跃程序
    工程的执行入口
    TODO 程序结束的判断 再玩一局
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#设置系统默认编码
import cv2
import numpy as np
from ADBHelper import ADBHelper
from BlackChess import getChessFootPosi
from NextJumpPlat import getNextJumpPlatCenter
from FGVisonUtil import FGVisionUtil as vutil
import time
import math
import random

def distance2time(distance):
    '''
        距离与延迟时间不完全成正比，需要添加惩罚项
    '''
    print(distance)
    pt1 = (800, 1.6)
    pt2 = (300, 2.4)


    ratio = pt1[1] - (pt1[1]-pt2[1])*(pt1[0]-distance)/(pt1[0]-pt2[0])
    print("distance: %.2f  ratio=%.2f"%(distance, ratio))

    # 时间必须是整数类型
    return int(distance * ratio)



debug = True
# 初始话ADBHelper 传入手机分辨率
adb = ADBHelper(720, 1280)
# 声明窗口NextCenterFinder 展示图像处理过程
cv2.namedWindow('NextCenterFinder', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

while True:
    # 获取手机截图
    img = ADBHelper.getScreenShotByADB()
    # 获取棋子的位置
    chess_posi = getChessFootPosi(img)
    # 获取下一跳中心的位置
    center_posi,canvas = getNextJumpPlatCenter(img,debug=True)
    # 绘制底座位置
    cv2.circle(canvas, chess_posi, 10, (255,255,255), thickness=-1)
    cv2.imshow('NextCenterFinder', canvas)
    
    
    # 计算距离
    distance = vutil.cal_distance(chess_posi, center_posi)
    # 折算延迟
    delay = distance2time(distance)
    # 按压手机屏幕
    #rc = ADBHelper.pressOnScreen((500, 500), delay=delay)
  
    wait_time=1000 + random.randint(10, 1000)
    #随机等待时间
    region = ADBHelper(adb.win_width-200,adb.win_height-200,300)
    #屏幕可按压范围
    rc = region.randPressOnScreen(delay=delay)
    if rc:
        print("成功点击 并延时 "+str(round(float(wait_time)/1000,2)+1)+"s")
        if debug == True:
            # 保存日志  注意需要创建文件路径
            img_name = time.strftime("%Y-%m-%d-%H-%M-%S")+".png"
            #cv2.imwrite('./output/AutoJump/screenshot/'+img_name, img)
            cv2.imwrite('./output/AutoJump/log/'+img_name, canvas)

    # 随机等待2~3S
    key = cv2.waitKey(wait_time)

    if key == ord('q'):
        print("Exit")
        break
# 关闭所有窗口
cv2.destroyAllWindows()
