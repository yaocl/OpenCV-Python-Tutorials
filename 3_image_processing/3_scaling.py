# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../assets/lena.jpg')

frame = cv2.resize(img,None,fx=2, fy=1.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow('frame1',frame)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

# OR

height, width = img.shape[:2]
frame = cv2.resize(img,(2*width, int(1.5*height)) , interpolation = cv2.INTER_CUBIC)

cv2.imshow('frame2',frame)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()