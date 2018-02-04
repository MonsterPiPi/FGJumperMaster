import numpy as np
import cv2

kernel_size = (5, 5);
sigma = 1.5;

img = cv2.imread('cat.jpg')
cv2.imshow("src", img)

img_blur = cv2.GaussianBlur(img, kernel_size, sigma)
cv2.imshow('gaussian_blur', img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
