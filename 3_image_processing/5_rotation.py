# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../assets/lena.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D( (cols/2,rows/2),90,1 )
frame = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('frame',frame)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
