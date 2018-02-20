


def contours_filter(contours, minWidth=None, maxWidth=None, minHeight=None, maxHeight=None, minArea=None):
    '''
        contours筛选器
    '''    
    newCntList = []

    for cnt in contours:
        
        rect = cv2.minAreaRect(cnt)       # 获取最小矩形区域
        area = cv2.contourArea(cnt)       # 获取contour的面积

        # print(rect)
        width = int(rect[1][0])
        height = int(rect[1][1])

        if minWidth is not None and width < minWidth:
            continue
        if maxWidth is not None and width > maxWidth:
            continue
        if minHeight is not None and height < minHeight:
            continue
        if maxHeight is not None  and height > maxHeight:
            continue
        if minArea is not None and area < minArea:
            continue

        newCntList.append(cnt)
    return newCntList          
