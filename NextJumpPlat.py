'''
    提取跳一跳 下一跳的平台平面
'''
import cv2
import numpy as np
from FGVisonUtil import FGVisionUtil as vutils
from BlackChess import getChessFootMask
import math

'''
放弃颜色阈值的方案

def getBackBoundary(img, win_size=1):
    # 获取背景图片的 HSV边界阈值
    
    # 设定采样窗口
    back_img = np.hstack((img[:,0:50], img[:,img.shape[1]-50:img.shape[1]])) # 背景取样区域 左边宽度为50的长条区域
    
    back_img = cv2.cvtColor(back_img, cv2.COLOR_BGR2HSV)
    lowerb = np.uint8([0, 0, 0])
    upperb = np.uint8([255, 255, 255])
    bin_num = 256 / win_size
    for cidx in range(3):
        cHist = cv2.calcHist([back_img], [cidx], None, [bin_num], [0, 256])
        (leftIdx, rightIdx) = vutils.getMaxCurveBoundary(cHist, win_size=win_size,zero_threshold=0, offset=(0,0))
        lowerb[cidx] = leftIdx
        upperb[cidx] = rightIdx
    return (lowerb, upperb)


def getBackGroundMask(img):
    
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 背景颜色的阈值
    (lowerb, upperb) = getBackBoundary(img, win_size=1)
    # 获取背景
    back_mask = cv2.inRange(img_hsv, lowerb, upperb)

    # 获取阴影的阈值
    lowerb[2] -= 80
    upperb[2] -= 70
    # 将阈值放缩到合适的区间内
    lowerb = vutils.fitBGRBValue(lowerb)
    upperb = vutils.fitBGRBValue(upperb)
    shadow_mask = cv2.inRange(img_hsv, lowerb, upperb)

    # 二者合并
    mask = cv2.bitwise_or(back_mask, shadow_mask)
    
    # 涂抹顶部跟底部的区域

    wdith, height = mask.shape[::-1]
    mask[0: int(height/4),:] = 255
    mask[int(3*height/4): height,:] = 255
    # back_mask = cv2.bitwise_or(back_mask, shadow_mask)
    
    cv2.imwrite('test_shadow_mask.png', shadow_mask)
    return mask
'''

def getCannyEdge(img):
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_size = 5
    threshold1 = 150
    threshold2 = 100

    edgeB = cv2.Canny(img[:,:,0], threshold1, threshold2, apertureSize=sobel_size)
    edgeG = cv2.Canny(img[:,:,1], threshold1, threshold2, apertureSize=sobel_size)
    edgeR = cv2.Canny(img[:,:,2], threshold1, threshold2, apertureSize=sobel_size)

    edge = cv2.bitwise_or(cv2.bitwise_or(edgeB, edgeG), edgeR)
    
    # 抹掉小人
    chess_mask = getChessFootMask(img)
    edge = cv2.bitwise_and(edge, cv2.bitwise_not(chess_mask))

    height, width = edge.shape
    edge[0:int(height/4)] = 0
    edge[int(3*height/4):] = 0
    return edge

def isNextPoint(cur_pt, next_pt, x_direction=-1):
    '''
        拓展下一个点
        x_direction = -1 向左拓展
        x_direction = =1 向右拓展
    '''
    x1,y1 = cur_pt
    x2,y2 = next_pt

    if (x1 - x2) * x_direction > 0 or y1 - y2 > 5:
        # 判断方向是否匹配 
        # 对y轴方向小的起伏做滤波作用
        return False
    elif x1 == x2 and y2 - y1 > 5:
        # 检测较大落差 ->判断为垂直竖线
        return False
    return True

