'''
利用模板匹配寻找棋子的位置
'''
import cv2

def getChessFooterByTempMatch(img, template, offset=(0,-5)):
    '''
        img: 待要匹配的图片
        template： 模板
        offset： 偏移量 (模板底部中心再往上偏移一些才是棋子的位置)
    '''

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


# 导入待匹配图片
img = cv2.imread('basic_box.png')
# 导入模板图片
template = cv2.imread('little_chess.png')


chess_posi = getChessFooterByTempMatch(img, template)

canvas = img.copy()
cv2.circle(canvas, chess_posi, 10, (0, 0, 255), thickness=-1)

cv2.imwrite("chess_posi_mark.png", canvas)