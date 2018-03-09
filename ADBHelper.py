#-*- coding: UTF-8 -*-
'''
    在Python中执行ADB的命令行, 实现对Android设备的操控
'''

from subprocess import Popen, PIPE
import shlex
import cv2
import random
import subprocess

class ADBHelper:
    
    def __init__(self, win_width, win_height, margin = 100):
        '''
            构造器函数
            确认 窗口宽度高度与可按压范围.
        '''
        self.win_width = win_width
        self.win_height = win_height
        # 可以按压的矩形区域 内缩 margin个像素点。
        # 因为屏幕上的边缘 点击会触发别的事件        # region = (x, y, width, height)
        self.press_region = (margin, margin, win_width-margin, win_height-margin)
    @staticmethod
    def getScreenShotByADB():
        '''
            在手机上截图并返回opencv格式的ndarray
        '''
        cmd = "adb shell screencap -p /sdcard/tmp.png"
        subprocess.call(shlex.split(cmd))
        cmd = "adb pull /sdcard/tmp.png tmp.png"
        subprocess.call(shlex.split(cmd))
        # 使用opencv读取图片 返回ndarray
        return cv2.imread("tmp.png")
    

    @staticmethod
    def pressOnScreen(ptr1, delay=500):
        '''
            在屏幕上按压 带延时
        '''
        #随机位置,随机滑动
        ptr20 = (ptr1[0] + random.randint(1, 50),)
        ptr21 = (ptr1[1] + random.randint(1, 50),)
        ptr2 = ptr20+ptr21
        return ADBHelper.pressOnScreenAndMove(ptr1, ptr2, delay)

    @staticmethod
    def pressOnScreenAndMove(ptr1, ptr2, delay=500):
        '''
            按压屏幕并且移动
        '''
        # 命令样例: 'adb shell input touchscreen swipe 170 187 170 187 2000'
        cmd = 'adb shell input touchscreen swipe {} {} {} {} {}'.format(ptr1[0], ptr1[1], ptr2[0], ptr2[1], delay)

        # 运行指令
        rc = subprocess.call(shlex.split(cmd))

        return rc == 0
    
    def randPressOnScreen(self, delay=500):
        '''
            在屏幕上的可按压区域随意选取一个区域， 进行按压
        '''
        (x, y, w, h) = self.press_region

        cx = random.randint(x, x + w)
        cy = random.randint(y, y + h)
        print("Press On  x=%d y=%d , time=%.2f"%(cx, cy, delay))
        return ADBHelper.pressOnScreen((cx, cy), delay)