def isInShadow(refer_backcolor, hsv_value):
    '''
        refer_backcolor 为参考背景色(hsv 格式)
        hsv_value 用来验证是否是阴影
    '''
    # 验证H通道
    if abs(int(refer_backcolor[0])-int(hsv_value[0])) > 5:
        return False
    # 验证S通道
    if abs(int(refer_backcolor[1])-int(hsv_value[1])) > 5:
        return False


    delta_s =  int(refer_backcolor[2])- int(hsv_value[2])
    if delta_s > 70 and delta_s < 80:
        return True
    return False


def getLittleWhitePointCenter(img, offset=(0,0), debug=False):
    '''
        找到下一跳的中心白点
    '''
    lowerb = (245, 245, 245)
    upperb = (245, 245, 245)
    
    
    mask = cv2.inRange(img, lowerb, upperb)
    image, contours, hierarchy = cv2.findContours(image=mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    contours = vutils.contours_filter(contours, minWidth=35, maxWidth=45, minHeight=20, maxHeight=30)
    
    if len(contours) != 1:
        return None
    
    
    (x, y, w, h) = cv2.boundingRect(contours[0])
    cx = int(x+w/2+offset[0])
    cy = int(y+h/2+offset[1])

    if debug == False:
        return (cx, cy)
    else:
        canvas = img.copy()
        print("w: {}, h: {}".format(w, h))
        cv2.rectangle(canvas, (x,y), (x+w, y+h), (0,0,255), thickness=4)
        return (cx, cy), canvas


def adjust_points(top_point, left_point, right_point):
    '''
    根据左右两点的比值，来适当调整端点位置
    > 便利店轮廓 锯齿太多
    '''
    x1,y1 = top_point
    x2,y2 = left_point
    x3,y3 = right_point

    left_len = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2, 2))
    right_len = math.sqrt(math.pow(x1-x3,2) + math.pow(y1-y3, 2))
    
    ratio = left_len / right_len
    if ratio < 1/3:
        # 左边太短， 调整left_point
        left_point = (2*top_point[0]-right_point[0], right_point[1])
    elif ratio > 3:
        # 右边太短
        right_point = (2*top_point[0]-left_point[0], left_point[1])

    return (top_point, left_point, right_point)
