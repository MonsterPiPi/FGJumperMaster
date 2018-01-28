# -*- coding: utf-8 -*- 
from FGJumperMaster import FGJumperMaster

import cv2


from glob import glob

sample_folder = "./samples_roi"
sample_path_list = glob("%s/*.png"%(sample_folder))

# 遍历所有的样本图片
for sp in sample_path_list:
    print(sp)
    img = cv2.imread(sp)

    JM = FGJumperMaster(img)
    cv2.imwrite('./output/%s'%(sp[len(sample_folder)+1:]), JM.visualization())
    cv2.imwrite('./output_details/%s'%(sp[len(sample_folder)+1:]), JM.visualization_detail())