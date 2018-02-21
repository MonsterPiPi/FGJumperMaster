

import cv2
import numpy
from skimage.transform import hough_ellipse


'''
寻找椭圆形过于耗时
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
    # chess_mask = getChessFootMask(img)
    # edge = cv2.bitwise_and(edge, cv2.bitwise_not(chess_mask))
    return edge



img_path = "../../input/2018-01-25-21-01-12.png"

img = cv2.imread(img_path)
edges = getCannyEdge(img)

result = hough_ellipse(edges, accuracy=20, threshold=250,
                       min_size=100, max_size=120)

print(result)