def getNextJumpPlatCenter(img, debug=False):
    '''
        获取下一跳平台的中心
    '''
    # 声明画布
    canvas = img.copy()

    edge = getCannyEdge(img)
    # 获取边缘信息
    image, contours, hierarchy = cv2.findContours(image=edge, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    contours = vutils.contours_filter(contours, minWidth=50, minHeight=50)
    
    # 找到最大
    next_box_cnt = min(contours, key=lambda cnt: tuple(cnt[cnt[:,:,1].argmin()][0])[1])
    
    # 顶点序号
    top_point_idx = next_box_cnt[:,:,1].argmin()
    # 顶点
    top_point = tuple(next_box_cnt[top_point_idx,0,:2])
    
    # 背景色取样
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    refer_back_color = img_hsv[top_point[1], top_point[0]]

    left_idx_itr = 1
    right_idx_itr = -1
    if next_box_cnt[top_point_idx+left_idx_itr,0, 0] > top_point[0]:
        left_idx_itr, right_idx_itr = right_idx_itr, left_idx_itr 

    right_pt_idx = top_point_idx+right_idx_itr
    left_pt_idx = top_point_idx+left_idx_itr

    right_point = None
    left_point = None

    # 寻找右边的边缘点
    while True:
        # 当前right point
        right_point = tuple(next_box_cnt[right_pt_idx,0,:2])
        next = tuple(next_box_cnt[right_pt_idx+right_idx_itr,0,:2])
        
        if not isNextPoint(right_point, next, x_direction=1):
            break
        elif isInShadow(refer_back_color, img_hsv[next[1]+5, next[0]]):
            # 判断边缘下方的五个像素是不是阴影
            break
        
        right_pt_idx += right_idx_itr
    
    # 寻找左边的边缘点
    while True:
        left_point = tuple(next_box_cnt[left_pt_idx,0,:2])
        next = tuple(next_box_cnt[left_pt_idx+left_idx_itr,0,:2])

        if not isNextPoint(left_point, next, x_direction=-1):
            break
        elif isInShadow(refer_back_color, img_hsv[next[1]+5, next[0]]):
            break

        left_pt_idx += left_idx_itr
    # 调整三个点的位置
    (top_point, left_point, right_point) = adjust_points(top_point, left_point, right_point)
    down_point = (left_point[0]+right_point[0]-top_point[0],left_point[1]+right_point[1]-top_point[1])

    # 生成下一跳平台的搜索区域
    # TODO 检索椭圆形 四边形
    contour = np.array([
        [list(top_point)],
        [list(right_point)],
        [list(down_point)],
        [list(left_point)]])

    (x, y, w, h) = cv2.boundingRect(contour)
    # 在矩形区域内检索小白点提示
    res_pt = getLittleWhitePointCenter(img[y:y+h, x:x+w], offset=(x,y))
    
    center_point = None
    if res_pt is not None:
        # print("find white point")
        # print(res_pt)
        center_point = res_pt
    else:
        # 取left_point与right_point 中间处作为中心点
        cx = int((left_point[0]+right_point[0])/2)
        cy = int((left_point[1]+right_point[1])/2)
        center_point = (cx, cy)

    if debug == True:
        cv2.drawContours(image=canvas, contours=[next_box_cnt], contourIdx=-1, color=(125,125,125), thickness=1)
        canvas[top_point[1],top_point[0]] = [0,0,255]

        canvas[left_point[1],left_point[0]] = [0, 255, 0]
        canvas[right_point[1], right_point[0]] = [255, 0, 0]

        next_right = tuple(next_box_cnt[right_pt_idx+right_idx_itr,0,:2])
        canvas[next_right[1], next_right[0]] = [0,0,0]
        next_left = tuple(next_box_cnt[left_pt_idx+left_idx_itr,0,:2])
        canvas[next_left[1], next_left[0]] = [0,0,0]

        print('LEFT: {}, TOP: {}, RIGHT: {}'.format(left_point, top_point, right_point))
        print('rect region : {}'.format((x, y, w, h)))
    else:
        # 设定圆圈半径
        pt_radius = 10
        # 绘制轮廓
        cv2.drawContours(image=canvas, contours=[next_box_cnt], contourIdx=-1, color=(0,0,255), thickness=3)
        cv2.circle(canvas, top_point, pt_radius, (0, 255, 0), thickness=-1)
        cv2.circle(canvas, left_point, pt_radius, (0, 255, 255), thickness=-1)
        cv2.circle(canvas, right_point, pt_radius, (255, 0, 0), thickness=-1)
        cv2.circle(canvas, down_point, pt_radius, (255,255,0), thickness=-1)
        # 绘制检索框
        # x,y,w,h = next_plat_rect
        # cv2.rectangle(canvas, (x,y), (x+w, y+h), (255,255,255), thickness=2)
        cv2.circle(canvas, center_point, pt_radius, (45,100,255), thickness=-1)
    
    return center_point,canvas
    # otsu method  
    # threshold,imgOtsu = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # return imgOtsu

if __name__ == '__main__':
    from glob import glob

    img_paths = glob('./input/*.png')

    for path in img_paths:
        img_name = path.split('/')[-1]

        img = cv2.imread(path)
        
        
        edge = getCannyEdge(img)
        cv2.imwrite('./output/edge/'+img_name, edge)
        
        '''
        white_point_center, canvas = getLittleWhitePointCenter(img)
        # if white_point_center is not None :
        cv2.imwrite('./output/mask/white_points/'+img_name, canvas)
        '''
        
        center_point, canvas = getNextJumpPlatCenter(img,debug=False)
        # print("center: {}".format(center_point))
        cv2.imwrite('./output/next_jump_plat/'+img_name, canvas)
        
