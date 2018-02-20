import cv2
import numpy as np
from matplotlib import pyplot as plt


img = np.uint8(np.random.randint(0,255,size=(5,5)))

height,width= img.shape


# 声明新的维度
new_dimension = (1000, 1000)


method_map = {
    'INTER_NEAREST': cv2.INTER_NEAREST,
    'INTER_LINEAR': cv2.INTER_LINEAR,
    'INTER_AREA': cv2.INTER_AREA,
    'INTER_CUBIC': cv2.INTER_CUBIC,
    'INTER_LANCZOS4': cv2.INTER_LANCZOS4
}


for key, flag in method_map.items():
    plt.clf()
    plt.subplot(121)
    plt.title("SRC Image")
    plt.imshow(img,cmap='seismic')

    plt.subplot(122)
    resized = cv2.resize(img, new_dimension, interpolation =flag)
    plt.title(key)
    plt.imshow(resized,cmap='seismic')

    plt.savefig('interpolation_{}'.format(key))
