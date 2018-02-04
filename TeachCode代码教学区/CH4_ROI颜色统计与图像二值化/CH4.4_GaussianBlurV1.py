import numpy as np
import math
from matplotlib import pyplot as plt
from scipy import signal
import cv2

def gaussian(x, mu, sigma):
    return 1/(sigma * math.sqrt(2*math.pi)) * math.e**(-(x-mu)**2/(2*sigma**2))

def gaussian2d(x, y, sigma):
    return (1/(2*math.pi*(sigma**2))) * math.e**(-(x**2 + y**2)/(2*(sigma**2)))

def gaussian_kernal(size, sigma=1.5):
    sigma = 1.5
    # 高斯模糊的核 必须为奇数
    # 半径
    radius = int(size / 2)
    G = np.zeros((size, size))

    for x in range(0, 2*radius+1):
        for y in range(0, 2*radius+1):
            G[x][y] = gaussian2d(x-radius, y-radius, sigma)

    wsum = np.sum(G)
    G = G / wsum

    return G

def draw_gaussian_weight(size, sigma=1.5):
    gweight = gaussian_kernal(size, sigma)
    plt.imshow(gweight, cmap='gray')
    plt.show()


def gray_gaussian_blur(img, size, sigma=1.5):
    F = img
    H = gaussian_kernal(size, sigma)
    return signal.convolve2d(F, H, boundary='wrap',mode='valid')


# print(gaussian_kernal(3))
# draw_gaussian_weight(11)
img = cv2.imread("cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blur = gray_gaussian_blur(gray, 11)
plt.imshow(gray_blur, cmap='gray')
plt.show()