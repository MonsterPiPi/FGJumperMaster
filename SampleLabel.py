



'''

self.img 
self.canvas
self.fchess (x, y)
self.cbox (x, y)
self.save_path  图像的保存路径
self.label_filename




init(img)
u-更新画面

cancelLabel:
ctrl + z -> 撤销标注， 更新画面， 重新标注

saveLabel:
ctrl + s-检验标注是否完整， 保存标注 更新画面

addLabel(x, y, type)
    添加标记
    fchess chess footer
    cbox： box center

onMouse:
    监听鼠标事件


helpMenu 
ctrl + h 帮助按钮 打印帮助信息


genImageName 生成图像名称， 利用事件戳

saveImage 保存图片

label2str(img_name, )

saveLabelInfo



numpy 的copy问题
http://blog.csdn.net/u010099080/article/details/59111207


'''

import cv2
import numpy as np
import datetime
import math
import copy
from ADBHelper import ADBHelper

MP_UNMARK = 0 # 0 : 未进行标注
MP_MARKED_FCHESS = 1  # 1 : 标注了小人的底部
MP_MARKED_CBOX = 2 # 2 : 标注了box的中心点




'''
手动标注 两个标签

'''
def markChessAndBoxByHand(event,x,y,flags,sampleLabel):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("click: x= {}, y={}".format(x, y))
        sampleLabel.addLabel(x, y)
    

class SampleLabel:
    def __init__(self, save_path='./', label_filename='label.txt'):
        self.img = None # 原来的图片
        self.canvas = None # 画布
        self.img_name = None # 图片名称
        self.mp = 0 # 标注的进程 
        self.fchess = (0, 0) # 棋子底部中心
        self.cbox = (0, 0) # 下一条盒子的中心
        self.save_path = save_path # 图像的保存路径
        self.label_filename = label_filename #　标签记录文件的文件名
        # self.label_file = open(label_filename, 'w+') # 文件对象
        self.winname = 'label'
        
        # 创建一个窗口
        cv2.namedWindow(self.winname, flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
        cv2.setMouseCallback(self.winname, markChessAndBoxByHand, self)


    def responseToKeyEvent(self, key):
        
        pass
    
    
    def updateImg(self, img, img_name = None):
        # 更新当前源图像
        self.img = img.copy()
        # use copy deep copy
        self.canvas = img.copy()
        self.fchess = (0, 0)
        self.cbox = (0, 0)

        if img_name == None:
            # 根据时间戳　生成文件名
            self.img_name = f"{datetime.datetime.now():%Y-%m-%d-%H-%M-%S-%f.png}"
        else:
            # 如果有名字的话就直接赋值
            self.img_name = img_name

        # 重置标注状态
        self.mp = MP_UNMARK
        
        self.updateCanvas()

    def printProcessOnCanvas(self, info):
        '''
            在画布上显示帮助信息
        '''
        # 首先更新画布
        # self.updateCanvas()
        self.canvas[50:150,:] = 255
        # 选择字体
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        cv2.putText(self.canvas, text=info, org=(100, 100), fontFace=font, fontScale=fontScale, thickness=1, 
                     lineType=cv2.LINE_AA, color=(0, 0, 255))
        

        cv2.imshow(self.winname, self.canvas)

    def updateCanvas(self):
        '''
            根据状态更新画布　与文字提示
        '''
        # Use Deep Copy
        self.canvas = self.img.copy()

        rmarker = 10 # 标记半径
        if self.mp >= MP_MARKED_FCHESS:
            # 绘制chess中心
            # 绘制棋子底部的中心点 红色实心
            cv2.circle(img=self.canvas, center=self.fchess, radius=rmarker, color=(0, 0, 255), thickness=-1)
            
        if self.mp >= MP_MARKED_CBOX:
            # 绘制下一条盒子中心
            cv2.circle(img=self.canvas, center=self.cbox, radius=rmarker, color=(0, 255, 0), thickness=-1)

        if self.mp == MP_UNMARK:
            self.printProcessOnCanvas("step-0 unmarked, mark chess footer first.")

        elif self.mp == MP_MARKED_FCHESS:
            self.printProcessOnCanvas("step-1  you need to mark next box center.") 
    
        elif self.mp == MP_MARKED_CBOX:
            self.printProcessOnCanvas("step-2 mark done, save (s) or cancel (u)")
        
        cv2.imshow(self.winname, self.canvas)
        
    def addLabel(self, x, y):
        
        if self.mp == MP_UNMARK:
            self.fchess = (x, y)
            self.mp = MP_MARKED_FCHESS
        
        elif self.mp == MP_MARKED_FCHESS:
            self.cbox = (x, y)
            self.mp = MP_MARKED_CBOX
        else:
            print("标注已完成")

        print("fchess")
        print(self.fchess)
        print("cbox")
        print(self.cbox)
        print("mp")
        print(self.mp)
        self.updateCanvas()
        
    def isMarkDone(self):
        '''
            返回是否标注完成
        '''
        return self.mp == MP_MARKED_CBOX

    def saveImg(self):
        '''
            保存图片
        '''
        cv2.imwrite(self.save_path + self.img_name, self.img)
        cv2.imwrite(self.save_path + 'log/' + self.img_name, self.canvas)

    def label2string(self):
        (x1, y1) = self.fchess
        (x2, y2) = self.cbox

        return ",".join([self.img_name, str(x1), str(y1), str(x2), str(y2)]) + '\n'
    
    def saveLabelInfo(self):
        # 在文件后面追加 append
        with open(self.label_filename, 'a+') as f:
            f.write(self.label2string())
        
    def onDestroy(self):
        # exit
        # 关闭文件
        # self.label_file.close()
        # 关闭窗口
        cv2.destroyWindow(self.winname)

        # 退出并结束程序。
        exit()