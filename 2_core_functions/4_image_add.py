# -*- coding: utf-8 -*-

'Image Arithmetic Operation'

import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print cv2.add(x,y) # 250+10 = 260 => 255
#[[255]]

print x+y         # 250+10 = 260 % 256 = 4
#[4]

img1 = cv2.imread('../assets/lena.jpg')
img2 = cv2.imread('../assets/opencv-logo.png')

dst = cv2.addWeighted(img1, 0.4, img2, 0.5, 0)  # weight


cv2.imshow('image', dst)
cv2.imwrite('img_dst.jpg',dst)
cv2.waitKey(0)
cv2.destoryAllWindow()
