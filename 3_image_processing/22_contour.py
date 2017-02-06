# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../assets/lena.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# contours is a Python list of all the contours in the image, 每一條 contour 都是 a Numpy array of (x,y)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imwrite('contour0.jpg',img)

cv2.imwrite('contour0_contour.jpg',image)

# 在原圖, 畫上 contours
img1 = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite('contour1.jpg',img1)

# 畫上第四條 contour
img2 = cv2.drawContours(img, contours, 3, (0,255,0), 3)

cv2.imwrite('contour2.jpg',img2)

# 畫上第四條 contour（比較常用的方法）
cnt = contours[4]
img3 = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

cv2.imwrite('contour3.jpg',img)